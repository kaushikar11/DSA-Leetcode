# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLen = 0
        
#         for i in range(0,len(s)):
#             h={}
#             for j in range(i,len(s)):
#                 if s[j] in h:
#                     break
#                     if maxLen<len(h):
#                         maxLen = len(h)
#                     h={}
#                 h[s[j]] = 1
#                 maxLen = max(maxLen,len(h))
              
#         return maxLen


        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
