class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        A = lambda x1, y1, x2, y2, x3, y3: abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
        best = 0
        for i in range(n - 1):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                for k in range(j + 1, n):
                    x3, y3 = points[k][0], points[k][1]
                    area = A(x1, y1, x2, y2, x3, y3)
                    best = max(best, area)
        return best