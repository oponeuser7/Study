import heapq

def meteo(input_list): #소행성 함수
    heap = [] #heap 선언
    for i in input_list: #입력 리스트를 하나씩
        heapq.heappush(heap, (-i, i)) #heap에다가 push
    while len(heap) > 1: #heap의 원소가 1개 이하가 될 때 까지
        first = heapq.heappop(heap)[1] #첫번째 소행성 pop
        second = heapq.heappop(heap)[1] #두번째 소행성 pop
        result = first - second #두 소행성의 차
        if result > 0: #두 소행성 모두 사라지지 않았다면
            heapq.heappush(heap, (-result, result)) #남은 소행성을 heap에 push
    if len(heap) == 1: #마지막 2개 소행성의 무게가 달라 소행성이 하나 남았다면
        return heapq.heappop(heap)[1] #남은 소행성의 무게를 리턴
    else: #마지막 2개 소행성의 무게가 같아 모든 소행성이 사라졌다면
        return 0 #0을 리턴

input_list = list(map(int, input().split()))
print(meteo(input_list))

