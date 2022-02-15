def solve(graph):
    check = [False for i in range(len(graph))]
    stack = [1]
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not check[nxt]:
                check[nxt] = True
                stack.append(nxt)
    check[1] = False
    ans = 0
    for temp in check:
        if temp: ans += 1
    print(ans)

def main():
    n = int(input())
    m = int(input())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        frm, to = map(int, input().split())
        graph[frm].append(to)
        graph[to].append(frm)
    solve(graph)

if __name__=="__main__":
    main()
