# http://www.pythonchallenge.com/pc/def/map.html

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def shift_right(text,num):
    answer = ''
    for character in text:
        if(character.isalpha()):
            next_char = chr(ord(character)+num)
            if(next_char.isalpha() == False):
                next_char = chr(ord(next_char)-26)
            answer += next_char
        else:
            answer += character
        
    return answer

print(shift_right(string,2))


# string.maketransa 이용해서 풀면 이렇게
before_string = 'abcdefghijklmnopqrstuvwxyz'
after_string = 'cdefghijklmnopqrstuvwxyzab'
transtab = string.maketrans(before_string,after_string)

string.translate(transtab)

string = 'map'
shift_right(string,2)