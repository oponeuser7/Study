def number(n, m):
    s = set(n)
    for i in m:
        if i in s:
            print(1)
        else:
            print(0)

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
number(arr_n, arr_m)
