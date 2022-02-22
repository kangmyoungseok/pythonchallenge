# http://www.pythonchallenge.com/pc/return/italy.html

import requests
from PIL import Image
import io
image_url = "http://www.pythonchallenge.com/pc/return/wire.png"

headers = {
    'Authorization' : 'Basic aHVnZTpmaWxl'
}
response = requests.get(image_url,headers = headers)
img = Image.open(io.BytesIO(response.content))
answer_img = Image.new("RGB",(100,100))
# 1: 10000 이미지를 나눠서 담기

N = 100
x = 0
y = 0
idx = 0
while N > 0 :
    
    # 오른쪽으로 이동(N)
    for j in range(N):
        answer_img.putpixel((x,y),img.getpixel((idx,0)))
        idx = idx + 1
        x = x + 1
    x = x -1 
    y = y + 1    
    
    # 아래로 이동(N-1)
    for j in range(N-1):
        answer_img.putpixel((x,y),img.getpixel((idx,0)))
        idx = idx + 1
        y = y + 1
    y = y -1
    x = x -1


    # 왼쪽으로 이동(N-1)
    for j in range(N-1):
        answer_img.putpixel((x,y),img.getpixel((idx,0)))
        idx = idx + 1
        x = x - 1
    x = x + 1
    y = y - 1
    
    # 위로 이동 (N-2)
    for j in range(N-2):
        answer_img.putpixel((x,y),img.getpixel((idx,0)))
        idx = idx + 1
        y = y -1
    y = y + 1
    x = x + 1

    N = N - 2

answer_img.show()


