from collections import defaultdict, deque

def bfs(src, dst, parent, edges): #bfs 함수
    visited = set([src]) #방문 체크 셋
    queue = deque([src]) #큐 초기화
    while queue: #큐가 빌 때 까지
        temp = queue.popleft() #큐에서 pop
        for node in edges[temp]: #모든 연결된 노드에 대하여
            capacity = edges[temp][node]
            #만약 연결된 노드가 방문한 사실이 없고 용량이 남아있다면
            if node not in visited and capacity>0:
                queue.append(node) #큐에 append
                visited.add(node) #방문 체크
                parent[node] = temp #경로를 얻기 위하여 노드 연결
    return dst in visited #dst에 도착할 수 있는지 여부 리턴

def min_flow(src, dst, parent, edges): #최소 용량 찾는 함수
    flow = float("inf")
    while src!=dst: #src에 도착할 때 까지
        flow = min(flow, edges[parent[dst]][dst]) #간선 용량의 최소값을 탐색
        dst = parent[dst]
    return flow #최소 용량 리턴
    
def pulled_fork(src, dst, edges): #포드-풀커슨 함수
    parent = defaultdict(lambda: -1)
    max_flow = 0
    while bfs(src, dst, parent, edges): #아직 유량이 흐를 수 있는 경로가 있다면
        #해당 경로에서의 최소 용량을 찾는다
        path_flow = min_flow(src, dst, parent, edges)
        max_flow += path_flow #최대 유량에 덧셈
        temp = dst #dst로부터
        while src!=temp: #src에 이르기까지
            temp2 = parent[temp]
            #모든 경로에서 최소 용량만큼을 감소
            edges[temp2][temp] -= path_flow
            temp = parent[temp]
    return max_flow #최대 유량을 리턴

def main():
    n = int(input())
    src, dst = "0", str(n-1)
    edges = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        temp = input().split()
        for j in range(len(temp)):
            edges[str(i)][str(j)] = int(temp[j])
    print(pulled_fork(src, dst, edges))

if __name__=="__main__": main()
