def climbing_stairs(n):
    # for i in range(n - 1, -1, -1):
    one, two = 1, 1
    for i in range(0, n - 1):
        print(i)
        temp = one
        one = one + two
        two = temp
    return one


print(climbing_stairs(5))
