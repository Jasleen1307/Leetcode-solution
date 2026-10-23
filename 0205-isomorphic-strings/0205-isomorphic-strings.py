class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        map1={}
        map2={} 

        for i in range(len(s)):
            if s[i]  in map1 and map1[s[i]] != t[i]:
                return False
            if t[i] in map2 and map2[t[i]] != s[i]:
                return False
            map1[s[i]]=t[i]
            map2[t[i]]=s[i]
        return True           

        
        """
        :type s: str
        :type t: str
        :rtype: bool 
        """
        