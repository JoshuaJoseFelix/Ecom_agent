from collections import defaultdict 
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num] +=1
        for key,value in hashmap.items():
            if value == 1:
                return key
        