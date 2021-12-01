import heapq
ans = [["1","2","3"],["4","5","6"],["7","8","#"]]

def make_key(puzzle):
    return "".join(puzzle[0])+"".join(puzzle[1])+"".join(puzzle[2])

def cal_h(puzzle):
    cost = 0 
    for i in range(3):
        for j in range(3):
            if ans[i][j]!=puzzle[i][j]: cost += 1 
    return cost

def solve(puzzle):
    dy, dx = (0,0,1,-1), (1,-1,0,0)
    visited = set()
    visited.add(make_key(puzzle)) 
    y, x = 0, 0
    cost = cal_h(puzzle)
    for i in range(3):
        for j in range(3):
            if puzzle[i][j]=="#": y, x = i, j
    queue = [(cost, cost, 0, y, x, puzzle)]
    while queue:
        temp = heapq.heappop(queue)
        cost, h, g, y, x, puzzle = temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]
        if h==0: return cost
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<3 and 0<=nx<3:
                new_puzzle = [0]*3
                for i in range(3):
                    new_puzzle[i] = puzzle[i][:]
                new_puzzle[y][x], new_puzzle[ny][nx] = new_puzzle[ny][nx], new_puzzle[y][x]
                key = make_key(new_puzzle)
                if key not in visited:
                    visited.add(key)
                    temp_h = cal_h(new_puzzle)
                    heapq.heappush(queue, (temp_h+g+1, temp_h, g+1, ny, nx, new_puzzle))
    return "impossible"

def main():
    n = int(input())
    for i in range(n):
        input()
        puzzle = [[] for _ in range(3)]
        for i in range(3):
            temp = input()
            for j in range(3):
                puzzle[i].append(temp[j])
        print(solve(puzzle))

if __name__=="__main__": main()
