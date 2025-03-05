class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        freq = {}
        operations = 0
        for n in nums:
            complement = k - n
            if complement in freq and freq[complement] > 0:
                operations += 1
                freq[complement] -= 1
                continue

            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        return operations

s = Solution()
print(s.maxOperations([1,2,3,4], 5) == 2)
