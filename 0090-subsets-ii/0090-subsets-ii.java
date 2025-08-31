class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> ans = new ArrayList<>();
    Arrays.sort(nums); // sort to handle duplicates
    List<Integer> ds = new ArrayList<>();
    fun(0, ans, ds, nums);
    return ans;
}

private void fun(int ind, List<List<Integer>> ans, List<Integer> ds, int[] nums) {
    ans.add(new ArrayList<>(ds)); // add every subset at each step

    for (int i = ind; i < nums.length; i++) {
        if (i > ind && nums[i] == nums[i - 1]) continue; // skip duplicates

        ds.add(nums[i]);                  // choose
        fun(i + 1, ans, ds, nums);        // explore
        ds.remove(ds.size() - 1);         // backtrack
    }
}

}