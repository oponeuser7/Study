def napsack(cap, n, w, v): #배낭 함수
    V = [[0]*(cap+1) for _ in range(n+1)] #아이템수x최대용량의 행렬을 생성
    for i in range(1, n+1): #0행과 0열은 0으로 초기화 해놓았으므로
        for W in range(1, cap+1): #1행1열부터 n행 cap열까지 반복
            if w[i]<=W: #현재 무게제한에서 해당 아이템을 배낭에 넣을 수 있다면
                #해당 아이템을 넣고 남은 용량으로 채울 수 있는 양의 합과
                #이전 아이템으로 채울 수 있는 양 중 큰 것을 선택
                V[i][W] = max(v[i]+V[i-1][W-w[i]], V[i-1][W])
            else: #배낭에 넣을 수 없다면 이전 아이템으로 채울 수 있는 양을 선택
                V[i][W] = V[i-1][W]
    return V[-1][-1] #행렬의 맨 오른쪽 아래 값이 답

def main():
    cap = int(input())
    n = int(input())
    w = list(map(int, input().split())) 
    v = list(map(int, input().split())) 
    w.insert(0,0) #인덱스가 헷갈리기 때문에
    v.insert(0,0) #입력을 zero-index로 맞춤
    print(napsack(cap, n, w, v))

if __name__=="__main__": main()

