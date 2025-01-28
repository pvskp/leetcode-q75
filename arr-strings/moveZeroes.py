class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        nums_zero = nums.count(0)
        for i in len(nums):
            ...
        while i < len(nums):
            if nums[i] != 0:
                nums.append(nums.pop(i))
            i += 1

        for _ in range(nums_zero):
            nums.append(nums.pop(0))

        print(nums)


s = Solution()
s.moveZeroes([0,1,0,3,12])
s.moveZeroes([0])
s.moveZeroes([0,0,1])
