from pydub import AudioSegment
import os

def split_m4a_to_wav(input_file, output_dir, segment_length=20):
    # m4a 파일 불러오기
    audio = AudioSegment.from_file(input_file, format="m4a")

    # 출력 폴더 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 오디오 길이 (ms 단위)
    total_length = len(audio)

    # 20초(20000ms) 간격으로 자르기
    for i in range(0, total_length, segment_length * 1000):
        segment = audio[i:i + segment_length * 1000]
        output_file = os.path.join(output_dir, f"segment_{i // 1000}-{(i + segment_length * 1000) // 1000}.wav")
        segment.export(output_file, format="wav")
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    input_file = "input.m4a"  # 변환할 m4a 파일 이름
    output_dir = "output_wav"  # 변환된 wav 파일이 저장될 폴더
    split_m4a_to_wav(input_file, output_dir)
    print("모든 파일 변환 완료!")
