def reverse_range(arr, l, r):
    ## [2,3,6,32,42,42] ##

    if l > r: return
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


def revers_element(array, l, r):
    if l > r:
        print("invalid range!!!")

    for i in range(l, l + r // 2):
        temp = array[l + i]
        array[l + i] = array[r - i]
        array[r - i] = temp

    return array


if __name__ == '__main__':
    print(reverse_range([2, 3, 5, 4, 9, 13, 17], 2, 6))
    print(revers_element([2, 3, 5, 4, 9, 13, 17], 2, 6))

