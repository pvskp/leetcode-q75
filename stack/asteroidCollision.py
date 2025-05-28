class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans = []
        for i, a in enumerate(asteroids):
            if ans == [] or a > 0:
                ans.append(a)
                continue

            while ans != [] and a < 0 and ans[-1] > 0:
                if abs(a) > ans[-1]:
                    ans.pop()

                elif ans[-1] == abs(a):
                    ans.pop()
                    break

                elif abs(a) < ans[-1]:
                    break
            else:
                ans.append(a)

        return ans


s = Solution()

t1 = [5, 10, -5]
t2 = [8, -8]
t3 = [10, 2, -5]
t4 = [-2, -1, 1, 2]
t5 = [1, -2, -2, -2]

print(s.asteroidCollision(t1))
print(s.asteroidCollision(t2))
print(s.asteroidCollision(t3))
print(s.asteroidCollision(t4))
print(s.asteroidCollision(t5))
