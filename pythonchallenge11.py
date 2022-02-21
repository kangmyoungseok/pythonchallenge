# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

img = Image.open("cave.jpg")

width,height = img.size
print(width,height)

# index의 합이 짝수인것과 홀수인것을 분리해 보자
even_image = Image.new("RGB",(width+1,height+1))
odd_image = Image.new("RGB",(width+1,height+1))

for row_idx in range(width):
    for column_idx in range(height):
        if( (row_idx + column_idx) % 2 == 0): # 짝수인 경우
            even_image.putpixel((row_idx,column_idx),img.getpixel((row_idx,column_idx)))
            even_image.putpixel((row_idx,column_idx+1),img.getpixel((row_idx,column_idx)))
        else:
            odd_image.putpixel((row_idx,column_idx),img.getpixel((row_idx,column_idx)))
            odd_image.putpixel((row_idx,column_idx+1),img.getpixel((row_idx,column_idx)))


even_image.show()
odd_image.show()


