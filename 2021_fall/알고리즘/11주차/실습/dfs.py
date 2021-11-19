import sys

def pre_order(node):
    if not node: return
    sys.stdout.write(node)
    pre_order(left[node])
    pre_order(right[node])

def in_order(node):
    if not node: return
    in_order(left[node])
    sys.stdout.write(node)
    in_order(right[node])

def post_order(node):
    if not node: return
    post_order(left[node])
    post_order(right[node])
    sys.stdout.write(node)

n = int(input())
left = {}
right = {}
for i in range(n):
    p, l, r = input().split()
    left[p] = l if l!='.' else ""
    right[p] = r if r!='.' else ""
pre_order('A')
print()
in_order('A')
print()
post_order('A')