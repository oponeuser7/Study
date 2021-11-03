def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5,4,3,2,1]))