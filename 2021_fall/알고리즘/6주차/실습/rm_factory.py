import heapq

def factory(stock, dates, supplies, k): #라면공장 함수
    import_count = 0 #수입 횟수 선언
    stock_heap = [] #heap 선언
    i = 0 #dates에 사용할 인덱스 변수
    for cur_day in range(k): #0일부터 k일까지 반복
        stock -= 1 #하루가 지났으므로 stock 1 감소
        if cur_day == dates[i] - 1: #오늘이 수입 가능한 날짜라면
            heapq.heappush(stock_heap, (-supplies[i], supplies[i])) #heap에다가 우선 push
            if i < len(dates) - 1: #heap에 push 했으므로
                i += 1 #다음 수입 가능한 날짜를 탐색
        if stock == 0: #재고가 다 떨어졌다면
            max_amout = heapq.heappop(stock_heap)[1] #heap에서 원소를 하나 pop
            stock += max_amout #결과적으로 지금까지 수입 가능했던 시점 중 공급량이 가장 큰 건을 stock에 더하게 된다.
            #가능한 한 수입 횟수를 줄여야 하기 때문이다.
            import_count += 1 #수입 횟수 1 증가
    return import_count #총 수입 횟수 리턴

stock, k, dates_length, supplies_length = map(int, input().split())
dates = list(map(int, input().split()))
supplies = list(map(int, input().split()))
print(factory(stock, dates, supplies, k))

