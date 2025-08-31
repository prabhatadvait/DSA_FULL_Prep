import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        fun(0,ans,target,ds,candidates);
        return ans;
    }

    private void fun(int ind,List<List<Integer>> ans,int target,List<Integer> ds,int[] candidates){
        if(ind==candidates.length){
            if(target==0){
                ans.add(new ArrayList<>(ds));
            }
            return;
        }

        if(candidates[ind]<=target){
            ds.add(candidates[ind]);
            fun(ind,ans,target-candidates[ind],ds,candidates);
            ds.remove(ds.size()-1);
        }
        fun(ind+1,ans,target,ds,candidates);
    }
}