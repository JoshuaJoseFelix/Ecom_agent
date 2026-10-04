class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap=defaultdict(int)
        for val in nums:
            hashmap[val] +=1
        for i,n in hashmap.items():
            if n>1:
                return True 
           
        return False 