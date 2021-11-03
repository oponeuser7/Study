import collections

def marathon(a, b): #집합 비교 함수
    result = collections.Counter(a) - collections.Counter(b) #두 집합의 차집합을
    return list(result) #리턴

a = input().split()
b = input().split()
print(*marathon(a, b))

