from collections import deque

def solve(n, k):
    visited = [False]*100001
    path = [n]
    def dfs(k, path):
        n = path[-1]
        if n==k: 
            print(len(path)-1) 
            return path
            if k-(2*n) and 0<=n*2<=100000 and not visited[n*2]:
                temp = path[:]
                temp.append(n*2)
                dfs(k, temp)
            elif 0<=n+1<=100000 and not visited[n+1]:
                temp = path[:]
                temp.append(n+1)
                dfs(k, temp)
        else:
            if 0<=n-1<=100000 and not visited[n-1]:
                temp = path[:]
                temp.append(n-1)
                dfs(k, temp)
    return dfs(k, path)

def main():
    n, k = map(int, input().split())
    print(*solve(n, k))

if __name__=="__main__": main()
