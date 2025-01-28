class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                free_left = (i == 0) or (flowerbed[i - 1] == 0)
                free_right = (i == (len(flowerbed) - 1)) or (flowerbed[i + 1] == 0)

                if free_left and free_right:
                    flowerbed[i] = 1
                    count += 1

        if count >= n:
            return True

        return False

## Test
s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
