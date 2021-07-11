n = int(input())
m = input()
arr = m.split(" ")
counts = []
arr = list(map(int, arr))
for i in range(n):
    list = []
    count = 0
    for j in range(n):
        if j == i:
            continue
        d = i - j
        h = arr[j]
        list.append((h,d))
    list2 = sorted(list, key = lambda x : (-x[0], x[1]))
    while(len(list2)!=0):
        head = list2[0][1]
        del list2[0]
        count += 1
        for i, x in enumerate(list2):
            if x[1] > head:
                del list2[i]
    counts.append(count)
counts.sort(reverse=True)
for k in counts:
    print(k)
print(counts[0])