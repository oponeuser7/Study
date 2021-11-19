def piramid(n): # 피라미드 함수
    if n == 1: # 말단 노드에 닿으면
        return 1 # 1 리턴
    return 1 + piramid(n-1)*2 # f(n) = f(1) + f(n-1) * 2 의 점화식으로 볼 수 있다.
    
print(piramid(int(input())))

