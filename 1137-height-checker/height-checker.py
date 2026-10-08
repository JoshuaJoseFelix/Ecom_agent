class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        new=heights.copy()
        new.sort()
        out=0
        for l in range(len(new)):
            if new[l] != heights[l]:
                out +=1
        return out