class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = 0
        for v in nums:
            total_sum += v

        left_sum = 0
        for i, v in enumerate(nums):
            right_sum = total_sum - left_sum - v
            if right_sum == left_sum:
                return i

            left_sum += v

        return -1


# print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
print(Solution().pivotIndex([1, 2, 3]) == -1)
print(Solution().pivotIndex([2, 1, -1]) == 0)
