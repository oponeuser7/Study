from collections import deque

def solution(rows, columns, max_virus, queries):
    ans = [[0 for i in range(columns)] for j in range(rows)]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    def bfs(query):
        visited = set()
        queue = deque([(query[0]-1, query[1]-1)])
        while queue:
            temp = queue.popleft()
            y, x = temp[0], temp[1]
            if temp not in visited: visited.add(temp)
            if ans[y][x]==max_virus:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=ny<rows and 0<=nx<columns and (ny, nx) not in visited:
                        queue.append((ny, nx))
                        visited.add((ny, nx))
            else:
                ans[y][x] += 1
    for query in queries:
        bfs(query)
    return ans
