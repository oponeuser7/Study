def bellman_ford(edges, v, src, dst, vertexes, costs): #벨만-포드 함수
    distance, prev, path = {}, {}, [] #최단거리, 경로를 저장할 닥셔너리, 리스트
    for vertex in vertexes: #모든 정점에 대해서
        distance[vertex] = float("inf") #src에서 정점까지의 거리를 무한으로 초기화
    distance[src] = 0 #src부터 src까지의 거리는 0
    for _ in range(v-1): #정점의 수 - 1번 반복
        for edge in edges: #모든 간선에 대해서
            if distance[edge[1]]>distance[edge[0]]+edge[2]: #더 짧은 경로를 찾았다면
                distance[edge[1]] = distance[edge[0]]+edge[2] #업데이트
                prev[edge[1]] = edge[0] #경로 저장
    for edge in edges: #음수 가중치 사이클 검사
        if distance[edge[1]]>distance[edge[0]]+edge[2]: return "Negative"
    temp = dst #목적지
    while temp in prev:
        #출발지, 목적지, 비용을 뒤에서부터 찾아 저장
        path.insert(0, prev[temp]+" "+temp+" "+costs[(prev[temp],temp)]) 
        temp = prev[temp]
    return "\n".join(path) #경로 리턴

def main():
    v, e = map(int, input().split())
    src, dst = input().split()
    edges, costs = [], {}
    vertexes = input().split()
    for _ in range(e):
        frm, to, cost = input().split()
        edges.append((frm, to, int(cost)))
        costs[(frm, to)] = cost
    print(bellman_ford(edges, v, src, dst, vertexes, costs))

if __name__=="__main__": main()


