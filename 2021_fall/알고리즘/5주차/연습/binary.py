def bin(n, right, times):
    left = 0
    result = right
    while left <= right:
        mid = (right+left)//2
        if check(n, mid, times):
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result

def check(n, mid, times):
    sum = 0
    for i in times:
        sum += mid // i
    return n <= sum

n = int(input())
times = list(map(int, input().split()))
print(bin(n, n*max(times), times))