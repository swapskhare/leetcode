class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diag, anti, cols):
            if row == n:
                return 1
            solutions = 0

            for col in range(n):
                curr_diag = row - col
                curr_anti = row + col

                if (col in cols or curr_diag in diag or curr_anti in anti):
                    continue
                
                cols.add(col)
                diag.add(curr_diag)
                anti.add(curr_anti)

                solutions+= backtrack(row+1, diag, anti, cols)
                cols.remove(col)
                diag.remove(curr_diag)
                anti.remove(curr_anti)

            return solutions
        return backtrack(0, set(),set(), set())