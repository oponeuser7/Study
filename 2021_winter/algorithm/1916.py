def main():
    n = int(input())
    m = int(input())
    g = [[] for i in range(n+1)]
    for i in range(m):
        frm, t0, cost = map(int, input().split())
        g[frm] = (to, cost)
    s, e = map(int, input().split())
    print(solve(g, s, e))



