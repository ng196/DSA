class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        k = 0 
        i = 0
        
        while i < n:
            if nums[i] == 0:
                # Count consecutive zeros
                # Added i < n check to prevent IndexError
                while i < n and nums[i] == 0:
                    k += 1 
                    i += 1
            
            # If we've found zeros (k > 0) and current i is a non-zero
            if i < n and k > 0:
                # Shift the non-zero element back by k positions
                nums[i - k] = nums[i]
                
                # Zero out the current position
                # This replaces your nested j-loop logic which was decrementing k
                nums[i] = 0
            
            i += 1
        
        return nums