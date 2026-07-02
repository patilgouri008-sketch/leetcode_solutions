class Solution(object):
    def firstUniqChar(self, s):
     return next((i for i,c in enumerate(s) if s.index(c)==s.rindex(c)), -1)        