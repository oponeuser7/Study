import sys

def pre_order(node): #pre-order 함수
    if not node: return #리프 노드에서 리턴
    sys.stdout.write(node) #pre-order 출력
    pre_order(left[node]) #좌측 자식 호출
    pre_order(right[node]) #우측 자식 호출

def in_order(node): #in-order 함수
    if not node: return #리프 노드에서 리턴
    in_order(left[node]) #좌측 자식 호출
    sys.stdout.write(node) #in-order 출력
    in_order(right[node]) #우측 자식 호출

def post_order(node): #post-order 함수
    if not node: return #리프 노드에서 리턴
    post_order(left[node]) #좌측 자식 호출
    post_order(right[node]) #우측 자식 호출
    sys.stdout.write(node) #post-order 출력

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

