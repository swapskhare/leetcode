class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 0
        col = 0

        if len(s) == 1 or numRows == 1:
            return s

        row = 0
        col = 1

        rows = [[] for _ in range(numRows)]
        
        for c in s:

            rows[row].append(c)

            if row == 0:
                col = 1
            elif row == numRows - 1:
                col = -1
            
            row += col

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)
            


