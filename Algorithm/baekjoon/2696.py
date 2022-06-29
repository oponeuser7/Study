import heapq

def solve(m, seq):
    l = len(seq)
    q = []
    for i, val in enumerate(seq):
        heapq.heappush(q, val)
        if i%2==0: print(q[i//2], end=" ")
    print()

def main():
    t = int(input())
    for i in range(t):
        m = int(input())
        seq = list(map(int, input().split()))
        solve(m, seq)

if __name__=="__main__": main()
