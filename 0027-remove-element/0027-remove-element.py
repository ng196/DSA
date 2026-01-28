class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        move = []
        arr = nums
        for i in range(len(arr)):
            if arr[len(arr)-1-i] != val:
                move.append(arr[len(arr)-1-i])
            
        n = len(arr)
        k = len(move)
    
        for i in range(k):
            arr[i] = move.pop()
        
        for i in range(k, n):
            arr[i] = 0

        return k