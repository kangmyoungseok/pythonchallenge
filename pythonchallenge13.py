# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client

# XML 서버와 프록시 연결
server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

# XML 서버에서 사용가능한 Method들 
server.system.listMethods()
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']


# 이전 문제에서 나온 힌트 ;; 
server.phone("Bert")

