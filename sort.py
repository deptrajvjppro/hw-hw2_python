def sort_list(l):
    n = len(l)
    i = 1
    while i<len(l):
        j = 0
        while j<=len(l)-i-1:
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
            j += 1
        i += 1
    return l


unsorted_list = [34, 76, 90, 12, 32, 44, 55]
sorted_list = sort_list(unsorted_list)
print(sorted_list)
list = [1,3,2,7]
sorted_list = sort_list(list)
print(sorted_list)