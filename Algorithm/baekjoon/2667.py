from collections import deque

# 입력
n = int(input())
arr = [[0 for i in range(n)] for j in range(n)] # 2차원 배열 선언
for i in range(n):
    temp = input()
    for j in range(n):
        arr[i][j] = int(temp[j])

q = deque() # 큐 선언
division = list() # 단지 정보를 저장할 리스트
cross = [[0,1],[0,-1],[1,0],[-1,0]] # 상하좌우 처리를 위한 값
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: # 집(1)이 있는 곳이라면
            arr[i][j] = 0
            count = 1
            q.append([i, j]) # 최초의 cell을 offer
            # bfs를 통해 상하좌우로 인접한 1을 찾아내며 count를 증가시킨다.
            while q:
                temp = q.pop() # 큐에서 poll
                y = temp[0]
                x = temp[1]
                for k in range(4): # 상하좌우니까 4번 반복
                    xx = x + cross[k][1]
                    yy = y + cross[k][0]
                    if xx < n and xx >= 0 and yy < n and yy >= 0: # 해당 인접 cell이 지도 내에 존재하고
                        if arr[yy][xx] == 1: # 값이 1이라면
                            arr[yy][xx] = 0
                            count+=1
                            q.append([yy, xx]) # 값을 0으로 만들고 count를 증가한 뒤 큐에 offer
            division.append(count) # count를 저장
            count = 0
division.sort() # 오름차순 정렬
print(len(division)) # 리스트의 길이가 바로 총 단지수
for i in division:
    print(i) # 각 단지 내 집의 수 출력