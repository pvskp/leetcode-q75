class Solution:
    def removeStars(self, s: str) -> str:
        answer = []

        for c in s:
            if c != "*":
                answer.append(c)
            else:
                answer.pop()

        return "".join(answer)


# WARN: bad solution
#
# class Solution:
#     def removeStars(self, s: str) -> str:
#         s_list = list(s)
#         stars = 0
#         for c in s:
#             if c == "*":
#                 stars += 1
#
#         i = 0
#         rodada = 0
#         while stars > 0:
#             rodada += 1
#             if s_list[i] == "*":
#                 if i > 0:
#                     s_list.pop(i - 1)
#                     s_list.pop(i - 1)
#                     stars -= 1
#                     i -= 1
#                     continue
#
#                 else:  # i == 0
#                     s_list.pop(i)
#                     stars -= 1
#                     break
#
#             i += 1
#
#         return "".join(s_list)
#

from pathlib import Path

t1 = "leet**cod*e"
t2 = "erase*****"
t3 = "xa**j*z*e*a*q*ry*bioj*mzd**k**g*"
t4 = Path("./removeStarts-t4.txt").read_text()
s = Solution()

print(s.removeStars(t1))
print(s.removeStars(t2))
print(s.removeStars(t3))
print(s.removeStars(t4))
