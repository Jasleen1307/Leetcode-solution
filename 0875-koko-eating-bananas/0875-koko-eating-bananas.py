class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            speed = (low + high) // 2

            totalHours = 0

            for pile in piles:
                hours = (pile + speed - 1) // speed
                totalHours += hours

            if totalHours <= h:
                high = speed - 1
            else:
                low = speed + 1

        return low           
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        