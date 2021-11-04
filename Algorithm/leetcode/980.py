class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dx, dy = (1,-1,0,0), (0,0,1,-1)
        m, n = len(grid), len(grid[0])
        count = 0
        target = 1
        goal = None
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    stack.append((i,j,[(i,j)]))
                elif grid[i][j]!=-1:
                    if grid[i][j]==2:
                        goal = (i,j)
                    target += 1
        while stack:
            temp = stack.pop()
            y, x, visited = temp[0], temp[1], temp[2]
            if y==goal[0] and x==goal[1]:
                if len(visited)==target:
                    count += 1
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<n and 0<=ny<m and (ny,nx) not in visited:
                    if grid[ny][nx]!=-1:
                        copied = visited[:]
                        copied.append((ny,nx))
                        stack.append((ny,nx,copied))
        return count

