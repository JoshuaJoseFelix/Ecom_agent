class Solution:
    def reverseWords(self, s: str) -> str:
        rev=s.split()
        rev_word=[i[::-1]for i in rev]
        return ' '.join(rev_word)