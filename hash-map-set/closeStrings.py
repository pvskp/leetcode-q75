class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        n = len(word1)

        set_w1 = set(word1)
        set_w2 = set(word2)

        if set_w1 != set_w2:
            return False

        freq_w1 = {}
        freq_w2 = {}

        for i in range(n):
            c1 = word1[i]
            c2 = word2[i]
            if c1 in freq_w1:
                freq_w1[c1] += 1
            else:
                freq_w1[c1] = 1

            if c2 in freq_w2:
                freq_w2[c2] += 1
            else:
                freq_w2[c2] = 1

        freq_set_1 = sorted(freq_w1.values())
        freq_set_2 = sorted(freq_w2.values())

        if freq_set_1 == freq_set_2:
            return True

        return False


s = Solution()

t1 = ("abc", "bca")
t2 = ("a", "aa")
t3 = ("cabbba", "abbccc")
t4 = ("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff")

print(s.closeStrings(*t1) == True)
print(s.closeStrings(*t2) == False)
print(s.closeStrings(*t3) == True)
print(s.closeStrings(*t4) == False)
