# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/channel.zip

from zipfile import ZipFile
import re


zip_obj = ZipFile('channel.zip')
print(zip_obj.read("readme.txt").decode("ascii"))


next = 90052

answer = ''
# 그다음은 끝까지 반복문, comment 수집
while True:
    result = zip_obj.read(str(next)+'.txt')
    if ('Next nothing is' in str(result)):
        answer += zip_obj.getinfo(str(next)+'.txt').comment.decode('ascii')
        next = re.sub(r'[^0-9]','',str(result))        
    else:
        print(result.decode("ascii"))
        break

print(answer)

# 답은 hockey가 아니라 OXYGEN 이란다 ^^