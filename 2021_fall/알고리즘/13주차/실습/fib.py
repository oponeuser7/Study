def fib(n): #피보나치 함수
    dp = [0]*100 #입력 범위가 100이므로 크기 100의 dp 리스트 선언
    dp[0], dp[1] = 0, 1 #피보나치 0과 1의 결과를 초기화
    for i in range(2, 100): #i가 2부터 100까지
       dp[i] = dp[i-1]+dp[i-2] #피보나치 결과를 저장
    return dp[n] #피보나치 n을 리턴

def main():
    n = int(input())
    print(fib(n))

if __name__=="__main__": main()
