def notPalindrom(string):
    length = len(string)
    for i in range(length//2):
        if not string[0+i]==string[length-1-i]:
            return True
    return False

def is69(string):
    length = len(string)
    for i in range(length//2):
        if (string[0+i]==9 and string[length-1-i]==6) or (string[0+i]==6 and string[length-1-i]==9):
            return True
    return False

def num(string):
    flag = False
    length = len(string)
    if string[length-1]=='0':
        flag = True
    for i in range(length):
        if string[i]=='2' or string[i]=='3' or string[i]=='4' or string[i]=='5' or string[i]=='7':
            return False
        if string[i]=='6' or string[i]=='9':
            flag = True
    if not flag and notPalindrom(string):
        flag = True
    elif is69(string):
        flag = False
    return flag

n = int(input())
count = 0
for i in range(1, n+1):
    if num(str(i)):
        count+=1
print(count)