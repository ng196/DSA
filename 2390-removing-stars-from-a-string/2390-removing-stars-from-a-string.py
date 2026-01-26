class Solution(object):
    def removeStars(self, s):
        arr = []
        
        for char in s:
            if char == '*':
                if arr:
                    arr.pop()
            else:
                arr.append(char)
        
        return "".join(arr)