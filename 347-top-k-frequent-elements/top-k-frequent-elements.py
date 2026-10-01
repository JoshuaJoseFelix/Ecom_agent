from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}                                      # number → frequency
        freq = [[] for i in range(len(nums) + 1)]       # index → frequency

        for n in nums:
            count[n] = 1 + count.get(n, 0)              # count n

        for n, c in count.items():
            freq[c].append(n)                            # put n in bucket

        res = []

        for i in range(len(freq) - 1, 0, -1):            # high → low frequency
            for num in freq[i]:                          # numbers with freq i
                res.append(num)

                if len(res) == k:
                    return res                           # got k numbers