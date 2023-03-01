# Beats 94% cpu, 88% mem

class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int) -> List[List[int]]:
        A = len(image)
        B = len(image[0])
        prev_color = image[sr][sc]
        if color == prev_color:
            return image

        stack = [(sr, sc)]
        while stack:
            a, b = stack.pop()
            if image[a][b] != prev_color:
                continue
            image[a][b] = color

            if a >= 1:
                stack.append((a - 1, b))
            if a < A - 1:
                stack.append((a + 1, b))
            if b >= 1:
                stack.append((a, b - 1))
            if b < B - 1:
                stack.append((a, b + 1))
        return image


