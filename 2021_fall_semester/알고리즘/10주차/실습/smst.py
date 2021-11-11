def union(a, b): #union 함수
    root1 = find(a) #집합 a의 루트
    root2 = find(b) #집합 b의 루트
    if rank[root1]<rank[root2]: #b의 높이가 a보다 깊다면
        parent[root1] = root2 #a를 b에다가 붙인다
    else: #그 외의 경우
        parent[root2] = root1 #b를 a에다가 붙인다
        if rank[root1]==rank[root2]: #만약 둘의 높이가 같다면
            rank[root1] += 1 #높이를 1 증가

def find(v): #find 함수
    if parent[v]!=v: #부모가 자신이 아니면 아직 루트노드가 아니다
        parent[v] = find(parent[v]) #부모 노드로 이동
    return parent[v] #루트 노드 리턴

def kruskal(vertices, edges): #kruskal 함수
    for v in vertices: #모든 정점 v에 대해서
        parent[v] = v #루트가 v
        rank[v] = 0 #높이가 0인 집합으로 초기화
    result = 0 #결과(최소비용)를 저장할 변수
    for edge in edges: #모든 간선에 대하여
        cost, a, b = edge
        if find(a)!=find(b): #두 정점이 같은 집합에 속하지 않으면
            union(a, b) #한 집합으로 union
            result += cost #간선의 비용을 추가
    return result #최소 비용 리턴

parent = {}
rank = {}
n, m = map(int, input().split())
vertices = input().split()
edges = []
for i in range(m):
    a, b, c = input().split()
    edges.append([int(c),a,b])
edges.sort() # 비용 오름차순으로 간선을 정렬한다
result = kruskal(vertices, edges) #최소 비용 저장
ans = float("inf")
for i in range(len(edges)): #모든 간선에 대하여
    temp = edges.copy()
    del temp[i] #해당 간선이 없을 때의
    x = kruskal(vertices, temp) #최소 비용을 계산
    if result < x < ans: #원래의 최소 비용보단 큰 값들 중에서
        ans = x #최소를 계산하면 바로 두 번째로 작은 비용이다
print(ans) #결과 출력

