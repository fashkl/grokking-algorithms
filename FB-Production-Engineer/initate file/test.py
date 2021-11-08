
# def canPartition(nums):
#     s = sum(nums)
#     if s % 2 == 1: return False
#
#     s //= 2
#     l = len(nums)
#     dp = []
#
#     for i in range(0, 2):
#         dp.append([0] * (s + 1))
#
#     print(dp)
#     print(s)
#
#     dp[0][0] = 1
#     for i in range(1, l + 1):
#         for j in range(0, s + 1):
#             if j == 0:
#                 dp[i % 2][j] = 1
#             elif j < nums[i - 1]:
#                 dp[i % 2][j] = dp[(i - 1) % 2][j]
#             else:
#                 dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[(i - 1) % 2][j - nums[i - 1]]
#         if dp[i % 2][s]:
#             return True
#     return False
# print(canPartition([1, 5, 11, 5]))

board = []

for x in range(7):
    board.append(["O"] * 7)


