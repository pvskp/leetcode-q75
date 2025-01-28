from typing import final


class Solution:
    def reverseWords(self, s: str) -> str:
        formed_string = ""
        word_list = []
        for i, char in enumerate(s):
            if char == " " and formed_string == "":
                continue

            last = i == (len(s) - 1)
            if char == " " or last:
                if last and char != " ":
                    formed_string += char

                word_list.append(formed_string)
                formed_string = ""
                continue

            formed_string += char

        final_string = ""
        for i in range(len(word_list) - 1, -1, -1):
            final_string += word_list[i]
            last = i == 0

            if not last:
                final_string += " "

        return final_string


s = Solution()
print(s.reverseWords("the sky is blue") == "blue is sky the")
print(s.reverseWords("  hello world  ") == "world hello")
print(s.reverseWords("a good   example") == "example good a")
print(s.reverseWords("t ") == "t")
