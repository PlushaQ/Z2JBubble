def bubble_sort(lst):
    if sorted(lst) == lst:
        print("List already sorted")
        return
    n = len(lst)
    for x in range(n):
        for y in range(n-1):
            if lst[y] > lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]
    print(f'Your sorted list is {lst}')


bubble_sort([1, 4, 6, 3, 2, 5])