n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
#선택정렬 사용
for i in range(n):
    min_num = 1001
    index = 0
    for j in range(i, n):
        if min_num > arr[j]:
            min_num = arr[j]
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp
for i in arr:
    print(i)

    
