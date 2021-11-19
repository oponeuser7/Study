merge_count = 0 #현재 순번을 저장할 전역변수
def merge_sort(array, count, order): #머지소트 함수, count는 목표 순번, order는 오름차순 or 내림차순 파라미터이다
    def inside_sort(arr): #재귀함수인데 파라미터가 다소 많아서 2중 함수로 구현
        if len(arr) < 2: #크기가 1까지 조각나면
            return arr #리턴
        global merge_count #전역 변수를 사용하도록 재정의
        middle = len(arr) // 2 #홀수 크기를 나눌 시 left가 작고 right가 커야하므로 // 연산자 사용
        left = inside_sort(arr[:middle]) #왼쪽과
        right = inside_sort(arr[middle:]) #오른쪽으로 나누어서 재귀
        merged = [] #정렬되며 합쳐질 배열
        l = 0 #left 카운트
        r = 0 #right 카운트
        if merge_count == count: #순번이 목표 순번에 도달하게 되면
           return left + right #정렬을 그만두고 쪼갰던 left와 right를 그대로 합쳐서 다시 올라간다
        if order == 'A': #오름차순의 경우
            while l < len(left) and r < len(right):
                if left[l] < right[r]: #첫 번째 요소가 작은 쪽을 merged 배열에 append하는 식으로 진행
                    merged.append(left[l]) #left와 right는 항상 정렬되어있으므로 이런 식의 정렬이 가능하다
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
        else:
            while l < len(left) and r < len(right): #내림차순의 경우
                if left[l] > right[r]: #첫 번째 요소가 큰 쪽을 merged 배열에 append하는 식으로 진행
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
        merged += left[l:] #위 과정을 수행하면 left와 right중에서 원소가 하나 남게 된다
        merged += right[r:] #이를 마지막으로 merged 배열에 append
        merge_count += 1 #순번 카운트 증가
        return merged #합병된 배열 리턴
    return inside_sort(array) #내부 함수 리턴

n, m, o = input().split()
input_list = list(input().split())
result = merge_sort(input_list, int(m), o)
print(*result)

