n, m = map(int, input().split())
arr = list(map(int, input().split()))
max = 0
for i in range(n):
    for j in range(n):
        if i==j: continue
        for k in range(n):
            if k==i or k==j: continue
            sum = arr[i] + arr[j] + arr[k]
            if sum <= m and max < sum:
                max = sum
print(max)