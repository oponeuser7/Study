parent = {}
rank = {}

def make_set(v):
    global parent, rank
    parent[v] = v
    rank[v] = 0

def find(v):
    global parent, rank
    if parent[v]!=v:
        parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    global parent, rank
    root1 = find(a)
    root2 = find(b)
    if rank[root1]<rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        if rank[root1]==rank[root2]:
            rank[root1] += 1

def kruskal(vertices, edges):
    for i in vertices:
        make_set(i)
    result = 0
    for edge in edges:
        c, a, b = edge
        if find(a)!=find(b):
            union(a,b)
            result += c
    return result

n, m = map(int, input().split())
vertices = input().split()
edges = []
for i in range(m):
    a, b, c = input().split()
    edges.append([int(c),a,b])
edges.sort()
result = kruskal(vertices, edges)
ans = 100001
for i in range(len(edges)):
    temp = edges.copy()
    del temp[i]
    x = kruskal(vertices, temp)
    if result < x < ans:
        ans = x
print(ans)

