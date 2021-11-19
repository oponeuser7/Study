import heapq

def factory(stock, dates, supplies, k):
    import_count = 0
    stock_heap = []
    index = 0
    while stock < k:
        for i in range(index, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(stock_heap, (-supplies[i], supplies[i]))
                index = i + 1
            else:
                break
        max_amout = heapq.heappop(stock_heap)[1]
        stock += max_amout
        import_count += 1
    return import_count

stock, k, dates_length, supplies_length = map(int, input().split())
dates = list(map(int, input().split()))
supplies = list(map(int, input().split()))
print(factory(stock, dates, supplies, k))