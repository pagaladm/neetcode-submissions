class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch] +=1
        for ch in t:
            if ch not in freq:
                return False
            else:
                freq[ch]-=1
        for key in freq:
            if freq[key]!= 0:
                return False
            
        return True
            