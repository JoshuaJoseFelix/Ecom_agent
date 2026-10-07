class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=len(nums)//2
        x=nums[0:mid]
        y=nums[mid:]
        new=[]
        i =0 
        j =0
        while i < len(x) and j < len(y):
            new.append(x[i])
            new.append(y[j])
            i += 1
            j += 1

        return new

        
        
        