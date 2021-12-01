import sys
from math import log2
from collections import deque

def generate_tree(tree, n):
    for _ in range(n-1):
        parent, child = map(int, sys.stdin.readline().split())
        tree[child].append(parent)
        tree[parent].append(child)

def bfs(tree, parents, depth, n):
    queue = deque([1])
    visited = [False]*(n+1)
    while queue:
        temp = queue.popleft()
        visited[temp] = True
        for child in tree[temp]:
            if not visited[child]:
                queue.append(child)
                parents[child] = temp
                depth[child] = depth[temp]+1

def compute_exp_parent(exp_parents, n):
    for i in range(1, logN):
        for j in range(1, n+1):
            exp_parents[j][i] = exp_parents[exp_parents[j][i-1]][i-1]

def lca(exp_parents, depth, n, m):
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if depth[a] > depth[b]:
            a, b = b, a
        level_diff = depth[b] - depth[a]
        for i in range(logN):
            if level_diff & (1 << i):
                b = exp_parents[b][i]
        if a==b:
            sys.stdout.write(str(b)+"\n")
            continue
        for i in range(logN-1, -1, -1):
            if exp_parents[a][i] != exp_parents[b][i]:
                a = exp_parents[a][i]
                b = exp_parents[b][i]
        sys.stdout.write(str(exp_parents[a][0])+"\n")

n = int(sys.stdin.readline())
logN = int(log2(n)+1)
tree = [[] for _ in range(n+1)]
generate_tree(tree, n)
parents = [0]*(n+1)
depth = [0]*(n+1)
bfs(tree, parents, depth, n)
exp_parents = [[0 for i in range(logN)] for j in range(n+1)]
for i in range(n+1):
    exp_parents[i][0] = parents[i]
compute_exp_parent(exp_parents, n)
m = int(sys.stdin.readline())
lca(exp_parents, depth, n, m)