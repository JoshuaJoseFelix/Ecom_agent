class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st=[]
        s=("+-/*")

        for i in tokens:
            if i not in s:
                st.append(int(i))
            else:
                # First popped = right operand
                n1 = st.pop()

                # Second popped = left operand
                n2 = st.pop()

                if i == "+":
                    st.append(n2 + n1)

                elif i == "-":
                    st.append(n2 - n1)

                elif i == "*":
                    st.append(n2 * n1)

                else:
                    st.append(int(n2 / n1))

        return st[-1]