class State:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    #Title: Robot Bounded In Circle
    #Approach: huristic, vector, math
    def isRobotBounded(self, instructions: str) -> bool:
        ans = set()
        dx, dy = (0,-1,0,1), (1,0,-1,0)
        init = State(0)
        temp = init
        for i in range(1,4):
            temp.next = State(i,temp)
            temp = temp.next
        temp.next = init
        init.prev = temp
        
        cur = [0,0]
        state = init

        for i in range(4):
            for inr in instructions:
                if inr=="G":
                    ans.add((cur[0]+dx[state.val], cur[1]+dy[state.val]))
                    cur[0] += dx[state.val]
                    cur[1] += dy[state.val]
                elif inr=="L":
                    state = state.next
                else:
                    state = state.prev
        
        count = len(ans)
        
        for i in range(4):
            for inr in instructions:
                if inr=="G":
                    ans.add((cur[0]+dx[state.val], cur[1]+dy[state.val]))
                    cur[0] += dx[state.val]
                    cur[1] += dy[state.val]
                elif inr=="L":
                    state = state.next
                else:
                    state = state.prev
        
        print(count,", ",len(ans))
        print(-1%4)
        if count==len(ans): return True
        return False

    def isRobotBounded_vector(self, instructions: str) -> bool:
        dx, dy = (0,-1,0,1), (1,0,-1,0)
        pos, head = [0,0], 0
        for inr in instructions:
            if inr=="G":
                pos[0] += dx[head]
                pos[1] += dy[head]
            elif inr=="L":
                head = (head+1)%4
            else:
                head = (head-1)%4
        return pos==[0,0] or head!=0
