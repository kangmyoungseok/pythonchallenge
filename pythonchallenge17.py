# http://www.pythonchallenge.com/pc/return/romance.html

import requests
from PIL import Image
import io
import numpy as np
import re
from urllib.parse import unquote_to_bytes
import bz2

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?"

params = {
    'busynothing' : '12345'
}

response = requests.get(url,params=params)
response.cookies.get('info')
response.text

number_pattern = 'is [0-9]+$'

secret = ''
while True:
    try:
        response = requests.get(url,params=params)
        secret += response.cookies.get('info')
        next_number = re.search(number_pattern,response.text).group()[3:]
        params['busynothing'] = next_number
        print('\rsecret : {}'.format(secret),end='')
    except:
        print(response.text)
        break

bz_file = unquote_to_bytes(secret)
bz2.decompress(bz_file).decode("ascii")

# 1 월 26 일 -> 모차르트 얘기 -> 아빠 -> Leopold
# Leopold 에게 전화 -> 13번 문제


import xmlrpc.client

# XML 서버와 프록시 연결
server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
server.phone("Leopold")


url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
cookies = {'info' : 'the flowers are on their way'}

response = requests.get(url,cookies=cookies)
response.text #balloons
