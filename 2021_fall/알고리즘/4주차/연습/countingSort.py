def count(input_list):
    arr = [0] * len(input_list)
    for i in input_list:
        arr[int(i)-1] += 1
    result = ""
    for i in range(len(arr)):
        result += str(i+1)*arr[i]
    return result
print(count(list(input().split())))
    