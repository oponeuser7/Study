def train(root, graph):
    stack = [root]
    visited = [root]
    while stack:
        temp = stack.pop()
        children = graph[temp] if temp in graph else []
        for node in children:
            if node not in visited:
                stack.append(node)
                visited.append(node)
    return len(visited)==len(graph)

graph = {}
n, m = map(int, input().split())
names = input().split()
for name in names:
    graph[name] = []
root = names[0]
for i in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)
print(train(root, graph))
