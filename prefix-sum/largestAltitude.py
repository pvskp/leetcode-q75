class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_max = 0
        curr_sum = 0
        for v in gain:
            curr_sum += v
            curr_max = max(curr_max, curr_sum)

        return curr_max


print(Solution().largestAltitude([-5, 1, 5, 0, -7]) == 1)
print(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0)
