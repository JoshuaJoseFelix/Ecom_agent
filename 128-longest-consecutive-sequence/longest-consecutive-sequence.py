class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for i in seen:
            if i - 1 not in seen:
                count = 1

                while i + count in seen:
                    count += 1

                res = max(res, count)

        return res