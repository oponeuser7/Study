def city(a, b):
    if a not in parents or b not in parents:
        return 0
    while not a==b:
        a = parents[a]
        b = parents[b]
    return a

parents = {}
n = int(input())
a, b = input().split()
cities = input().split()
parents[cities[0]] = cities[0]
for i in range(1, n):
    parents[cities[i]] = cities[0]
for i in range(n-1):
    parts = input().split()
    for j in range(1, len(parts)):
        parents[parts[j]] = parts[0]
print(city(a,b))


