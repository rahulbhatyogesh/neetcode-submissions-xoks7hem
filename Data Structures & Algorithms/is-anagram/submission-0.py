class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        import string
        alphadict1 = {ch: 0 for ch in string.ascii_lowercase}
        alphadict2 = {ch: 0 for ch in string.ascii_lowercase}

        for i in range(len(s)):
            alphadict1[s[i]] += 1
            alphadict2[t[i]] += 1
        
        for i in range(26):
            if alphadict1[chr(ord('a') + i)] != alphadict2[chr(ord('a') + i)]:
                return False
        
        return True