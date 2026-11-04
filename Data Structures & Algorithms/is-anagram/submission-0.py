class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s) != len(t):
            return False
       
        s_chars = sorted(s)
        t_chars = sorted(t)
        n = len(s)
        for i in range(n):
            if s_chars[i] != t_chars[i]:
                return False
        
        return True