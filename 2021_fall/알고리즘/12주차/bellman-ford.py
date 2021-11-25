def bellman_ford(edges, v, src, dst, vertexes, costs):
    distance, prev, path = {}, {}, []
    for vertex in vertexes:
        distance[vertex] = float("inf")
    distance[src] = 0
    for _ in range(v-1):
        for edge in edges:
            if edge[1]!=src and distance[edge[1]]>distance[edge[0]]+edge[2]:
                distance[edge[1]] = distance[edge[0]]+edge[2]
                prev[edge[1]] = edge[0]
    for edge in edges:
        if distance[edge[1]]>distance[edge[0]]+edge[2]: return "Negative"
    temp = dst
    while temp in prev:
        path.insert(0, prev[temp]+" "+temp+" "+costs[(prev[temp],temp)]) 
        temp = prev[temp]
    return "\n".join(path)

def main():
    v, e = map(int, input().split())
    src, dst = input().split()
    edges, costs = {}, {}
    vertexes = input().split()
    for _ in range(e):
        frm, to, cost = input().split()
        edges.append((frm, to, int(cost)))
        costs[(frm, to)] = cost
    print(bellman_ford(edges, v, src, dst, vertexes, costs))

if __name__=="__main__": main()
