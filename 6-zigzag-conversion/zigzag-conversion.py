class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        mat = [[] for _ in range(numRows)]
        c = 0

        while c < len(s):
            
            for i in range(numRows):
                if c >= len(s):
                    break
                mat[i].append(s[c])
                c += 1

            # diagonal up
            for i in range(numRows - 2, 0, -1):
                if c >= len(s):
                    break
                mat[i].append(s[c])
                c += 1

        ans = ""
        for i in range(numRows):
            ans += "".join(mat[i])

        return ans
