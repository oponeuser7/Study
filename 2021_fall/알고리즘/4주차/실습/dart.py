import re

def dart(s): #다트 함수
    p = re.compile("(\d+)([a-zA-Z])(\*|\#)?") #정규표현식 선언
    p = p.findall(s) #정규표현식으로 파싱
    result = [1 for _ in range(3)] #곱셈을 해야하므로 배열 값 1로 초기화
    for i in range(3): #총 3회 반복
        temp = int(p[i][0]) #파싱된 배열의 첫번째 인덱스가 점수 부분이다
        if p[i][1] == 'D': #두번째 인덱스는 SDT 영역이다. 더블이면
            temp *= temp #점수 ^ 2
        elif p[i][1] == 'T': #트리플이면
            temp *= temp * temp #점수 ^ 3
        if p[i][2] == '*': #세번째 인덱스는 옵션 영역이다. 스타상이면
            temp *= 2 #점수 * 2
            if i < 2: #마지막 기회가 아니라면
                result[i+1] *= 2 #바로 뒤에 얻는 점수도 곱하기 2
        elif p[i][2] == '#': #아차상이면
            temp *= -1 #점수 * -1
        result[i] *= temp #결과 배열에 저장
    return result[0] + result[1] + result[2] #3번의 점수 결과를 모두 합하여 리턴
s = input()
print(dart(s))

