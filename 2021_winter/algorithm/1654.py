def solve(d, n):
    def check(mid):
        count = 0
        for t in d:
            count += t//mid
        return count>=n
            
    l, r, ans = 0, max(d)*2, 0
    while l<=r:
        mid = (l+r)//2
        if check(mid):
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans

def main():
    k, n = map(int, input().split())
    d = []
    for i in range(k):
        d.append(int(input()))
    print(solve(d, n))

if __name__=="__main__": main()
