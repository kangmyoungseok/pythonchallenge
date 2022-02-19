# http://www.pythonchallenge.com/pc/def/linkedlist.php

from pytest import param
import requests
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

params ={'nothing' : 12345}
response = requests.get(url,params=params)

while True:
    params['nothing']= re.sub(r'[^0-9]','',response.text)
    response = requests.get(url,params = params)
    if('and the next nothing' not in response.text):
        print(response.text)
        break
    else:
        print(response.text[-5:])

# 중간에 한번 수동작업 해줘야 함
params = {'nothing' : 8022}
response = requests.get(url,params=params)

while True:
    params['nothing']= re.sub(r'[^0-9]','',response.text)
    response = requests.get(url,params = params)
    if('and the next nothing' not in response.text):
        print(response.text)
        break
    else:
        print(re.sub(r'[^0-9]','',response.text))