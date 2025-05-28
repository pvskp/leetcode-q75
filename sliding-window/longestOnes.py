class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left_index = 0
        max_window = 0
        zeros = 0

        for right_index in range(len(nums)):
            if nums[right_index] == 0:
                zeros += 1

            while zeros > k:
                if nums[left_index] == 0:
                    zeros -= 1

                left_index += 1

            max_window = max(max_window, right_index - left_index + 1)

        return max_window


t1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
t2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]

print(Solution().longestOnes(t1, 2) == 6)
print(Solution().longestOnes(t2, 3) == 10)
