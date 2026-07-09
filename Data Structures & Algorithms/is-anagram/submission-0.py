class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        
        for c in t:
            if c not in m:
                return False
            m[c] = m.get(c, 0) - 1
            if m[c] < 0:
                return False
        
        return True
