# http://www.pythonchallenge.com/pc/return/mozart.html

import requests
from PIL import Image
import io
import numpy as np

image_url = "http://www.pythonchallenge.com/pc/return/mozart.gif"

headers = {
    'Authorization' : 'Basic aHVnZTpmaWxl'
}
response = requests.get(image_url,headers = headers)
img = Image.open(io.BytesIO(response.content))  # mozart.gif 다운

# img.show()
print(img.size) # 640,480
print(img.mode) # P 

# 분홍색의 pixel 값 찾기 --> 연속된 pixel, 4개 이상은 연속되어 보임
pink_idx = 0  # 195
for y in range(1):
    for x in range(4,img.width):
        if(img.getpixel((x-3,0)) == img.getpixel((x-2,0)) == img.getpixel((x-1,0)) == img.getpixel((x,0)) ):
            print(img.getpixel((x,0)))
            pink_idx=img.getpixel((x,0))
            break


# 분홍색을 첫번째 인덱스가 되도록 정렬
# putpixel로 하나씩 값을 넣어주는 방법과 / frombytes 형식으로 한번에 바이트를 다 넣어주는 방식이 있음
# 이번문제는 frombytes로 해보기
new_img = Image.new("P",img.size)
new_img.putpalette(img.getpalette())

# 원본 이미지를 다루기 위해서 nparray 사용
# np를 이용해서 roll(옆으로 밀기)

numpy_img = np.array(img)
shifted_row = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in numpy_img  ]
shifted_byte =  b"".join(shifted_row)
new_img.frombytes(shifted_byte)

new_img.show()
