def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return abs(a)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]

### test
# s = Solution()
# print(s.gcdOfStrings("ABCABC", "ABC") == "ABC")
# print(s.gcdOfStrings("ABABAB", "ABAB") == "AB")
# print(s.gcdOfStrings("LEET", "CODE") == "")
