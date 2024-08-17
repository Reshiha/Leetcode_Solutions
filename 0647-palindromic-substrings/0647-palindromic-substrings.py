class Solution:
    def countSubstrings(self, s: str) -> int:
        strs = []
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                strs.append(s[i:j])
        
        for char in strs:
            revs_char = ''.join(reversed(char))
            if char == revs_char:
                count += 1
        return count
                
        
        
        