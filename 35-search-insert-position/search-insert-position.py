class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        res=len(nums)
        l,r = 0,len(nums) - 1
        while l <= r:
            m=(l+r)//2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                res = m
                r = m - 1
            else:
                return m

        return res
        