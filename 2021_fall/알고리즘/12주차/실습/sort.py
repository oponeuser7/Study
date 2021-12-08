from collections import defaultdict, deque

def solve(nodes, graph, pre):
    ans = []
    queue = deque()
    for node in nodes: #모든 노드에 대하여
        if pre[node]==0: queue.append(node) #선행조건이 없으면 큐에 push
    while queue: #큐가 빌 때 까지
        temp = queue.popleft() #큐에서 pop
        ans.append(temp) #정답 배열에 append
        for node in graph[temp]: #모든 연결된 노드에 대하여
            pre[node] -= 1 #연결된 노드의 선행조건 개수를 1 감소
            if pre[node]<=0: queue.append(node) #선행조건이 없다면 큐에 push
    return ans #정답을 리턴

def main():
    n, m = map(int, input().split())
    nodes = input().split()
    graph, pre = defaultdict(list), defaultdict(int) 
    for i in range(m):
        a, b = input().split()
        graph[a].append(b) #a에서 b로 가는 간선을 저장
        pre[b] += 1 #b의 선행조건 개수를 1 증가
    print(*solve(nodes, graph, pre))

if __name__=="__main__": main()
