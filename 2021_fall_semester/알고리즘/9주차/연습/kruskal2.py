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

n, m = map(int, input().split())
vertices = input().split()
edges = []
for i in range(m):
    a, b, c = input().split()
    edges.append((int(c), a, b))
print(kruskal(vertices, sorted(edges)))

