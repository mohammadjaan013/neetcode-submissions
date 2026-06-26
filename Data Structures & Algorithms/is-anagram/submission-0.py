class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different; if so, they can't be anagrams
        if len(s) != len(t):
            return False

        mapS, mapT = {}, {}
        
        for i in range(len(s)):
            # Get current characters
            c1 = s[i]
            c2 = t[i]
            
            # Increment counts in mapS for c1 and in mapT for c2
            mapS[c1] = mapS.get(c1, 0) + 1
            mapT[c2] = mapT.get(c2, 0) + 1

        # Compare the dictionaries
        return mapS == mapT
