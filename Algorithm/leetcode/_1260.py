class Solution:
    #Title: Shift 2D Grid
    #Approach: queue 
    #Explanation: Unpack the grid and save it to a queue. Poping from rear and pushing
    #to front would do a cycle action. Put back data from the queue to grid and return
    # the grid.
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                q.append(grid[i][j])
        for i in range(k):
            q.appendleft(q.pop())
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = q.popleft()
        return grid
