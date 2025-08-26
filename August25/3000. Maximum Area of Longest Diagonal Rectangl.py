# You are given a 2D 0-indexed integer array dimensions.
#
# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.
#
# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea, Mdia2 = 0, 0
        for w, h in dimensions:
            dia2 = w * w + h * h
            if Mdia2 < dia2:
                Mdia2 = dia2
                maxArea = 0
            if dia2 == Mdia2:
                maxArea = max(maxArea, w * h)
        return maxArea
