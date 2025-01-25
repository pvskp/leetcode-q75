class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        last = "w2"
        new_string = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                new_string += word1[i]

            if i < len(word2):
                new_string += word2[i]

        return new_string

s = Solution()
print(s.mergeAlternately("abc", "pqr"))
