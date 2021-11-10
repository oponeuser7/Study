from math import log2

def generate_tree(tree, n):
    for _ in range(n-1):
        parent, child = map(int, input().split())
        tree[child].append(parent)
        tree[parent].append(child)

def dfs(tree, parents, depth, n):
    queue = [1]
    visited = [False]*(n+1)
    while queue:
        temp = queue.pop(0)
        visited[temp] = True
        for child in tree[temp]:
            if not visited[child]:
                queue.append(child)
                parents[child] = temp
                depth[child] = depth[temp]+1

def compute_exp_parent(exp_parents, n):
    logN = (int)(log2(n))
    for i in range(1, n+1):
        for j in range(1, logN):
            exp_parents[i][j] = exp_parents[exp_parents[i][j-1]][j-1]

def lca(exp_parents, depth, n, m):
    logN = (int)(log2(n))
    for _ in range(m):
        a, b = map(int, input().split())
        if depth[a] > depth[b]:
            a, b = b, a
        level_diff = depth[b] - depth[a]
        for i in range(logN):
            if level_diff & 1 << i:
                b = exp_parents[b][i]
        if a==b:
            print(a)
            continue
        for i in range(logN-1, -1, -1):
            if exp_parents[a][i] != exp_parents[b][i]:
                a = exp_parents[a][i]
                b = exp_parents[b][i]
        print(exp_parents[a][0])

n = int(input())
tree = [[] for _ in range(n+1)]
generate_tree(tree, n)
parents = [0]*(n+1)
depth = [0]*(n+1)
dfs(tree, parents, depth, n)
logN = (int)(log2(n))
exp_parents = [[0 for i in range(logN)] for j in range(n+1)]
for i in range(1, n+1):
    exp_parents[i][0] = parents[i]
compute_exp_parent(exp_parents, n)
m = int(input())
lca(exp_parents, depth, n, m)