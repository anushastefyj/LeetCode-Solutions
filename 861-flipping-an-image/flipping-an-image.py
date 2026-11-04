class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        for row in image:
            left, right = 0, n - 1
            while left <= right:
                if row[left] == row[right]:
                    row[left] = row[right] = row[left] ^ 1
                left += 1
                right -= 1
        return image