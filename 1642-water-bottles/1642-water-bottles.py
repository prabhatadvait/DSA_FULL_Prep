class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles 
        empty = numBottles
        
        while empty >= numExchange:
            new_bottles = empty // numExchange  
            ans += new_bottles                   
            empty = empty % numExchange + new_bottles
        
        return ans