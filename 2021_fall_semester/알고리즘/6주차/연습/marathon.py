import collections

def marathon(a, b):
    result = collections.Counter(a) - collections.Counter(b)
    return list(result)

a = input().split()
b = input().split()
print(*marathon(a, b))
