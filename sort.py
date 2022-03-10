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


