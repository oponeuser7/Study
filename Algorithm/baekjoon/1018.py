def check(x, y):
    white = 0
    black = 0
    for i in range(8):
        for j in range(8):
            if i%2==0:
                if j%2==0:
                    if arr[i+y][j+x] == 'B':
                        white += 1
                    else:
                        black += 1
                else:
                    if arr[i+y][j+x] == 'W':
                        white += 1
                    else:
                        black += 1
            else:
                if j%2==0:
                    if arr[i+y][j+x] == 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if arr[i+y][j+x] == 'B':
                        white += 1
                    else:
                        black += 1
    return min(white, black)

n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(n):
    temp = input()
    for j in range(m):
        arr[i].append(temp[j])
x = m - 8
y = n - 8
result = 2500
for i in range(y + 1):
    for j in range(x + 1):
        result = min(result, check(j, i))
print(result)
