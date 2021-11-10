import heapq

def prim(edges, n, costs, start_node):
    visited = set()
    queue = []
    heapq.heappush(queue, (costs[start_node-1], 0, start_node))
    result = 0
    while queue:
        temp = heapq.heappop(queue)
        if temp[2] in visited:
            continue
        visited.add(temp[2])
        result += temp[0]
        frm = temp[2]
        for i in range(1, n+1):
            if i not in visited:
                cost, to = costs[i-1], i
                if (frm, to) in edges:
                    cost = min(edges[(frm, to)], cost)
                heapq.heappush(queue, (cost, frm, to))
    return result

n, m = map(int, input().split())
costs = list(map(int, input().split()))
min_val = float("inf")
start_node = 1
for cost in enumerate(costs):
    if min_val > cost[1]:
        min_val = cost[1]
        start_node = cost[0]+1
edges = {}
for i in range(m):
    a, b, c = map(int, input().split())
    edges[(a, b)] = c
    edges[(b, a)] = c
print(prim(edges, n, costs, start_node))