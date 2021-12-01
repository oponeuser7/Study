def city(a, b): #공통 지역 찾기 함수
    #둘 중 한 노드라도 트리에 속하지 않는다면
    if a not in parents or b not in parents:
        return 0 #0 리턴
    while not a==b: #a와 b가 같아질 때 까지(깊이는 무조건 같다)
        a = parents[a] #각자 부모 노드로
        b = parents[b] #이동
    return a #공통 조상 리턴

parents = {}
n = int(input())
a, b = input().split()
cities = input().split()
for i in range(1, n):
    parents[cities[i]] = cities[0] #국가에 도시 저장
for i in range(n-1):
    parts = input().split()
    for j in range(1, len(parts)):
        parents[parts[j]] = parts[0] #도시마다 구 저장
print(city(a,b))

