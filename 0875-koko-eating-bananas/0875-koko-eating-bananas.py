from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total = sum(piles)
        # Binary search k = 1..n to find the value whereby total/k <= h
        # Write a helper function to calculate total/k <= h

        def isPossible(rate: int) -> bool:
            time_taken = 0
            for pile in piles:
                time_taken += ceil(pile / rate)
            return time_taken <= h
        
        # max speed is max(piles) because eating every pile would take 1hour
        low, high = 1, max(piles)
        while low < high:
            print(low, high)
            mid = (low + high) // 2
            print("mid", mid)
            if isPossible(mid):
                high = mid
            else:
                low = mid + 1
        return low
        