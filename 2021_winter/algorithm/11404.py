def solve(n, d):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if d[i][j]>d[i][k]+d[k][j]:
                    d[i][j] = d[i][k]+d[k][j]

def main():
    n = int(input())
    m = int(input())
    d = [[100000 for i in range(n+1)] for j in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        d[a][b] = c
    print(d)
    solve(n, d)
    print(d)

if __name__=="__main__": main()

