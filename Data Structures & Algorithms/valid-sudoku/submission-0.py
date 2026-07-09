class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()

        for i in range(len(board)):
            for j in range(len(board[i])):

                value = board[i][j]

                if value == ".":
                    continue 
                
                row = (value, "row", i)
                column = (value, "column", j)
                sub_box = (value, "sub_box", i // 3, j // 3)

                if row in seen or column in seen or sub_box in seen:
                    return False
                
                seen.add(row)
                seen.add(column)
                seen.add(sub_box)

        
        return True