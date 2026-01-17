class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        
        for i in range(0,len(s)):
            h={}
            for j in range(i,len(s)):
                if s[j] in h:
                    break
                    if maxLen<len(h):
                        maxLen = len(h)
                    h={}
                h[s[j]] = 1
                maxLen = max(maxLen,len(h))
              
        return maxLen


        