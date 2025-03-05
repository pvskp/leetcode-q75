class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        vowels_count = 0
        max_vowels = 0

        for i in range(0, k):
            if s[i] in vowels:
                vowels_count += 1

        max_vowels = vowels_count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                vowels_count -= 1

            if s[i] in vowels:
                vowels_count += 1

            max_vowels = max(max_vowels, vowels_count)

        return max_vowels

print(Solution().maxVowels("abciiidef", 3) == 3)
print(Solution().maxVowels("aeiou", 2) == 2)
print(Solution().maxVowels("leetcode", 3) == 2)
