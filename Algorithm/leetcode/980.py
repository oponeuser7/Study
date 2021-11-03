class Solution:
    def uniquePathsIII(self, grid):
        stack = []
        visited = set()
        h = len(grid)
        w = len(grid[0])
        count = 0
        target = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]==0 or grid[i][j]==2:
                    target += 1
                elif grid[i][j]==1:
                    stack.append((j,i,0))
        dx = (1,-1,0,0)
        dy = (0,0,1,-1)
        while stack:
            temp = stack.pop()
            x, y, v = temp[0], temp[1], temp[2]
            if grid[y][x]==2:
                if v==target:
                    count += 1
                    visited = set()
                continue
            visited.add((x,y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<w and 0<=ny<h:
                    if grid[ny][nx]!=-1 and (nx,ny) not in visited:
                        stack.append((nx,ny,v+1))
        return count

