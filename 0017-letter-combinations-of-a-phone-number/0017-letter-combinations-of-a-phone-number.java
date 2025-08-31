class Solution {
    public List<String> letterCombinations(String digits) {

        List<String> ans = new ArrayList<>();
        if (digits == null || digits.length() == 0) return ans;

        Map<Character, String> mapping = new HashMap<>();
        mapping.put('2', "abc");
        mapping.put('3', "def");
        mapping.put('4', "ghi");
        mapping.put('5', "jkl");
        mapping.put('6', "mno");
        mapping.put('7', "pqrs");
        mapping.put('8', "tuv");
        mapping.put('9', "wxyz");

        backtrack(0,ans,"", digits, mapping);
        return ans;
    }

    private void backtrack(int index,List<String> ans, String current, String digits, Map<Character, String> mapping) {
        if (index == digits.length()) {
            ans.add(current);
            return;
        }

        String letters = mapping.get(digits.charAt(index));
        for (char ch : letters.toCharArray()) {
            backtrack(index + 1,ans,current + ch, digits, mapping);
        }
    }
}