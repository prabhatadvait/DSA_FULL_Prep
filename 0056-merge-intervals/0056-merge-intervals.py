from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged is empty or no overlap, just append
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Overlapping intervals, merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
