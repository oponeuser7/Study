import re

def filt(string):
    ip = re.compile("\d+.\d+.\d+.\d+")
    mac1 = re.compile("\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}")
    mac2 = re.compile("\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}")
    ip = ip.match(string)
    mac1 = mac1.match(string)
    mac2 = mac2.match(string)
    if ip:
        d = ip.group().split('.')
        if int(d[0])<255 and int(d[1])<255 and int(d[2])<255 and int(d[3])<255:
            return "IP"
    if mac1:
        flag = True
        d = mac1.group().split('-')
        for h in d:
            if not ((ord('0')<=ord(h[0])<=ord('9') or ord('A')<=ord(h[0])<=ord('F')) and (ord('0')<=ord(h[1])<=ord('9') or ord('A')<=ord(h[1])<=ord('F'))):
                flag = False
        if flag:
            return "MAC"
    if mac2:
        flag = True
        d = mac2.group().split(':')
        for h in d:
            if not ((ord('0')<=ord(h[0])<=ord('9') or ord('A')<=ord(h[0])<=ord('F')) and (ord('0')<=ord(h[1])<=ord('9') or ord('A')<=ord(h[1])<=ord('F'))):
                flag = False
        if flag:
            return "MAC"
    return 0

while True:
    try:
        print(filt(input()))
    except EOFError:
        break