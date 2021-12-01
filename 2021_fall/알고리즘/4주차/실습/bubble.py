def bubble_a(input_list, count): #오름차순 버블정렬 함수, count 파라미터는 목표 순번을 받는다
    bubble_count = 0 #순번 변수
    length = len(input_list) #입력 배열의 길이
    for i in range(length): #배열의 모든 문자를
        for j in range(length-i-1): #뒤의 문자와 비교하면서
            if input_list[j] > input_list[j+1]: #뒤의 문자보다 크다면
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j] #스왑
        bubble_count += 1 #순번 1회 증가
        if bubble_count == count: #목표 순번이 되었으면
            return input_list #리턴
    return input_list #정렬 완료된 배열 리턴
def bubble_d(input_list, count): #내림차순 버블정렬 함수
    bubble_count = 0
    length = len(input_list)
    for i in range(length):
        for j in range(length-i-1):
            if input_list[j] < input_list[j+1]: #뒤의 문자보다 작다면 스왑한다는 점이 오름차순과 다르다.
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
        bubble_count += 1
        if bubble_count == count:
            return input_list
    return input_list

n, m, o = input().split()
input_list = list(input().split())
result = []
if o == 'A': #'A'이면 오름차순, 'D'이면 내림차순 함수 사용
    result = bubble_a(input_list, int(m)) 
else:
    result = bubble_d(input_list, int(m)) 
print(*result)

