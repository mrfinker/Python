import numbers


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
sort_nums = insertion_sort(nums)
print(sort_nums)