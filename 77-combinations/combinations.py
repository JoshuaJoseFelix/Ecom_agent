class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def backtracking(start,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start,n+1):
                comb.append(i)
                backtracking(i+1,comb)
                comb.pop()

        backtracking(1,[])
        return res