class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num] +=1
        for i in range(len(nums) + 1):
            if hashmap[i] == 0:
                return i