class Solution(object):
    def romanToInt(self, s):
        total=0
        values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i in range(len(s)-1):
            current=values[s[i]]
            next=values[s[i+1]]
            if current<next:
                total=total-current
            else:
                total=total+current
        total=total+values[s[-1]]
        return total            
        """
        :type s: str
        :rtype: int
        """
        