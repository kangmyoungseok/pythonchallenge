# http://www.pythonchallenge.com/pc/def/peak.html

import requests
import pickle

response = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
datas = pickle.loads(response.content)

for raw in datas:
    print("".join([word * repeat for word,repeat in raw]))

