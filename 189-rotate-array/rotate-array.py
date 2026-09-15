class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        arr = len(nums) - k

        list1 = nums[0:arr]
        list2 = nums[arr:]

        nums[:] = list2 + list1

        return nums
        