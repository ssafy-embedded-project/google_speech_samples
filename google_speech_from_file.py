# google_speech_from_file.py
from google.cloud import speech
import io

# 사용할 파일 위치
local_file_path = '/home/pi/test.wav'

# Instantiates a client
client = speech.SpeechClient()

# 리퀘스트 구성
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code="ko-KR",  # 영어라면 en-US
)
with io.open(local_file_path, "rb") as f:   # 오디오 파일. 바이너리모드로 읽는다.
    content = f.read()
audio = speech.RecognitionAudio(content=content)

# 리퀘스트 보내고 응답 받아온다.
response = client.recognize(config=config, audio=audio)

for result in response.results: # results 는 음성이 잠시 멈출 때로 구분되는 여러개의 세그멘트의 리스트.( 한 문장 ~= 한 세그먼트)
    print(f"Transcript: {result.alternatives[0].transcript}")  # 각 세그먼트의 alternatives항목은 복수개의 제안일 수 있으며, 가능성이 높은 순으로 정렬되므로 대부분의 경우 alternatives[0]을 사용한다.
