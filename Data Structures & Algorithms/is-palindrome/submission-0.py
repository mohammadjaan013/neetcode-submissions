class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        t = ''.join(char.lower() for char in s if char.isalnum())
        r = len(t) - 1  
        while(l<r):
            if(t[l] == t[r]):
                l+=1
                r-=1
            else:
                return False
        return True
        