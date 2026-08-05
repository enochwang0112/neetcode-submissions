class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row[i]:
                    return False
                if board[i][j] in col[j]:
                    return False

                box_row = i // 3
                box_col = j // 3
                index = box_row * 3 + box_col

                if board[i][j] in box[index]:
                    return False
                
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[index].add(board[i][j])
        
        return True
