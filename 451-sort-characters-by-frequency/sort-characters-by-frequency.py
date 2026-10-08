class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap=defaultdict(int)
        for count in s:
            hashmap[count] += 1
        res = ""

        for key, freq in sorted(hashmap.items(), key=lambda x: x[1], reverse=True):
            res += key * freq
        return res