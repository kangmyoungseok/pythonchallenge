# http://www.pythonchallenge.com/pc/hex/idiot2.html

import zlib
import bz2
f = open("result/package.pack","rb")
data = f.read()

data = zlib.decompress(data)
answer = ''
while True:
    try:
        if(data[0:2] == b'x\x9c'):
            data = zlib.decompress(data)
            answer += '1'
        elif(data[0:2] == b'BZ'):
            data = bz2.decompress(data)
            answer += '#'
        else:
            data = zlib.decompress(data[::-1])            
            answer +='\n'
    except KeyboardInterrupt:
        print("keyboard Interrupt")
        break
    except:
        print("finish decompress")
        print(data)
        break
    
print(answer) # COPPER

