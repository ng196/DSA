class Solution(object):
    def asteroidCollision(self, asteroids):
        arr = []
        n = len(asteroids)

        def remove(i, arr):
            while len(arr) > 0:
                N = len(arr)
                last = arr[N-1]
                
                if last < 0:
                    break
                
                if last == i:
                    arr.pop()
                    return
                
                if last > i:
                    return

                if last < i:
                    arr.pop()
            
            arr.append(-1 * i)

        for i in range(n):
            val = asteroids[i]
            if val < 0:
                remove(abs(val), arr)
            else:
                arr.append(val)
        return arr