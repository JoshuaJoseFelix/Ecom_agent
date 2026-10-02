from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num] +=1
        res=0
        for n,c in hashmap.items():
            if c > res:
                res = c
                ans = n

        return ans

