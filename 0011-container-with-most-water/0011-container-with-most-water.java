import java.util.*;

class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int result = 0;

        while (l < r) {
            int minHeight = Math.min(height[l], height[r]);
            int area = minHeight * (r - l);
            result = Math.max(result, area);

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return result;
    }
}
