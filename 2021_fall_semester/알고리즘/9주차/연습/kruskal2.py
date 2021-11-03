parent = {}
rank = {}

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
    global parent, rank
    for v in vertices:
        parent[v] = v
        rank[v] = 0
    result = 0
    for edge in edges:
        cost, a, b = edge
        if find(a)!=find(b):
            union(a, b)
            result += cost
    return result

vertices = []
edges = []
n = int(input())
m = int(input())
for v in range(1, n+1):
    vertices.append(v)
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
print(kruskal(vertices, sorted(edges)))