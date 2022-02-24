# http://www.pythonchallenge.com/pc/hex/idiot2.html


import requests
import re

url = "http://www.pythonchallenge.com/pc/hex/idiot2.html"
response = requests.get(url,auth=('butter','fly'))

url_img = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
response = requests.get(url_img,auth=('butter','fly'))
response.headers
# Content-Range : bytes 0-30202/2123456789
# 전체 데이터중 앞에 30202바이트만 받은게 현재 이미지. 나머지 데이터 요청

headers = {
    'Range' : 'bytes=30203-'
}

# 순차적으로 처리

while True:
    try:
        response = requests.get(url_img,auth=('butter','fly'),headers=headers)
        next_bytes = re.findall('\d+',response.headers.get('Content-Range'))[1]
        headers['Range'] = 'bytes={}-'.format(int(next_bytes)+1)
        print(response.text)
    except:
        break

# 뒤에서 부터 시도
answer = ''
for i in range(100):
    headers = {
        'Range' : 'bytes={}-'.format(2123456788-i)
    }

    response = requests.get(url_img,auth=('butter','fly'),headers=headers)
    print(response.headers)
    try:
        response.headers.get('Content-Range')
        answer = response.text
        print(answer[::-1])
        # the password is your new nickname in reverse
        break
    except:
        continue


headers['Range'] = 'bytes=2123456743-'
response = requests.get(url_img,auth=('butter','fly'),headers=headers)

print(response.headers.get('Content-Range'))
# bytes 2123456712-2123456743/2123456789
print(response.text)
# and it is hiding at 1152983631.

headers['Range'] = 'bytes=1152983631-'
response = requests.get(url_img,auth=('butter','fly'),headers=headers)

with open("result.zip","wb") as f:
    f.write(response.content)

len(response.text[0:100])
print(response.content[0:100])

