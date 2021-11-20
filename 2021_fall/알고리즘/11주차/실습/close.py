import sys

n = int(input())
input()
target = float(input())
k = int(input())
if target<1: #target이 음수 또은 0이라면
    for i in range(1, k+1): #1부터 k까지 출력
        sys.stdout.write(str(i)+" ")
else: #target이 양수라면
    temp = round(target) #target 반올림
    count = 0 #출력한 횟수 -> k번만큼 출력
    if temp > target: #올림되었다면
        for i in range(1,k+1): #큰값, 작은값, 큰값 ... 순으로 출력
            sys.stdout.write(str(temp+i-1)+" ")
            count += 1
            if count==k: break
            if temp-i>=1:
                sys.stdout.write(str(temp-i)+" ")
                count +=1
            if count==k: break       
    else: #내림되었다면
        for i in range(1,k+1): #작은값, 큰값, 작은값 ... 순으로 출력
            if temp+1-i>=1:
                sys.stdout.write(str(temp+1-i)+" ")
                count += 1
            if count==k: break
            sys.stdout.write(str(temp+i)+" ")
            count += 1
            if count==k: break

            