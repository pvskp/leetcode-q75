class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mult = 1
        zero_count = 0
        for i, n in enumerate(nums):
            if n == 0:
                zero_count += 1
                continue
            mult *= n

        answer = [0] * len(nums)
        if zero_count > 1:
            return answer

        for i, n in enumerate(nums):
            if n ==  0:
                answer[i] = mult
                continue

            if zero_count > 0:
                answer[i] = 0
                continue

            answer[i] = mult // nums[i]


        return answer


s = Solution()
s.productExceptSelf([1, 2, 3, 4])
s.productExceptSelf([-1, 1, 0, -3, 3])
