class Solution:
    def secondHighest(self, s: str) -> int:
        digits = [int(c) for c in s if c.isdigit()]
        unique_digits = sorted(set(digits))
        
        if len(unique_digits) < 2:
            return -1
            
        return unique_digits[-2]