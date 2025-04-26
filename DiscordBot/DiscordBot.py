import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    raise ValueError("🚫 DISCORD 봇 토큰이 설정되지 않았습니다! .env 파일을 확인하세요.")

# 디스코드 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="sk ", intents=intents)

queue = []
current_song = None

# 다운로드 폴더 설정
DOWNLOAD_DIR = "./downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)  # 다운로드 폴더 없으면 생성

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("🔊 음성 채널에 연결되었어요!")
    else:
        await ctx.send("🚫 음성 채널에 들어간 후 명령어를 사용하세요!")

@bot.command()
async def play(ctx, *, query):
    vc = ctx.voice_client
    if not vc:
        if ctx.author.voice:
            vc = await ctx.author.voice.channel.connect()
            await ctx.send("🔊 자동으로 음성 채널에 연결했어요!")
        else:
            await ctx.send("🚫 음성 채널에 먼저 들어가 주세요!")
            return

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "default_search": "ytsearch1",  # 검색 결과를 1개로 제한
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=True)
            filename = ydl.prepare_filename(info)
            song_path = os.path.splitext(filename)[0] + ".mp3"

            # 다운로드가 끝난 후에 파일이 실제로 존재하는지 확인
            if not os.path.exists(song_path):
                await ctx.send("🚫 음원 파일 다운로드에 실패했습니다.")
                return

            # 검색한 곡을 대기열에 추가
            queue.append({"path": song_path, "title": info.get("title", "Unknown")})

            if not vc.is_playing():
                await next(ctx)

    except Exception as e:
        await ctx.send(f"🚫 노래를 찾는 도중 오류가 발생했습니다: {str(e)}")



async def next(ctx):
    global current_song
    vc = ctx.voice_client

    if queue:
        song = queue.pop(0)
        current_song = song

        def after_play(error):
            if error:
                print(f"Error: {error}")
            bot.loop.create_task(next(ctx))

        vc.play(discord.FFmpegPCMAudio(song["path"]), after=after_play)
        await ctx.send(f"🎶 Now Playing: {song['title']}")
    else:
        current_song = None
        await ctx.send("⏹️ 모든 곡이 끝났습니다!")

@bot.command()
async def pause(ctx):
    vc = ctx.voice_client
    if vc and vc.is_playing():
        vc.pause()
        await ctx.send("⏸️ 음악이 일시 정지되었습니다!")
    else:
        await ctx.send("🚫 음악이 재생 중이 아닙니다!")

@bot.command()
async def resume(ctx):
    vc = ctx.voice_client
    if vc and vc.is_paused():
        vc.resume()
        await ctx.send("▶️ 음악이 재개되었습니다!")
    else:
        await ctx.send("🚫 음악이 일시 정지되지 않았습니다!")

@bot.command()
async def skip(ctx):
    vc = ctx.voice_client
    if vc and vc.is_playing():
        vc.stop()
        await next(ctx)
        await ctx.send("⏭️ 곡이 건너뛰어졌습니다!")
    else:
        await ctx.send("🚫 재생 중인 음악이 없습니다!")

@bot.command()
async def list(ctx):
    if queue:
        queue_titles = [f"{i+1}. {song['title']}" for i, song in enumerate(queue)]
        await ctx.send("📜 현재 대기 목록:\n" + "\n".join(queue_titles))
    else:
        await ctx.send("🚫 대기 목록에 곡이 없습니다.")

@bot.command()
async def clear(ctx):
    global queue
    queue.clear()
    await ctx.send("🧹 대기열이 모두 비워졌습니다! 현재 재생 중인 곡은 계속 재생돼요.")

@bot.command()
async def stop(ctx):
    vc = ctx.voice_client
    if vc:
        vc.stop()
        await vc.disconnect()
        await ctx.send("⏹️ 음악 정지 및 채널 나가기")

bot.run(TOKEN)
