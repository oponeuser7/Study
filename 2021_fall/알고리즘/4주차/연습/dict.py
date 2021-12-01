def multiple_sort(input_list):
    return sorted(input_list, key=lambda x:(len(x), x))
input_list = list(input().split())
print(*multiple_sort(input_list))