class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = len(s)
        if length <= 1:
            return s

        dp = [[False] * length for _ in range(length)]
        max_pal_length = 1
        start = 0
        for i in range(length):
            dp[i][i] = True
        
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_pal_length = 2

        for k in range(3, length + 1):
            for i in range(length - k + 1):
                j = i + k - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > max_pal_length:
                        start = i
                        max_pal_length = k

        return s[start: start + max_pal_length]

        
                
                        