class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_position = []
        vowels = set("aeiouAEIOU")
        for i, v in enumerate(s):
            if (v in vowels):
                vowels_position.append(i)

        start = 0
        end = len(vowels_position) - 1

        s_list = list(s)

        while start < end:
            s_list[vowels_position[start]], s_list[vowels_position[end]] = (
                s_list[vowels_position[end]],
                s_list[vowels_position[start]],
            )
            start += 1
            end -= 1

        return "".join(s_list)


## test
s = Solution()
print(s.reverseVowels("IceCreAm") == "AceCreIm")
print(s.reverseVowels("leetcode") == "leotcede")
