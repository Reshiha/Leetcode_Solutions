class Solution {
    public String removeOuterParentheses(String s) {
        int count1 = 0;
        int count2 = 0;
        int temp = 0;
        String res = "";
        for(int i=0;i<s.length();i++){
            char str1 = s.charAt(i);
            if(str1 == '('){
                count1 = count1 + 1;
            }
            else if (str1 == ')')
            {
                count2 = count2 + 1;
            }
            
            if(count1 == count2){
                res = res + s.substring(temp + 1, i);
                temp = i + 1;
            }
            
        }
        return res;
        
    }
}