from collections import deque

n = int(input())
dic = {}
result = []
for i in range(1,n+1):
    dic[i] = int(input())
for i in range(1,n+1):
    temp = i
    check = True
    stack = deque()
    mem = set()
    while(check):
        if temp not in dic:
            break
        next = dic.get(temp)
        stack.append(temp)
        if next == temp:
            del dic[next]
            result.append(next)
            break
        if next in mem:
            while(True):
                x = stack.pop()
                del dic[x]
                result.append(x)
                if x == next:
                    check = False
                    break
            break
        mem.add(temp)
        temp = next
result.sort()
print(len(result))
for i in result:
    print(i)