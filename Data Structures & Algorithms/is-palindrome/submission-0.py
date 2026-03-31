class Solution:
    def isPalindrome(self, s: str) -> bool:
         i = 0
         j = len(s) - 1
         while(i<j):
            if (s[i] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
                i+=1
                continue
            if (s[j] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
                j-=1
                continue
            if ((s[i] == s[j]) or (s[i] == s[j].upper()) or (s[i] == s[j].lower())):
                i+=1
                j-=1
            else:
                return False
         return True