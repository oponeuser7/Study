import heapq

def prim(edges, n, costs, start_node): #prim 함수
    visited = set() #방문 체크 셋
    queue = [] #힙
    #힙에 (시작 노드의 건설 비용, 0(가상의 노드), 시작 노드)를 푸쉬한다
    heapq.heappush(queue, (costs[start_node-1], 0, start_node))
    result = 0 #결과를 저장할 변수
    while queue: #큐가 빌 때 까지
        temp = heapq.heappop(queue) #힙에서 원소를 팝
        if temp[2] in visited: #이미 방문한 노드라면
            continue #continue
        visited.add(temp[2]) #노드를 방문 셋에 추가
        result += temp[0] #비용을 결과에 덧셈
        frm = temp[2] #출발 노드
        #건설이 가능하므로 모든 노드는 모든 노드와 이어진 것이나 마찬가지이다
        for i in range(1, n+1): #모든 노드에 대해서
            if i not in visited: #방문한 사실이 없으면
                cost, to = costs[i-1], i #건설 비용을 비용으로 책정
                if (frm, to) in edges: #만약 도착 노드로의 간선이 존재한다면
                    #건설 비용과 유선 연결 비용 중 작은 것을 비용으로 선택
                    cost = min(edges[(frm, to)], cost)
                heapq.heappush(queue, (cost, frm, to)) #힙에 푸쉬
    return result #결과 리턴

n, m = map(int, input().split())
costs = list(map(int, input().split()))
min_val = float("inf")
start_node = 1 #탐색을 시작할 노드
for cost in enumerate(costs):#모든 건설 비용에 대하여
    if min_val > cost[1]:
        min_val = cost[1] #비용이 가장 작은 노드를
        start_node = cost[0]+1 #시작 노드로 선택
edges = {}
for i in range(m):
    a, b, c = map(int, input().split())
    edges[(a, b)] = c #간선은 (출발지,목적지) 튜플을 키로 하는
    edges[(b, a)] = c #딕셔너리로 선언
print(prim(edges, n, costs, start_node))

