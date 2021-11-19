import math
import sys

n = int(input())
input()
target = float(input())
k = int(input())
if target<1:
    for i in range(1, k+1):
        sys.stdout.write(str(i)+" ")
else:
    temp = round(target)
    count = 0
    if temp > target:
        for i in range(1,k+1):
            sys.stdout.write(str(temp+i-1)+" ")
            count += 1
            if count==k: break
            if temp-i>=1:
                sys.stdout.write(str(temp-i)+" ")
                count +=1
            if count==k: break       
    else:
        for i in range(1,k+1):
            if temp+1-i>=1:
                sys.stdout.write(str(temp+1-i)+" ")
                count += 1
            if count==k: break
            sys.stdout.write(str(temp+i)+" ")
            count += 1
            if count==k: break