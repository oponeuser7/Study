from collections import deque

def solve(n, m, graph):
    dx, dy = (1,-1,0,0), (0,0,1,-1)
    queue = [(0,0,0)]
    visited = set()
    while queue:
        cur = check.popleft()
        x, y, count = cur[0], cur[1], cur[2]
        visited.add((x, y))
        if y==n-1 and x==m-1: return count
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n and (x, y) not in visited:
                queue.append(nx, ny, count+1)
    return count



