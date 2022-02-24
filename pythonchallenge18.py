# http://www.pythonchallenge.com/pc/return/balloons.html

import gzip
from difflib import Differ
# 파일 열기
f = gzip.open('deltas.gz')

# 좌우로 나눠서 배열에 담기
# difflib.compare에서 한줄 단위로 비교를 하기 위해서 각각의 줄을 list로 담아야 한다.

lines = f.readlines()

left = []
right = []
for line in lines:
    left.append((line[:53] + b'\n').decode())
    right.append(line[56:].decode() )

# 각각 비교해서 결과를 3개의 파일로 저장

f1 = open("common.png","wb")
f2 = open("left.png","wb")
f3 = open("right.png","wb")

compare = Differ().compare(left,right)

for line in compare:
    compare_result = line[0]
    arr = line[2:].rstrip('\n').split()
    answer_bytes = bytes([ int(byte,16)  for byte in arr]   )

    # 공통인 경우 공통 파일에 쓰기
    if(compare_result == ' '):
        f1.write(answer_bytes)
    if(compare_result == '-'):
        f2.write(answer_bytes)
    if(compare_result == '+'):
        f3.write(answer_bytes)
    

f1.close()
f2.close()
f3.close()
f.close()

