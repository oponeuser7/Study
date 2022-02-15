def solve(cor, c):
    def check(mid):
        if d//mid<c-1: return False
        count, a, b = 1, cor[0], 0
        for t in cor:
            b += t-a
            a = t
            if b>=mid:
                count += 1
                b = 0
        return count>=c

    d = max(cor) - min(cor)
    l, r, n, ans = 1, 1000000000, len(cor), 0
    while l<=r:
        mid = (l+r)//2
        if check(mid):
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans
        
def main():
    n, c = map(int, input().split())
    cor = []
    for i in range(n):
        cor.append(int(input()))
    cor.sort()
    print(solve(cor, c))

if __name__=="__main__": main()
