def lcs(a, b): #lcs 함수
    #M by N 행렬 0으로 초기화
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]: #두 수열이 같은 원소로 끝난다면
                dp[i][j] = dp[i-1][j-1]+1 #이전까지의 lcs 결과 + 1
            else: #두 수열이 다른 원소로 끝난다면
                #두 수열 각각 원소를 하나씩 제거한 lcs 결과중 큰 것을 선택
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[len(a)][len(b)] #결과 리턴

def main():
    a = input()
    b = input()
    print(lcs(a,b))

if __name__=="__main__": main()

