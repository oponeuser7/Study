from collections import defaultdict, deque

def solve(nodes, graph, pre):
    ans = []
    queue = deque()
    for node in nodes:
        if pre[node]==0: queue.append(node)
    while queue:
        temp = queue.popleft()
        ans.append(temp)
        for node in graph[temp]:
            pre[node] -= 1
            if pre[node]<=0: queue.append(node)
    return ans

def main():
    n, m = map(int, input().split())
    nodes = input().split()
    graph, pre = defaultdict(list), defaultdict(int) 
    for i in range(m):
        a, b = input().split()
        graph[a].append(b) 
        pre[b] += 1
    print(*solve(nodes, graph, pre))

if __name__=="__main__": main()
