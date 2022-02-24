# http://www.pythonchallenge.com/pc/hex/bin.html

import requests
import base64
import soundfile

# 주석에 있는 파일 indian.wav 파일 다운
response = requests.get("http://www.pythonchallenge.com/pc/hex/bin.html",auth=('butter','fly'))

start_idx = response.text.index('UklG')
end_idx = response.text.index("JQBA=") + 5

wav_file = response.text[start_idx:end_idx]
with open('indian.wav',"wb") as f:
    f.write(base64.b64decode(bytes(wav_file,'utf-8')))


# indian.wav 파일 big-endian 형식으로 변환
indian = soundfile.SoundFile('indian.wav',mode='r')
print(indian)
# SoundFile('indian.wav', mode='r', samplerate=11025, channels=1, format='WAV', subtype='PCM_16', endian='FILE')

soundfile.write('big.wav',
                indian.read(),
                indian.samplerate,
                indian.subtype,
                'BIG',
                indian.format
                )

# 기본 윈도우 오디오 재생으로는 안되서 5k player로 재생하니까 됨

