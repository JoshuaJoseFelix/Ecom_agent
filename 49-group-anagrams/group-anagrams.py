class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words=defaultdict(list)
        result=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            words[sorted_s].append(s)

        for i in words.values():
            result.append(i)

        return result

             