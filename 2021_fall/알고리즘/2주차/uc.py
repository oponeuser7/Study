def uc(n, m): # 유클리드 호제법 함수
    x = n % m # n을 m으로 나눈다.
    if x == 0: # 나머지가 0이면
        return m # m을 리턴
    return uc(m, x) # 다시 m과 나머지로 재귀 호출

n, m = map(int, input().split())
print(uc(n, m))

