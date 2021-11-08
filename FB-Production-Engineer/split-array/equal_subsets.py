# def isItPossibleToSplitInTwoArrays(arr):
#     left_sum = 0
#     right_sum = sum(arr)
#
#     for i, n in enumerate(arr):
#         if left_sum == right_sum:
#             # print("left array: " + str(arr[:i]))
#             # print("right array: " + str(arr[i:]))
#             return True
#
#         right_sum -= n
#         left_sum += n
#         print("left array: " + str(arr[:i]))
#         print("right array: " + str(arr[i:]))
#         print('--------------------')
#     return False

def is_it_possible_to_split_in_two_arrays(nums):
    if sum(nums) % 2: return False

    dp = set()
    dp.add(0)

    target = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        next_dp = set()
        for totalValue in dp:
            if (totalValue + nums[i]) == target: return True
            next_dp.add(totalValue + nums[i])
            next_dp.add(totalValue)
        dp = next_dp

    print('----   ', dp)
    return True if target in dp else False


if __name__ == '__main__':
    print(is_it_possible_to_split_in_two_arrays([1, 15, 11, 5]))
