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