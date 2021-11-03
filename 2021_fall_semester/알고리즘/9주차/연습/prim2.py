import heapq

def prim(edges, n):
    result = 0
    q = []
    visited = [False for _ in range(n+1)]
    heapq.heappush(q, (0,0,1))
    while q:
        temp = heapq.heappop(q)
        if visited[temp[2]]:
            continue
        visited[temp[2]] = True
        result += temp[0]
        for edge in edges[temp[2]]:
            if not visited[edge[0]]:
                heapq.heappush(q, (edge[1], temp[2], edge[0]))
    return result

n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))
print(prim(edges, n))