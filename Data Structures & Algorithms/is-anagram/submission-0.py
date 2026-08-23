class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_count = {}
        t_count = {}

        for x in s:
            s_count[x] = s_count.get(x,0) + 1

        for x in t:
            t_count[x] = t_count.get(x,0) + 1

        if s_count == t_count:
            return True
        else:
            return False