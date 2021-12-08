def napsack(cap, n, w, v):
    V = [[0]*(cap+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for W in range(1, cap+1):
            if w[i]<=W:
                V[i][W] = max(v[i]+V[i-1][W-w[i]], V[i-1][W])
            else:
                V[i][W] = V[i-1][W]
    return V[-1][-1]

def main():
    cap = int(input())
    n = int(input())
    w = list(map(int, input().split())) 
    v = list(map(int, input().split())) 
    w.insert(0,0)
    v.insert(0,0)
    print(napsack(cap, n, w, v))

if __name__=="__main__": main()

