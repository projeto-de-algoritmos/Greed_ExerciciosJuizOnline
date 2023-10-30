from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  

        max_sum = 0
        curr_time = 0

        for s in satisfaction:
            if curr_time + s <= 0:
                break  
            curr_time += s
            max_sum += curr_time

        return max_sum