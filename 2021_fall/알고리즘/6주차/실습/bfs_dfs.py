from collections import deque

def bfs(root, graph): #bfs 함수 선언
    visited = set() #방문 확인 셋
    result = "" #방문순서를 저장할 문자열
    queue = deque() #큐 선언
    queue.append(root) #큐에 루트 노드 삽입
    while queue: #큐가 빌 때 까지
        temp = queue.popleft() #큐에서 노드를 한개 제거
        visited.add(temp) #해당 노드에 방문 체크
        result += temp+" " #해당 노드를 방문 순서에 추가
        children = graph[temp] #해당 노드의 자식들
        for i in children: #모든 자식들에 대해서
            if i not in visited: #방문된 사실이 없으면
                queue.append(i) #큐에 삽입
    return result #결과 리턴
    
def dfs(root, graph): #dfs 함수 선언
    visited = set() #방문 확인 셋
    result = "" #방문 순서를 저장할 문자열
    stack = [] #스택 선언
    stack.append(root) #스택에 루트 노드 삽입
    while(stack): #스택이 빌 때 까지
        temp = stack.pop() #스택에서 노드를 한개 제거
        visited.add(temp) #해당 노드에 방문 체크
        result += temp+" " #해당 노드를 방문 순서에 추가
        children = graph[temp] #해당 노드의 자식들
        for i in children: #모든 자식들에 대해서
            if i not in visited: #방문된 사실이 없으면
                stack.append(i) #큐에 삽입
    return result #결과 리턴

root = input()
graph = { #입력 그래프
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
print(bfs(root, graph))
print(dfs(root, graph))

