class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""

        for i in range(len(s)):
            j = len(s)
            while j > i:
                sub = s[i:j]
                if sub == sub[::-1]:
                    if len(sub) > len(max_pal):
                        max_pal = sub
                    break
                j -= 1

        return max_pal
