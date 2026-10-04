class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            freqs=defaultdict(int)
            l=0
            res=0
            for r in range(len(s)):
                words=s[r]
                freqs[words] +=1
                maxfreq = max(freqs.values())
                curr=r-l+1
                if curr-maxfreq>k:
                    freqs[s[l]] -=1
                    l +=1
                    curr=r-l+1

                res=max(res,curr)
            return res