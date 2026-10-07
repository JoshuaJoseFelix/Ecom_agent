class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] != 0:
                l += 1
                r += 1

            elif nums[r] == 0:
                r += 1

            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1