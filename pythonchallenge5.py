# http://www.pythonchallenge.com/pc/def/peak.html

# peakhell 이 pickle이랑 발음이 비슷하다니 ,,, ㅡㅡ 

import requests
import pickle

response = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
datas = pickle.loads(response.content)

#print(datas)
#for data in datas:
#    print(data)

for raw in datas:
    print("".join([word * repeat for word,repeat in raw]))

