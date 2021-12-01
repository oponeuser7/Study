import heapq
import math

def heuristic(current, end):
    return math.sqrt((end[1]-current[1])**2+(end[0]-current[0])**2)

def solve(row, col, start, end, graph, n):
    ans = 0
    dy, dx = (0,0,1,-1), (1,-1,0,0)
    queue = [(heuristic(start, end), 0, start)]
    visited = set()
    while queue:
        temp = heapq.heappop(queue)
        cost, spent, y, x = temp[0], temp[1], temp[2][0], temp[2][1]
        visited.add((y,x))
        if end[0]==y and end[1]==x:
            ans = spent
            break
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<row and 0<=nx<col and (ny,nx) not in visited:
                g = spent+graph[ny][nx]
                gh = g+heuristic((ny,nx),end)
                heapq.heappush(queue, (gh, g, (ny, nx))) 
    if ans>n: return "FAIL"
    return n-ans

def main():
    row, col, n = map(int, input().split()) 
    start, end = None, None
    graph = [[] for _ in range(row)]
    for i in range(row):
        temp = input()
        for j in range(len(temp)):
            if temp[j]=='S': 
                start = (i,j)
                graph[i].append(0)
            elif temp[j]=='E': 
                end = (i,j)
                graph[i].append(0)
            else:
                graph[i].append(int(temp[j]))
    print(solve(row, col, start, end, graph, n))

if __name__=="__main__": main()
