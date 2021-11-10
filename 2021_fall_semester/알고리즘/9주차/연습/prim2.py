import heapq

def prim(edges, n):
    queue = []
    heapq.heappush(queue, [0,0,1])
    visited = [False for _ in range(n+1)]
    result = 0
    while queue:
        #temp[0] == 가중치, temp[1] == 출발노드, temp[2] == 도착노드
        temp = heapq.heappop(queue)
        if visited[temp[2]]:
            continue
        visited[temp[2]] = True
        result += temp[0]
        for edge in edges[temp[2]]:
            if not visited[edge[0]]:
                heapq.heappush(queue, [edge[1],temp[2],edge[0]])
    return result

n, m = map(int, input().split())
edges = [[]for _ in range(n+1)]
check = set(i for i in range(1, n+1))
for i in range(m):
    a, b, c = map(int, input().split())
    edges[a].append([b,c])
    edges[b].append([a,c])
    check.remove(a)
    check.remove(b)
print(prim(edges, n))