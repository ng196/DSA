class Solution(object):
    def largestAltitude(self, gain):
        total = 0 
        max_sum = 0 
        for i in gain:
            total +=i
            if max_sum <= total : max_sum = total 
        return max_sum