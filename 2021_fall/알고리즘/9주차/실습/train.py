def train(root, graph): #dfs 함수
    stack = [root] #스택 선언하고 루트노드 push
    visited = [root] #방문 배열 선언하고 루트노드 추가
    while stack: #스택이 빌 때 까지
        temp = stack.pop() #스택 pop
        children = graph[temp] if temp in graph else [] #pop한 노드의 자식들
        for node in children: #모든 자식 노드들에 대해서
            if node not in visited: #방문한 사실이 없으면
                stack.append(node) #스택에 push
                visited.append(node) #방문 배열에 추가
    #방문 배열의 크기와 그래프의 크기가 같다면 모든 노드를 방문한 것이다.
    return len(visited)==len(graph)

graph = {}
n, m = map(int, input().split())
names = input().split()
for name in names:
    graph[name] = [] #역 이름으로 그래프 초기화
root = names[0] #첫 번째 역이 루트
for i in range(m):
    a, b = input().split()
    graph[a].append(b) #양방향
    graph[b].append(a) #연결
print(train(root, graph))

