def floyd_warshall(edges, v, d, vertexes): #플로이드-워셜 함수
    for i in vertexes:
        for j in vertexes:
            for k in vertexes: #모든 간선들에 대해서 정점 개수만큼 반복
                if edges[(j,k)]>edges[(j,i)]+edges[(i,k)]: #더 짧은 경로 찾아 갱신
                    edges[(j,k)] = edges[(j,i)]+edges[(i,k)]
    ans = {} #노드 별 거리 d 내에 위치한 노드 수를 저장할 닥셔너리
    for vertex in vertexes: #모든 정점에 대해서
        ans[vertex] = 0 #거리 d 내에 위치한 노드 수를 1로 초기화
    for edge in edges: #모든 간선을 읽어서
        #간선의 비용이 d보다 작으면 해당 간선의 출발노드를 ans에서 1 증가
        if edges[edge]<=d: ans[edge[0]] += 1
    max_key = max(ans, key=ans.get) #ans의 최대값을 찾아서
    return max_key+" "+str(ans[max_key]) #key와 value를 리턴

def main():
    v, e = map(int, input().split())
    d = int(input())
    vertexes = input().split()
    edges = {} #edge는 (src,dst) 형태의 튜플을 키로 하는 딕셔너리에 저장
    for i in vertexes:
        for j in vertexes:
            edges[(i,j)] = float("inf") if i!=j else 0
    for _ in range(e):
        frm, to, cost = input().split()
        edges[(frm,to)] = int(cost)
        edges[(to,frm)] = int(cost)
    print(floyd_warshall(edges, v, d, vertexes))

if __name__=="__main__": main()


