import heapq
import math

def heuristic(current, end): #휴리스틱 함수, 2차원 직선거리를 계산
    return math.sqrt((end[1]-current[1])**2+(end[0]-current[0])**2)

def solve(row, col, start, end, graph, n):
    ans = 0 #정답을 저장할 변수
    dy, dx = (0,0,1,-1), (1,-1,0,0)
    #큐를 초기화, 튜플의 내용은 앞에서부터 순서대로 g+h, g, 좌표이다
    queue = [(heuristic(start, end), 0, start)]
    visited = set() #방문 체크 셋
    while queue: #힙이 빌 때 까지
        temp = heapq.heappop(queue) #힙에서 pop
        cost, spent, y, x = temp[0], temp[1], temp[2][0], temp[2][1]
        visited.add((y,x)) #방문 체크
        if end[0]==y and end[1]==x: #도착지 좌표에 도달했다면
            ans = spent #정답을 저장하고 break
            break
        for i in range(4): #동서남북 방향에 대하여
            ny, nx = y+dy[i], x+dx[i]
            #그래프 범위 내에 있고 방문한 사실이 없다면
            if 0<=ny<row and 0<=nx<col and (ny,nx) not in visited:
                g = spent+graph[ny][nx] #g(얼음이 녹은 양)을 갱신
                gh = g+heuristic((ny,nx),end) #휴리스틱을 계산
                heapq.heappush(queue, (gh, g, (ny, nx))) #힙에 push 
    if ans>n: return "FAIL" #결과 얼음의 양이 음수가 되었다면 FAIL
    return n-ans #답을 리턴

def main():
    row, col, n = map(int, input().split()) 
    start, end = None, None
    graph = [[] for _ in range(row)] #그래프를 리스트의 딕셔너리로 초기화
    for i in range(row):
        temp = input()
        for j in range(len(temp)):
            if temp[j]=='S': #입력이 S면 start에 저장하고 값은 0으로 저장
                start = (i,j)
                graph[i].append(0)
            elif temp[j]=='E': #입력이 E면 end에 저장하고 값은 0으로 저장
                end = (i,j)
                graph[i].append(0)
            else: #외의 경우에는 입려 값을 저장
                graph[i].append(int(temp[j]))
    print(solve(row, col, start, end, graph, n))

if __name__=="__main__": main()
