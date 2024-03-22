# https://leetcode.com/problems/remove-outermost-parentheses/description/

class Solution:
    def _init_(self):
        self.indexes = []
    

    def removeOuterParentheses(self, s: str) -> str:
        hasil = ""

        for idx,  var in enumerate(s):
            if var == "(":
                
                self.indexes.append(idx)
            if var == ")":
                to_print = self.indexes.pop()

                if not len(self.indexes):  # Kalo "indexes" kosong
                    hasil += s[to_print+1 : idx]

        return hasil