cache = [0]*46
def solve(n):
    global cache
    if cache[n]: return cache[n]
    if n<2: 
        cache[n] = n
        return cache[n]
    cache[n] = solve(n-1)+solve(n-2)
    return cache[n]

def main():
    n = int(input())
    print(solve(n))

if __name__=="__main__": main()

