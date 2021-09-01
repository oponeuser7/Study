n = int(input())
result = 0
length = len(str(n))
start = n - (length * 9)
for i in range(start, n):
    if i > 0:
        temp = i
        sum = 0
        for j in range(len(str(i))):
            sum = sum + temp % 10
            temp = int(temp / 10)
        val = i + sum
        if val == n:
            result = i
            break
print(result)
