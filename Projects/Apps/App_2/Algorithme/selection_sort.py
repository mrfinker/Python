def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                #swap la valeur actuel avec la valeur min

        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr


nums = [64,55,25,96,45,85,2,36,58,4,7]
sort_num = selection_sort(nums)
print(sort_num)