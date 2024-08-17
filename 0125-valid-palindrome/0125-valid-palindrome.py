class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_text = ''.join(char for char in s if char.isalnum())
        if new_text == new_text[::-1]:
            return True
        else:
            return False


  
        
        