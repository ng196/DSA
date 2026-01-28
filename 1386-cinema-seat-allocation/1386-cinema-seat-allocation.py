class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        z1 = set()
        z21 = set()
        z22 = set()
        z3 = set()
        affected_rows = set()

        for i in reservedSeats:
            affected_rows.add(i[0])
            if i[1] in [2, 3]:
                z1.add(i[0])
            if i[1] in [4, 5]:
                z21.add(i[0])
            if i[1] in [6, 7]:
                z22.add(i[0])
            if i[1] in [8, 9]:
                z3.add(i[0])
        
        k = (n - len(affected_rows)) * 2
        
        for i in affected_rows:
            left = i not in z1 and i not in z21
            right = i not in z22 and i not in z3
            mid = i not in z21 and i not in z22
            
            if left and right:
                k += 2
            elif left or right or mid:
                k += 1
                
        return k