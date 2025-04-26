# SkrrBot

SkrrBot은 Discord 음성 채널에서 음악을 재생할 수 있는 Python 기반의 봇입니다. YouTube에서 음악을 다운로드하고, 음성 채널에 연결하여 음악을 재생할 수 있습니다.

## 기능

- **음악 재생**: YouTube 링크 또는 검색어로 음악을 재생합니다.
- **음악 일시 정지 / 재개**: 음악을 일시 정지하고, 다시 재개할 수 있습니다.
- **음악 건너뛰기**: 현재 재생 중인 음악을 건너뛰고, 대기 목록의 다음 음악을 재생합니다.
- **대기 목록 조회**: 현재 대기 중인 음악 목록을 확인할 수 있습니다.
- **음악 정지 및 채널 나가기**: 음악을 정지하고, 봇이 음성 채널에서 나갑니다.

## 설치

이 봇을 사용하려면 Python 3.11 이상이 설치되어 있어야 합니다. 또한, `yt-dlp`, `discord.py`, `python-dotenv` 등의 라이브러리가 필요합니다.

### 1. 클론

먼저 이 프로젝트를 클론합니다.

```bash
git clone https://github.com/yourusername/SkrrBot.git
cd SkrrBot
```

### 2. 가상 환경 설정 (선택 사항)

가상 환경을 설정하여 의존성 패키지를 관리할 수 있습니다.

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3. 필수 패키지 설치

필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

### 4. .env 파일 설정

`.env` 파일을 생성하고, 디스코드 봇 토큰을 설정합니다. `.env` 파일에 아래와 같이 작성해주세요.

```env
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

`YOUR_DISCORD_BOT_TOKEN`을 [Discord Developer Portal](https://discord.com/developers/applications)에서 생성한 봇의 토큰으로 변경합니다.

### 5. 실행

봇을 실행하려면 아래 명령어를 사용하세요.

```bash
python DiscordBot.py
```

## 명령어

봇은 `sk`라는 접두어를 사용합니다.

- **`sk join`**: 음성 채널에 봇을 연결합니다.
- **`sk play <URL/검색어>`**: 음악을 재생합니다. YouTube 링크 또는 검색어로 음악을 재생할 수 있습니다.
- **`sk pause`**: 현재 음악을 일시 정지합니다.
- **`sk resume`**: 일시 정지된 음악을 재개합니다.
- **`sk skip`**: 현재 재생 중인 음악을 건너뛰고, 대기 목록에서 다음 음악을 재생합니다.
- **`sk list`**: 현재 대기 목록에 있는 음악들을 확인합니다.
- **`sk stop`**: 음악을 정지하고, 음성 채널에서 나갑니다.
- **`sk clear`**: 대기 목록을 모두 지웁니다. (현재 재생 중인 음악은 계속 들을 수 있습니다.)

## 라이선스

MIT 라이선스에 따라 배포됩니다. 더 자세한 사항은 [LICENSE](LICENSE) 파일을 참조하세요.