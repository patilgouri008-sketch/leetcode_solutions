class Solution(object):
    def longestCommonPrefix(self, strs):
      
        return min(strs, key=len)[:next((i for i,c in enumerate(min(strs,key=len)) if any(s[i]!=c for s in strs)), len(min(strs,key=len)))]