class Solution(object):
    def maxNonOverlapping(self, nums, target):
        seen = {0}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            if (current_sum - target) in seen:
                count += 1
           
                seen = {0}
                current_sum = 0
            else:
                seen.add(current_sum)
                
        return count