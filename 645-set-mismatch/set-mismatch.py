class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num] +=1
        res=[]
        duplicate,missing=0,0
        
        for i in range(1, len(nums) + 1):
            if hashmap[i] == 2:
                duplicate = i
            elif hashmap[i] == 0:
                missing = i

        return [duplicate, missing]