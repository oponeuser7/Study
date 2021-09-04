n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    arr[i].append(1)
for i in range(len(arr)):
    for j in range(len(arr)):
        if i is not j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                arr[i][2] += 1
result = ""
for i in arr:
    result += str(i[2]) + " "
print(result)
