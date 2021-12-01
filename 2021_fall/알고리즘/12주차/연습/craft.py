from collections import defaultdict, deque

def main():
    t = int(input())
    for i in range(t):
        ans = 0
        n, k = map(int, input().split())
        cost = {}
        edges = {}
        condition_count = {}
        costs = list(map(int, input().split()))
        for i in range(1, n+1):
            cost[str(i)] = costs[i-1]
            edges[str(i)] = []
            condition_count[str(i)] = 0
        for i in range(k):
            a, b = input().split()
            edges[a].append(b)
            condition_count[b] += 1
        target = input()
        print(condition_count[target])
        queue = deque()
        for i in range(1, n+1):
            if condition_count[str(i)]==0:
                queue.append((str(i), cost[str(i)]))
        while queue:
            temp = queue.popleft()
            node, temp_cost = temp[0], temp[1]
            condition_count[node] -= 1
            ans = max(temp_cost, ans)
            if node==target and condition_count[node]<=0: 
                break
            for nxt in edges[node]:
                queue.append((nxt, cost[nxt]+temp_cost))
        print(ans)

if __name__=="__main__": main()
