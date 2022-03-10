def sort_list(list):
    n = len(list)
    i = 0
    while i<n:
        j = 0
        while j< n-i-1:
            if list[j+1] < list[j]:
                list[j], list[j+1] = list[j+1], list[j]
            j += 1
        i += 1
    return list


unsorted_list = [34, 76, 90, 12, 32, 44, 55]
sorted_list = sort_list(unsorted_list)
print(sorted_list)
list = [1,3,2,7]
sorted_list = sort_list(list)
print(sorted_list)