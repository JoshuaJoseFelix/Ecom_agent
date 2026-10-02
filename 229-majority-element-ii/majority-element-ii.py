class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hashmap={}  
        for val in nums:
           hashmap[val] = 1 + hashmap.get(val, 0)
        res=[]
        for n, c in hashmap.items():
            if c > len(nums) // 3:
                res.append(n)

        return res