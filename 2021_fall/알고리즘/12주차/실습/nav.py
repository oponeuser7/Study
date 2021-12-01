from collections import defaultdict, deque

def bfs(src, dst, parent, edges):
    visited = set([src])
    queue = deque([src])
    while queue:
        temp = queue.popleft()
        for node in edges[temp]:
            capacity = edges[temp][node]
            if node not in visited and capacity>0:
                queue.append(node)
                visited.add(node)
                parent[node] = temp
    return dst in visited

def min_flow(src, dst, parent, edges):
    flow = float("inf")
    while src!=dst:
        flow = min(flow, edges[parent[dst]][dst])
        dst = parent[dst]
    return flow
    
def pulled_fork(src, dst, edges):
    parent = defaultdict(lambda: -1)
    max_flow = 0
    while bfs(src, dst, parent, edges):
        path_flow = min_flow(src, dst, parent, edges)
        max_flow += path_flow
        temp = dst
        while src!=temp:
            temp2 = parent[temp]
            edges[temp2][temp] -= path_flow
            temp = parent[temp]
    return max_flow

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
