from collections import deque

def bfs(m, n, arr):
    queue = deque()
    count = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue.append([j, i, 0])
    while(queue):
        temp = queue.popleft()
        x = temp[0]
        y = temp[1]
        count = max(count, temp[2])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < m and 0<= ny < n and arr[ny][nx] == 0):
                arr[ny][nx] = 1
                queue.append([nx, ny, temp[2]+1])
    for i in arr:
        if 0 in i:
            return -1
    return count

arr = []
m, n = map(int, input().split())
for i in range(n):
    arr.append(list(map(int, input().split())))
print(bfs(m, n, arr))
