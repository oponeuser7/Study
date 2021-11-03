def piramid(n):
    if n == 1:
        return 1
    result = 1
    sum = 1
    for i in range(2, n+1):
        sum *= 2
        result += sum
    return result

n = int(input())
print(piramid(n))