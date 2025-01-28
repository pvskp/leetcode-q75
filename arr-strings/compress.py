class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        response = 0
        input_size = len(chars)

        while i < input_size:
            curr = chars[i]
            group_len = 1
            while (i + group_len < input_size) and (chars[i + group_len] == curr):
                group_len += 1
            chars[response] = curr
            response += 1
            if group_len > 1:
                for c in str(group_len):
                    chars[response] = c
                    response += 1

            i += group_len

        print(response)
        return response




s = Solution()
s.compress(["a","a","b","b","c","c","c"])
s.compress(["a"])
s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

