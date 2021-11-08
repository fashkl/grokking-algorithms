def list_count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + list_count(arr[1:])


print(list_count([1, 5, 6, 6, 2, 3]))
