import heapq

def mid(arr):
    left = []
    right = []
    heapq.heappush(left, (-arr[0], arr[0]))
    mid = left[0][1]
    print(mid)
    for i in range(1, len(arr)):
        if arr[i] > mid:
            if len(left) == len(right):
                heapq.heappush(right, arr[i])
                temp = heapq.heappop(right)
                heapq.heappush(left, (-temp, temp))
            else:
                heapq.heappush(right, arr[i])
        else:
            if len(left) == len(right)+1:
                heapq.heappush(left, (-arr[i], arr[i]))
                temp = heapq.heappop(left)[1]
                heapq.heappush(right, temp)
            else:
                heapq.heappush(left, (-arr[i], arr[i]))
        mid = left[0][1]
        print(mid)

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
mid(arr)