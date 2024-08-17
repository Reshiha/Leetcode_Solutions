class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        StringBuilder new_text = new StringBuilder();
        for(char c:s.toCharArray())
        {
            if(Character.isLetterOrDigit(c))
            {
                new_text.append(c);
            }
        }
        int i = 0;
        int j = new_text.length() - 1;
        while(i < j)
        {
            if(new_text.charAt(i) != new_text.charAt(j))
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
        
    }
}