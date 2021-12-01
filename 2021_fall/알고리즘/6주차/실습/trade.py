def trade(root, road, citymap): #dfs 함수
    visited = set() #방문 확인을 위한 셋
    stack =[root] #스택을 생성하고 루트 노드를 삽입
    while(stack): #스택이 빌 때 까지 
        temp = stack.pop() #스택의 최상단에서 노드 제거
        visited.add(temp) #해당 노드 방문 체크
        children = citymap[temp] #해당 노드의 자식(해당 도시와 연결된 도시)
        for i in children: #모든 자식에 대해서
            if i not in visited: #방문된 사실이 없고
                #현재 노드와 자식 노드의 사이가 target 도로가 아니라면
                if not (temp == road[0] and i == road[1]) and not (temp == road[1] and i == road[0]):
                    stack.append(i) #자식 노드를 스택에 추가
    if len(visited) != len(citymap): #target 도로가 무역 독점로였다면 모든 노드를 방문하지 못했을 것이므로
        return True #True 반환
    return False #아니면 False 반환

roads = [] #도로를 저장할 배열
citymap = {} #그래프(지도)를 형성할 맵
n, m = map(int, input().split())
for i in range(n):
    citymap[i] = [] #그래프를 빈 배열로 초기화
for i in range(m):
    road = list(map(int, input().split()))
    roads.append(road) #도로 저장
    citymap[road[0]].append(road[1]) #도시 간에는 양방 통행이기 때문에
    citymap[road[1]].append(road[0]) #쌍방 그래프로 구현한다
result = [] #결과를 저장할 배열
for road in roads: #모든 도로에 대해서
    if trade(0, road, citymap): #해당 도로가 무역 독점로라면
        result.append(road) #결과 배열에 추가
for i in sorted(result): #오름차순 정렬하여
    print(*i) #출력

