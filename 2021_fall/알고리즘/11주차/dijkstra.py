import heapq

def dijkstra(edges, v, src, dst, vertexes): #다익스트라 함수
    distance = {} #src로부터의 거리 딕셔너리
    for vertex in vertexes: #src로부터의 거리를
        distance[vertex] = float("inf") #무한으로 초기화
    distance[src] = 0 #src부터 src까지의 거리는 0
    path, prev = [dst], {} #경로를 저장할 path 리스트와 경로의 이전 노드를 저장할 prev 딕셔너리
    queue = [(0, src)] #힙에 src를 push
    found = set() #최단거리를 찾았음을 저장할 set
    while queue: #힙이 빌 때 까지
        v = heapq.heappop(queue) #힙에서 원소를 pop
        found.add(v[1]) #현재 노드의 최단거리를 찾았다
        for node in edges[v[1]]: #현재 노드의 모든 간선에 대해서
            if node[0] in found: continue #이미 최단거리를 찾은 노드라면 continue
            if distance[node[0]]>distance[v[1]]+node[1]: #더 짧은 경로를 찾았다면
                distance[node[0]] = distance[v[1]]+node[1] #업데이트
                heapq.heappush(queue, (distance[node[0]], node[0])) #힙에 push
                prev[node[0]] = v[1] #경로 저장
    temp = dst #목적지
    while temp in prev: #목적지로부터 거꾸로 경로를 찾아 저장
        path.insert(0, prev[temp]) 
        temp = prev[temp]
    print("".join(map(str, path))) #경로 출력
    return distance[dst] #최단거리 출력

def main():
    v, e = map(int, input().split())
    src, dst = input().split()
    edges = {}
    vertexes = input().split()
    for edge in vertexes:
        edges[edge] = []
    for _ in range(e):
        frm, to, cost = input().split()
        edges[frm].append((to, int(cost)))
        edges[to].append((frm, int(cost)))
    print(dijkstra(edges, v, src, dst, vertexes))

if __name__=="__main__": main()


