def bubble(input_list):
    length = len(input_list)
    for i in range(length):
        for j in range(length-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list
print(*bubble(list(map(int, input().split()))))