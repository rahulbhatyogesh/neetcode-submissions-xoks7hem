class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {j: set() for j in range(9)}
        cols = {k: set() for k in range(9)}
        block = set()
        for i in [0,3,6]:
            for j in range(9):
                if (j%3 == 0):
                    block = set()
                for k in range(3):
                    if (board[i+k][j] == "."):
                        continue
                    if (board[i+k][j] in block):
                        return False
                    else:
                        block.add(board[i+k][j])
                        if (board[i+k][j] in rows[i+k]):
                            return False
                        else:
                            rows[i+k].add(board[i+k][j])
                        
                        if (board[i+k][j] in cols[j]):
                            return False
                        else:
                            cols[j].add(board[i+k][j])
        
        return True