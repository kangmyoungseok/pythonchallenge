# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
import numpy as np

R = 0
G = 1
B = 2

img = Image.open('oxygen.png')

numpy_img = np.array(img)

# 115 115 115 가 회색이므로 회색이 들어 있는 열 선택
message_row = np.ndarray
for row in numpy_img:
    if(row[0][R] == 115 and row[0][G] == 115 and row[0][B] == 115 ):
        message_row = row
        break

# RGB가 동일한 픽셀들 선택
message = ''
for pixel in message_row:
    if(pixel[R] == pixel[G] == pixel[B]):
        message += chr(pixel[R])

# 메시지가 7번씩 반복 되므로 하나만 선택
message = message[::7]
print(message)
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]


next_level_ascii = [105,110,116,101,103,114,105,116,121]
next_level = ''
for asc in next_level_ascii:
    next_level += chr(asc)

print(next_level)
# integrity