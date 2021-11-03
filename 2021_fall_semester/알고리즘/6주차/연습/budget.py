def cut(base, m, right, budgets):
    left = 0
    result = right
    while left <= right:
        mid = (left+right) // 2
        if check(m, base + mid, budgets):
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return base + result

def check(m, mid, budgets):
    sum = 0
    for i in budgets:
        if mid >= i:
            sum += i
        else:
            sum += mid
    return m >= sum

budgets = list(map(int, input().split()))
m = int(input())
right = max(budgets) - min(budgets)
print(cut(min(budgets), m, right, budgets))
