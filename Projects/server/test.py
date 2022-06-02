def binary_search(list, find_value):
    low = 0
    high = len(list)
    while low <= high:
        mid = (low + high)//2
        if list[mid] < find_value:
            low = mid
        elif list[mid] > find_value:
            high = mid
        else:
            return mid

nums = [1,2,3,4,5,6,7,8,9]
index = binary_search(nums, 8)
print(index)
print()

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - 1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

nums = [64,34,25,12,22,11,90]
sort_num = bubble_sort(nums)
print(sort_num)
print()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert = arr[i]

        j = i - 1
        while insert < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = insert
    return arr

nums = [12,14,58,6,9,66,9,5,4,8,9,66,3,2,5]
sort_num = insertion_sort(nums)
print(sort_num)
print()

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr

nums = [5,65,8,6,9,55,88,7,4,5,55,88,999666,555,44,522,555,]
sort_num = selection_sort(nums)
print(sort_num)
print()