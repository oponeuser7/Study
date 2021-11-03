def power(bases, stations):
    needs = []
    for i in bases:
        ranges = []
        for j in stations:
            ranges.append(abs(j-i))
        needs.append(min(ranges))
    return max(needs)

bases = list(map(int, input().split()))
stations = list(map(int, input().split()))
print(power(bases, stations))