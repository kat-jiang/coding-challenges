import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #use binary search from k = 1 to max of piles
        #get mid of l and r pointer
        #iterate through piles to calculate # of hours to eat
        #if num hours to eat is < h:
            #move r pointer to mid - 1
        #if num hours to eat is > h:
            #move l pointer to mid + 1
        #if same then return k
        #otherwise keep iterating until l >= r and return best k
        
        l, r  = 1, max(piles)
        k = r
        
        while l <= r:
            mid = (l + r) // 2
            total_hours = 0
            
            for p in piles:
                total_hours += math.ceil(p/mid)
                
            if total_hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return k
            