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