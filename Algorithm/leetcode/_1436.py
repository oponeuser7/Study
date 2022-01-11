import heapq

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dx = (-1,0,1)
        rows, cols = len(grid), len(grid[0])
        q1, q2 = [], []
        q1.append((grid[0][0],0,0))
        q2.append(grid[0][cols-1],0,cols-1)
        while True:
            temp1 = heapq.heappop(q1)
            temp2 = heapq.heappop(q2)
            if temp1[1]==temp2[1] and temp1[2]==temp2[2]:
                temp2 = heapq.heappop(q2)
            c1, y1, x1  = temp1[0], temp1[1], temp1[2]
            c2, y2, x2 = temp2[0], temp2[1], temp2[2]
            if y1==rows-1 and y2==rows-1: 
                return c1+c2
            for i in range(3):
                if 0<=x1+dx[i]<cols:
                    heapq.heappush(q1, c1+grid[y1+1][x1+dx[i]], y1, x1+dx[i])
                if 0<=x2+dx[i]<cols:
                    heapq.heappush(q2, c2+grid[y2+1][x2+dx[i]], y2, x2+dx[i])
        return 0
