from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = defaultdict(int)
        for r in grid:
            freq[str(r)] += 1

        count = 0
        for i in range(len(grid)):
            column = []
            for j in range(len(grid[0])):
                column.append(grid[j][i])

            str_col = str(column)
            if str_col in freq:
                count += freq[str_col]

        return count


t1 = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
t2 = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

s = Solution()

print(s.equalPairs(t1) == 1)
print(s.equalPairs(t2) == 3)
