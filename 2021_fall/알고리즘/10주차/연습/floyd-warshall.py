def floyd_warshall(edges, v, src, dst):
    for i in range(1, v+1):
        for j in range(1, v+1):
            for k in range(1, v+1):
                if edges[j][k]>edges[j][i]+edges[i][k]:
                    edges[j][k] = edges[j][i]+edges[i][k]
    return edges[src][dst]

def main():
    v, e = map(int, input().split())
    src, dst = map(int, input().split())
    edges = [[float("inf") if i!=j else 0 for i in range(v+1)] for j in range(v+1)]
    for _ in range(e):
        frm, to, cost = map(int, input().split())
        edges[frm][to] = cost
    print(floyd_warshall(edges, v, src, dst))

if __name__=="__main__": main()
