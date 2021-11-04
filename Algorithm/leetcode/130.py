from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        if n>2 and m>2:
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            os = set()
            queue = deque()
            for i in range(n):
                for j in range(m):
                    if board[i][j]=='O':
                        if (i==0 or i== n-1 or j==0 or j==m-1):
                            queue.append((i,j))
                        else:
                            os.add((i,j))
                            board[i][j] = 'X'
            while queue:
                temp = queue.popleft()
                x = temp[1]
                y = temp[0]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<m and 0<=ny<n and board[ny][nx]=='X':
                        if (ny,nx) in os:
                            queue.append((ny,nx))
                            os.remove((ny,nx))
                            board[ny][nx] = 'O'