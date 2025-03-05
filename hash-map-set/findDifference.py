class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        items_on_first = set(nums1)
        items_on_second = set(nums2)

        already_added_first = set()
        already_added_second = set()

        missing_first = []
        missing_second = []

        for n in nums1:
            if n not in items_on_second and n not in already_added_first:
                missing_first.append(n)
                already_added_first.add(n)

        for n in nums2:
            if n not in items_on_first and n not in already_added_second:
                missing_second.append(n)
                already_added_second.add(n)

        return [missing_first, missing_second]


print(Solution().findDifference([1, 2, 3], [2, 4, 6]))
print(Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
