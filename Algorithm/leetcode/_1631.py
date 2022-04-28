class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def bfs(k):
            dy, dx = (0,0,1,-1), (1,-1,0,0)
            row = len(heights)
            col = len(heights[0])
            q = deque()
            visited = [[0 for i in range(col)] for j in range(row)]
            q.append((y, x))
            while q:
                temp = q.popleft()
                y, x = temp[0], temp[1]
                if y==row-1 and x==col-1: return True
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if 0<=ny<row and 0<=nx<col and not visited[ny][nx]:
                        if abs(heights[y][x]-heights[ny][nx])<=k:
                            q.append(ny, nx)
                            visited[ny][nx] = 1
            return False

       left, right = 0, max([max(height[i]) for i in range(col)])
       ans = right
       while left<right:
           mid = (left+right)//2
           if bfs(mid):
               ans = mid
               left = mid+1
            else:
                right = mid-1
        return ans
