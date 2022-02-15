def solve(e, v):
    dfs, bfs = [], []
    
    stack = [v]
    check = [False]*len(e)
    check[v] = True
    def df(cur):
        dfs.append(cur)
        for nxt in e[cur]:
            if not check[nxt]:
                check[nxt] = True
                df(nxt)
    df(v)

    queue = [v]
    check = [False]*len(e)
    check[v] = True
    while queue:
        cur = queue.pop(0)
        bfs.append(cur)
        for nxt in e[cur]:
            if not check[nxt]:
                check[nxt] = True
                queue.append(nxt)

    print(" ".join(map(str, dfs)))
    print(" ".join(map(str, bfs)))

def main():
    n, m, v = map(int, input().split())
    e = [[] for i in range(n+1)]
    for i in range(m):
        frm, to = map(int, input().split())
        e[frm].append(to)
        e[to].append(frm)
    for i in range(n):
        e[i].sort()
    solve(e, v)

if __name__=="__main__": main()
