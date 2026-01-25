class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        k = 0 
        i = 0
        
        while i < n:
            if nums[i] == 0:

                while i < n and nums[i] == 0:
                    k += 1 
                    i += 1
            
            if i < n and k > 0:
                nums[i - k] = nums[i]
                

                nums[i] = 0
            
            i += 1
        
        return nums