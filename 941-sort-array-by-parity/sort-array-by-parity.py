class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]%2 == 0:
                l +=1
            
            elif nums[r]%2 == 0 and nums[l]%2 != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l +=1
                r -=1
            else :
        
                r -=1
        return nums
            

            