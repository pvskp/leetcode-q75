########################
# Extra space approach #
########################
# class Solution:
#     def moveZeroes(self, nums: list[int]) -> list[int]:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         new_list = []
#         for item in reversed(nums):
#             if item == 0:
#                 new_list.append(item)
#                 continue
#
#             new_list.insert(0, item)
#         return new_list

#########################
# Linear Space approach #
#########################
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for item in nums:
            if item == 0:
                zero_count += 1

        zero_operations = 0

        i = 0
        while zero_operations < zero_count:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                zero_operations += 1

                if nums[i] != 0:
                    i += 1
                continue

            i += 1


inputs = (
        ([0,1,0,3,12], [1,3,12,0,0]),
        ([0], [0]),
        ([1,0], [1,0]),
        ([0,0,1], [1,0,0]),
    )

s = Solution()

for item in inputs:
    s.moveZeroes(item[0])
    # print(item[0])
    print(item[0] == item[1])
    # assert item[0] == item[1]
