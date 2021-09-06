def cal(n):
    x = -334
    count = 0
    for i in range(100000):
        x += 1000
        if i%10 == 6:
            if i%100 == 66:
                if i%1000 == 666:
                    if i%10000 == 6666:
                        temp = x - 6667
                        for j in range(10000):
                            temp += 1
                            count += 1
                            if count == n:
                                return temp
                    else:
                        temp = x - 667
                        for j in range(1000):
                            temp += 1
                            count += 1
                            if count == n:
                                return temp
                else:
                    temp = x - 67
                    for j in range(100):
                        temp += 1
                        count += 1
                        if count == n:
                            return temp
            else:
                temp = x - 7
                for j in range(10):
                    temp += 1
                    count += 1
                    if count == n:
                        return temp
        else:
            count += 1
            if count == n:
                return x
        if count == 10000:
            return x
n = int(input())
print(cal(n))
