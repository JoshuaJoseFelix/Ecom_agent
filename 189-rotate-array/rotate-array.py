class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # Handle cases where k is larger than the length of the list
        k = k % len(nums)
        
        # Split the list into two parts using standard slicing
        # and reassign them back into nums in-place
        nums[:] = nums[-k:] + nums[:-k]
