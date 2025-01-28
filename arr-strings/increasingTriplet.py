class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        m1 = float("inf")
        m2 = float("inf")
        for n in nums:
            if n <= m1:
                m1 = n
            elif n <= m2:
                m2 = n
            else:
                print(m1, m2, n)
                return True
        return False


s = Solution()
print(s.increasingTriplet([1,5,2,0,3]))
# print(s.increasingTriplet([2, 2, 3, 4, 5]))
# print(s.increasingTriplet([5, 4, 3, 2, 1]))
# print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))
# print(s.increasingTriplet([20, 100, 10, 12, 5, 13]))
