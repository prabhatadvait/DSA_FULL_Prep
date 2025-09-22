class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        suma=0
        for i in nums:
            suma+=i
            if suma>maxi:
                maxi = suma
            if(suma<0):
                suma=0
        return maxi