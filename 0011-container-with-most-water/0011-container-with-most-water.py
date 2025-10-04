class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r = len(height)-1
        result=0
        while l<r:
            min_height = min(height[l],height[r])
            area = min_height * (r-l)
            result = max(area,result)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return result

