class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num] +=1
        
        for n,c in hashmap.items():
            if c>1:
                return True 
        
        return False 