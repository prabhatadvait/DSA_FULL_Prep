class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k%n;
        List<Integer> rotated = new ArrayList<>();
        for(int i=n-k;i<n;i++){
            rotated.add(nums[i]);
        }

        for(int i=0;i<n-k;i++){
            rotated.add(nums[i]);
        }

        for(int i=0;i<n;i++){
            nums[i] = rotated.get(i);
        }
    }
}