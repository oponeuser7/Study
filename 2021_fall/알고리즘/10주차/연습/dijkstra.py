import heapq

def dijkstra(edges, v, src, dst):
    distance = [float("inf")]*(v+1)
    distance[src] = 0
    queue = []
    path = [dst]
    prev = [0]*(v+1)
    found = [False]*(v+1)
    heapq.heappush(queue, (0, src))
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True #found shortest path for v[1] (node)
        for node in edges[v[1]]:
            if found[node[0]]: continue
            if distance[node[0]]>(distance[v[1]]+node[1]):
                distance[node[0]] = distance[v[1]]+node[1]
                heapq.heappush(queue, (distance[node[0]], node[0]))
                prev[node[0]] = v[1]
    temp = dst
    while prev[temp]:
        path.insert(0, prev[temp]) 
        temp = prev[temp]
    path = "->".join(map(str, path))
    return distance[dst]

def main():
    v, e = map(int, input().split())
    src, dst = map(int, input().split())
    edges = [[] for _ in range(v+1)]
    for _ in range(e):
        frm, to, cost = map(int, input().split())
        edges[frm].append((to, cost))
    print(dijkstra(edges, v, src, dst))

if __name__=="__main__": main()
