def find_anagram(input_list): #아나그램 탐색 함수
    result = [] #결과를 저장할 배열
    while(0 < len(input_list)): #배열의 모든 문자열에 대해서
        temp = [] #아나그램 그룹 선언
        temp.append(input_list[0]) #배열의 첫 번째 문자열을 그룹에 추가
        j = 0
        while(j < len(input_list)): #첫 번째 문자열과 배열의 다른 모든 문자열들을 비교
            if j != 0:
                if is_anagram(input_list[0], input_list[j]): #첫 번째 문자열와 아나그램이라면
                    temp.append(input_list[j]) #그룹에 추가
                    del input_list[j] #배열에서 삭제
                    j -= 1 #배열 크기가 줄어들었으니 1 감소
            j += 1
        del input_list[0] #첫 번째 문자열도 배열에서 삭제
        result.append(temp) #결과에 그룹을 추가, 여기까지 한 과정을 배열이 빌 때 까지 반복
    return result #결과 리턴
 
def is_anagram(s1, s2): #아나그램 판별 함수
    c1 = [0] * 26 #알파벳 개수 만큼
    c2 = [0] * 26 #배열 선언
    for i in range(len(s1)): #문자열의 모든 문자에 대해
        pos = ord(s1[i]) - ord('a') #아스키 코드 - 97 (0부터 25가 나오게 된다)에 해당하는 인덱스로
        c1[pos] += 1 #1을 증가시킨다
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    stillOk = True
    j = 0
    while j < 26 and stillOk: #두 문자열이 a부터 z까지 모든 문자에 대해서
        if c1[j] == c2[j]: #등장 횟수가 같다면 아나그램
            j += 1
        else: #문자 하나라도 등장 횟수가 다르다면
            stillOk = False #아나그램 아님
    return stillOk

input_list = list(input().lower().split()) #일괄 소문자로 변환
result = find_anagram(sorted(input_list))
for i in result:
    print(*i)

    