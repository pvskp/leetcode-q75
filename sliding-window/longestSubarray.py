from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_index = 0
        max_window = 0
        zeros = 0

        for right_index in range(len(nums)):
            if nums[right_index] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left_index] == 0:
                    zeros -= 1

                left_index += 1

            max_window = max(max_window, right_index - left_index)

        return max_window


s = Solution()
t1 = [1, 1, 0, 1]
t2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
t3 = [1, 1, 1]

print(s.longestSubarray(t1))
print(s.longestSubarray(t2))
print(s.longestSubarray(t3))
