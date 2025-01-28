# # Unefficient solution (O(n^2))
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         max_area = 0
#
#         for i, v1 in enumerate(height):
#             for j, v2 in enumerate(height):
#                 if j == i:
#                     continue
#
#                 area = min(v1, v2) * (j - i)
#
#                 if area > max_area:
#                     max_area = area
#
#         return max_area

# O(n) solution
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        i = 0
        j = len(height) - 1

        while i < j:
            side = min(height[i], height[j])
            area = side * (j - i)
            if area > max_area:
                max_area = area

            if side == height[i]:
                i += 1
            else:
                j -= 1

        return max_area

inputs = (
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        )


s = Solution()
for i in inputs:
    print(s.maxArea(i[0]) == i[1])


# print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# print(s.maxArea([1,1]))
