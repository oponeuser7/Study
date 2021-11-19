import heapq

def factory(stock, dates, supplies, k):
    import_count = 0
    stock_heap = []
    i = 0
    for cur_day in range(k):
        stock -= 1
        if cur_day == dates[i] - 1:
            heapq.heappush(stock_heap, (-supplies[i], supplies[i]))
            if i < len(dates) - 1:
                i += 1
        if stock == 0:
            max_amout = heapq.heappop(stock_heap)[1]
            stock += max_amout
            import_count += 1
    return import_count

stock, k, dates_length, supplies_length = map(int, input().split())
dates = list(map(int, input().split()))
supplies = list(map(int, input().split()))
print(factory(stock, dates, supplies, k))