def room(arr):
    i = 0
    count = 1
    while(True):
        check = True
        end_time = arr[i][1]
        for j in range(i+1, len(arr)):
            if arr[j][0] >= end_time:
                print(arr[j][0],arr[j][1])
                i = j
                count += 1
                check = False
                break
        if check:
            break
    return count

n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    temp.append(temp[1] - temp[0])
    arr.append(temp)
print(sorted(arr))
print(room(sorted(arr)))