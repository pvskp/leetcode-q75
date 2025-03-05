class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left_index = 0
        right_index = 0

        for right_index in range(len(nums)):

            ...

        return right_index - left_index + 1
        ...

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6)
