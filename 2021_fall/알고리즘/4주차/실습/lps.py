def lps(s): #lps 함수
    table = [[False for i in range(len(s))] for j in range(len(s))] #False로 len(s)^2 크기의 배열 생성
    result = "" #리턴할 문자열
    for i in range(len(s)): #len(s) 만큼 반복
        for j in range(len(s)-i): #len(s)에서 1씩 줄어들면서 반복
            if i < 2: #2보다 작은 길이이면 한번의 비교로 알 수 있다
                if s[j] == s[i+j]: #문자열의 양 끝이 같은 문자이면
                    table[j][j+i] = True #팰린드롬이 맞다
                    result = s[j:i+j+1] #결과에 해당 문자열 저장
                else: #문자열의 양 끝이 다르다면
                    table[j][i+j] = False #False 저장
            else: #길이가 3 이상이라면 이전 결과로부터 도움을 받아야 한다(DP 같은 개념)
                if s[j] == s[i+j] and table[j+1][i+j-1]: #해당 문자열의 양 끝을 자른 문자열의 팰린드롬 여부 확인
                    table[j][i+j] = True #팰린드롬이 맞다면
                    result = s[j:i+j+1] #결과에 해당 문자열 저장
                else: #다르다면
                    table[j][i+j] = False #False 저장
    return result #길이가 커지는 순서로 for문이 돌기 때문에 최대값 비교 없이도 lps가 들어있다.
print(lps(input()))

