class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        s_pointer = 0
        for c in t:
            if c == s[s_pointer]:
                # print("c == s[s_pointer]")
                # print(f"{c} == {s[s_pointer]}")
                s_pointer += 1

            # print(f"s_pointer = {s_pointer}")
            if s_pointer > (len(s) - 1):
                return True


        return False





s = Solution()

inputs = (
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
    )

for item in inputs:
    print(s.isSubsequence(item[0], item[1]) == item[2])
