class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        n = len(nums)
        nums.sort()

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return

            if cur_sum > target or i == n:
                return

            # Include current number
            sol.append(nums[i])
            backtrack(i + 1, cur_sum + nums[i])

            # Backtrack
            sol.pop()

            # Skip duplicates
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            # Exclude current number
            backtrack(i + 1, cur_sum)
        backtrack(0, 0)
        return res