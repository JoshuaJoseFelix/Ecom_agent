class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            sorted_s= tuple(sorted(s))
            hashmap[sorted_s].append(s)

        return list(hashmap.values())