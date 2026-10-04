class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reversed_number = int(str(x)[::-1])
        if x==reversed_number:
            return True

        return False