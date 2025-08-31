class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        fun(1, k, n, ds, ans);
        return ans;
    }

    private void fun(int i, int k, int n, List<Integer> ds, List<List<Integer>> ans) {
        if (k == 0 && n == 0) {
            ans.add(new ArrayList<>(ds));
            return;
        }
        if (i > 9 || k < 0 || n < 0) return;

        // Pick the current number
        ds.add(i);
        fun(i + 1, k - 1, n - i, ds, ans);
        ds.remove(ds.size() - 1); // backtrack

        // Don't pick the current number
        fun(i + 1, k, n, ds, ans);
    }
}
