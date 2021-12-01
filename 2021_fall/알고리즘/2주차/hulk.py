def hulk(n, m): # 계단오르기 함수
    if n < 2: # n이 2보다 작은 경우
        return 1 # 1을 리턴
    result = 0 
    for i in range(1, m+1): # 한번에 오를 수 있는 최대 계단 수 만큼 반복
        n -= 1 # 계단을 한번에 한칸 더 오르는 대신 n은 - 1
        if n == -1: # n이 음수가 되면 break
            break
        result += hulk(n, m) # 계단을 n개오르고 i개를 한번에 오르는 경우의 수
    return result # 모든 경우의 수의 합을 리턴

n, m = map(int, input().split())
print(hulk(n, m))

