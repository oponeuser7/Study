def power(bases, stations):
    needs = [] #각 기지마다 필요한 최소의 전력을 저장할 배열
    for i in bases: #모든 기지에 대해서
        ranges = [] #전력소와의 거리를 저장할 배열
        for j in stations: #모든 전력소에 대해서
            ranges.append(abs(j-i)) #기지와 전력소 사이의 거리를 저장
        needs.append(min(ranges)) #거리의 최소값을 얻는다
    return max(needs) #기지마다 필요한 최소 전력 중에서 최대값을 리턴한다.

bases = list(map(int, input().split()))
stations = list(map(int, input().split()))
print(power(bases, stations))

