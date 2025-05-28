from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        s = set()
        for item in arr:
            if item in map:
                map[item] += 1
            else:
                map[item] = 1

        for _, v in map.items():
            if v in s:
                return False

            s.add(v)

        return True


t1 = [1, 2, 2, 1, 1, 3]
t2 = [1, 2]
t3 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

s = Solution()

print(s.uniqueOccurrences(t1))
print(s.uniqueOccurrences(t2))
print(s.uniqueOccurrences(t3))
