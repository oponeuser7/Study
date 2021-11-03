def danzi(arr, x, y, n):
    arr[y][x] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < n and 0<= ny < n and arr[ny][nx]):
            result += danzi(arr, nx, ny, n)
    return 1 + result

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            result.append(danzi(arr, j, i, n))
result.sort()
print(len(result))
for i in result:
    print(i)
