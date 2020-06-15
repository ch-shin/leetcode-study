class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            res.append(check_validity_one_part(get_row(board, i)))
            res.append(check_validity_one_part(get_col(board, i)))
            res.append(check_validity_one_part(get_subbox(board, i)))
        return all(res)


def get_row(board, i):
    return board[i]


def get_col(board, i):
    col = []
    for j in range(len(board)):
        col.append(board[j][i])
    return col


def get_subbox(board, k):
    subbox_array = []
    box_row = k // 3
    box_col = k % 3
    for i in range(3):
        for j in range(3):
            subbox_array.append(board[box_row * 3 + i][box_col * 3 + j])
    return subbox_array


def check_validity_one_part(part):
    exist_check = {}
    for element in part:
        if (element in exist_check) and (element != "."):
            return False
        else:
            exist_check[element] = True
    return True