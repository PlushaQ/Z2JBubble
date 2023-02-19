def bubble_sort(lst):
    if sorted(lst) == lst:
        return "List already sorted"
    n = len(lst)
    for x in range(n):
        for y in range(n-1):
            if lst[y] > lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]
    print(lst)


