class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hashmap = {}

        for n in nums2:
            while stack and n>stack[-1]:
                hashmap[stack.pop()] = n
            stack.append(n)
        for n in stack:
            hashmap[n] = -1

        return [hashmap[n] for n in nums1]