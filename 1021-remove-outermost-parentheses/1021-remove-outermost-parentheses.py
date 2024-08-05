class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count1 = 0
        count2 = 0
        res = ""
        temp = 0
        for i,c in enumerate(s):
            if c == "(":
                count1 += 1
            elif c == ")":
                count2 += 1
            if count1 == count2:
                res += s[temp+1:i]
                temp = i + 1
        return res
        