class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        int n = nums.length;
        fun(0,result,ds,nums,n);
        return result;
    }

    private void fun(int ind,List<List<Integer>> result,List<Integer> ds,int[] nums,int n){
        if(ind ==n){
            result.add(new ArrayList<>(ds));
            return;
        }

        //Include
        ds.add(nums[ind]);
        fun(ind+1,result,ds,nums,n);
        ds.remove(ds.size()-1);

        //Not Include
        fun(ind+1,result,ds,nums,n);
    }
}