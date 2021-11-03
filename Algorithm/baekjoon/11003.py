import heapq

def find_min(arr, m):
    length = len(arr)
    if length < m+1:
        temp = []
        result = []
        for i in range(length):
            heapq.heappush(temp, arr[i])
            result.append(temp[0])
        return result
    q = []
    prev_q = []
    result = []
    for i in range(m):
        heapq.heappush(q, arr[i])
        result.append(q[0])
    heapq.heappush(prev_q, arr[0])
    for i in range(m, length):
        heapq.heappush(q, arr[i])
        while prev_q:
            if q[0] == prev_q[0]:
                heapq.heappop(q)
                heapq.heappop(prev_q)
            else:
                break
        heapq.heappush(prev_q, arr[i-m+1])
        result.append(q[0])
    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(*find_min(arr, m))