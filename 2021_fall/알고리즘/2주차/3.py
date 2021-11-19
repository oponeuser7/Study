n, k, i = map(int, input().split()) #n, k, i 입력 받음
arr = list(map(int, (input().split()))) #배열 입력 받음
arr.sort() #리스트를 오름차순 정렬
''' 
리스트의 인덱스는 0부터 시작이므로 앞에서 k번째는 arr[k-1]
리스트의 인덱스는 len(arr)-1 까지이므로 뒤에서 i번째는
len(arr-1)-i+1 == len(arr)-i
'''
print(arr[k-1]+arr[len(arr)-i]) #앞에서 k번째와 뒤에서 i번째 값의 합 출력

