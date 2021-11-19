def strange_number(s):
    flag = False
    length = len(s)
    for i in range(length):
        d = s[i]
        if d=='2' or d=='3' or d=='4' or d=='5' or d=='7':
            return False
        if d=='6':
            if s[length-1-i]!='9':
                flag = True
            continue
        if d=='9':
            if s[length-1-i]!='6':
                flag = True
            continue
        if d!=s[length-1-i]:
            flag = True
    return flag

count = 0
n = int(input())
for i in range(1, n+1):
    if strange_number(str(i)):
        count +=1
print(count)