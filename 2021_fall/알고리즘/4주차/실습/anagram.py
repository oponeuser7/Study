def is_anagram(word1, word2): #애너그램 함수
    return sorted(word1) == sorted(word2) #두 문자열을 정렬한 뒤 비교하여 부울 리턴

n = input().lower().split() #문자열 입력 받은뒤 소문자로 변환
print(is_anagram(n[0], n[1]))

