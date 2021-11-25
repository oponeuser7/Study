def floyd_warshall(edges, v, d, vertexes):
    for i in vertexes:
        for j in vertexes:
            for k in vertexes:
                if edges[(j,k)]>edges[(j,i)]+edges[(i,k)]:
                    edges[(j,k)] = edges[(j,i)]+edges[(i,k)]
    ans = {}
    for vertex in vertexes:
        ans[vertex] = 0
    for edge in edges:
        if edges[edge]<=d: ans[edge[0]] += 1
    max_key = max(ans, key=ans.get)
    return max_key+" "+str(ans[max_key])

def main():
    v, e = map(int, input().split())
    d = int(input())
    vertexes = input().split()
    edges = {}
    for i in vertexes:
        for j in vertexes:
            edges[(i,j)] = float("inf") if i!=j else 0
    for _ in range(e):
        frm, to, cost = input().split()
        edges[(frm,to)] = int(cost)
        edges[(to,frm)] = int(cost)
    print(floyd_warshall(edges, v, d, vertexes))

if __name__=="__main__": main()