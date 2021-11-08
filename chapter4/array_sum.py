def get_sum(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + get_sum(nums[1:])


print(get_sum([1, 5, 6, 6, 2]))
