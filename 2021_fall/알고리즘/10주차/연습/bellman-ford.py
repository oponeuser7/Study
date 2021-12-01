def bellman_ford(edges, v, src, dst, costs):
    distance = []
    distance = [float("inf")]*(v+1)
    distance[src] = 0
    prev = [0]*(v+1)
    path = [dst]
    for _ in range(v-1):
        for edge in edges:
            if distance[edge[1]]>distance[edge[0]]+edge[2]:
                distance[edge[1]] = distance[edge[0]]+edge[2]
                prev[edge[1]] = edge[0]
    temp = dst
    while prev[temp]:
        path.insert(0, prev[temp]) 
        temp = prev[temp]
    path = "->".join(map(str, path))
    return distance[dst]

def main():
    v, e = map(int, input().split())
    src, dst = map(int, input().split())
    edges = []*(v+1)
    costs = {}
    for _ in range(e):
        frm, to, cost = map(int, input().split())
        edges.append((frm, to, cost))
        costs[(frm, to)] = cost
    print(bellman_ford(edges, v, src, dst, costs))

if __name__=="__main__": main()
