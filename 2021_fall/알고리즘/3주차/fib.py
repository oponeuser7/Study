def fib(n): # 피보나치 함수
    if n < 2: # 0 또는 1 인 경우
        return n # 그대로 리턴
    return fib(n-1) + fib(n-2) # 재귀 호출

n = int(input())
print(fib(n))

