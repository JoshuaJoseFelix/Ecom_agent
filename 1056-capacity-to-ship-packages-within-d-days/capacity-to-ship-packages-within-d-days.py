class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = sum(weights)
        def curr(m):
            ship,currcap =1,m 
            for w in weights:
                if currcap - w <0:  # checks weather the no is negative say w=5 and cap = 2  so 2-5 =-3 
                                    #new day starts
                    ship += 1    # new day
                    currcap=m  #reset that days cap 
                currcap -=w #remaining space available 
            return ship<=days

        while l<=r:
            m = (l + r)//2
            if curr(m): 
                res=min(res,m)
                r = m-1 
            else:
                 l = m + 1 
        return res