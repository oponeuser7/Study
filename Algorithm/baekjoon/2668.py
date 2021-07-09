n = int(input())
dic = {}
result = []
for i in range(n):
    dic[i] = int(input())
for i in range(n):
    temp = i
    while(True):
        
        if temp in dic:
            next = dic.get(temp)
            if temp == next:
                del dic[next]
                result.append(next)
                break
            else:
