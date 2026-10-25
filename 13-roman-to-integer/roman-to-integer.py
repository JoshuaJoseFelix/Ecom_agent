class Solution:
    def romanToInt(self, s: str) -> int:
        s_values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        for i in range(len(s)):
            if i + 1 < len(s) and s_values[s[i]] < s_values[s[i + 1]]:
                sum -= s_values[s[i]]
            else:
                sum += s_values[s[i]]
        return sum
            