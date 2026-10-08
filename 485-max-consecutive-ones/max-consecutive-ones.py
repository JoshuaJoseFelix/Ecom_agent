class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
                maxcount=max(maxcount,count)
            elif nums[i] != 1:
                count=0

        return maxcount