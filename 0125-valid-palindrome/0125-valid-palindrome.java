class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder filtered = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                filtered.append(Character.toLowerCase(c));
            }
        }
        
        // create reversed string
        String str = filtered.toString();
        String reversed = new StringBuilder(str).reverse().toString();
        
        // compare
        return str.equals(reversed);
    }
}
