import heapq

def dijkstra(edges, v, src, dst, vertexes):
    distance = {}
    for vertex in vertexes:
        distance[vertex] = float("inf")
    distance[src] = 0
    path, prev = [dst], {}
    queue = [(0, src)]
    found = set()
    while queue:
        v = heapq.heappop(queue)
        found.add(v[1])
        for node in edges[v[1]]:
            if node[0] in found: continue
            if distance[node[0]]>distance[v[1]]+node[1]:
                distance[node[0]] = distance[v[1]]+node[1]
                heapq.heappush(queue, (distance[node[0]], node[0]))
                prev[node[0]] = v[1]
    temp = dst
    while temp in prev:
        path.insert(0, prev[temp]) 
        temp = prev[temp]
    print("".join(map(str, path)))
    return distance[dst]

def main():
    v, e = map(int, input().split())
    src, dst = input().split()
    edges = {}
    vertexes = input().split()
    for edge in vertexes:
        edges[edge] = []
    for _ in range(e):
        frm, to, cost = input().split()
        edges[frm].append((to, int(cost)))
        edges[to].append((frm, int(cost)))
    print(dijkstra(edges, v, src, dst, vertexes))

if __name__=="__main__": main()