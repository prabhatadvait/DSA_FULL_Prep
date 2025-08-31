class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        Arrays.sort(candidates);
        fun(0,ans,target,ds,candidates);
        return ans;
    }

    private void fun(int ind,List<List<Integer>> ans,int target,List<Integer> ds,int[] candidates){
        if(target==0){
            ans.add(new ArrayList<>(ds));
            return;
        }
        for(int i=ind;i<candidates.length; i++){
            if(i > ind && candidates[i]==candidates[i-1])
                continue;
            if(candidates[i]>target){
                break;
            }

            ds.add(candidates[i]);
            fun(i+1,ans,target-candidates[i],ds,candidates);
            ds.remove(ds.size()-1);
        }
    }
}