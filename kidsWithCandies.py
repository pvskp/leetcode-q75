class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        mc = max(candies)

        new = [False] * len(candies)
        for i, k in enumerate(candies):
            if k + extraCandies >= mc:
                new[i] = True

        return new

### test
# s = Solution()
# print(s.kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True])
# print(s.kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False])
# print(s.kidsWithCandies([12,1,12], 10) == [True, False, True])
