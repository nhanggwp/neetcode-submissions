class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dict_row = {}
        dict_col = {}
        dict_box = {}

        m = len(board)
        n = len(board[0])
        number_box = (m * n ) // 9 

        for i in range(m):
            dict_row[i] = set()
        for i in range(n):
            dict_col[i] = set()
        
        for i in range(number_box):
           dict_box[i] = set()


        for i in range(m):
            for j in range(n):
                val = board [i][j]
                if val == ".":
                    continue
                box_id = (i // 3) * 3 + (j//3)
                if val in dict_box[box_id]:
                    return False
                if val in dict_row[i]:
                    return False
                if val in  dict_col[j]:
                    return False
                dict_box[box_id].add(val)
                dict_row[i].add(val)
                dict_col[j].add(val)

        return True
