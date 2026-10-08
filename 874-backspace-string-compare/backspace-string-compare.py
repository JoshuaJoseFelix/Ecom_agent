class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_characters(s):
            st=[]
            for char in s:
                if char == '#' and st:
                    st.pop()
                elif char !='#':
                    st.append(char)
            return st
        return remove_characters(s) == remove_characters(t)