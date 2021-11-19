def cup(target, root, graph): #dfs 함수
    visited = set() #방문 확인을 위한 셋
    stack = [root] #스택을 선언하고 루트 노드 삽입
    while stack: #스택이 빌 때 까지
        temp = stack.pop() #스택의 꼭대기에서 노드를 하나 제거
        if target == temp: #해당 노드가 마지막 컵이면
            return True #True 리턴
        children = [] #자식 노드를 저장할 배열
        if temp not in visited: #해당 노드를 방문한 사실이 없다면
            visited.add(temp) #방문 셋에 추가
            children = graph[temp] if temp in graph else children #자식이 없다면 찾지 않는다
        stack += set(children) - visited #해당 노드의 자식 중 방문 사실이 없는 노드들을 스택에 추가
    return False #마지막 컵을 못 찾았으면 False 리턴

graph = {}
n = int(input())
for i in range(n):
    temp = input()
    if temp: #입력이 공백이 아닐 시
        graph[i] = list(map(int, temp.split())) #그래프 형성
print(cup(n-1, 0, graph))

