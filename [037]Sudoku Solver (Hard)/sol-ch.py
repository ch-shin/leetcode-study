import numpy as np


# To solve this problem as exact cover problem, I refered following references.
# https://en.wikipedia.org/wiki/Exact_cover
# https://www.geeksforgeeks.org/exact-cover-problem-algorithm-x-set-1/
# https://medium.com/optima-blog/solving-sudoku-fast-702912c13307
# https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.board = board
        condition_mat = self.initialize_condition_mat()
        # preprocessing to apply algorithm X
        X = {}  # key: col, values: nonzero index in the col
        Y = {}  # key: row, values: nonzero index in the row
        for r in range(condition_mat.shape[0]):
            Y[r] = set(np.where(condition_mat[r] == 1)[0])
        for c in range(condition_mat.shape[1]):
            X[c] = set(np.where(condition_mat[:, c] == 1)[0])

        # convert given sudoku numbers
        solution = []
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    r = row * 81 + col * 9 + int(board[row][col]) - 1
                    X, cols = select(X, Y, r)
                    solution.append(r)

        # solve
        solution = solve(X, Y, solution)
        print(len(solution))
        for r in solution:
            row = r // 81
            col = (r // 9) % 9
            val = r % 9 + 1
            board[row][col] = str(val)

    def initialize_condition_mat(self):
        NUM_ROWS = 9 * 9 * 9  # row: ((9 * 9 boards) 9 numbers,
        NUM_COLS = 4 * 9 * 9  # col: ((9 * 9)* 4 constraints)
        condition_mat = np.zeros((9 * 9 * 9, 4 * 9 * 9))
        for i in range(9 * 9 * 9):
            row = i // 81
            col = (i // 9) % 9
            val = i % 9

            # Constraint 1
            # Row-Column: Each intersection of a row and column, i.e, each cell, must contain exactly one number.
            condition_mat[i, row * 9 + col] = 1

            # Constraint 2
            # Row-Number: Each row must contain each number exactly once.
            condition_mat[i, 81 + row * 9 + val] = 1

            # Constraint 3
            # Column-Number: Each column must contain each number exactly once.
            condition_mat[i, 81 * 2 + col * 9 + val] = 1

            # Constraint 4
            # Box-Number: Each box must contain each number exactly once
            box = get_box(row, col)
            condition_mat[i, 81 * 3 + 9 * box + val] = 1
        return condition_mat


def get_box(row, col):
    if row < 3:
        if col < 3:
            box = 0
        elif col < 6:
            box = 1
        else:
            box = 2
    elif row < 6:
        if col < 3:
            box = 3
        elif col < 6:
            box = 4
        else:
            box = 5
    else:
        if col < 3:
            box = 6
        elif col < 6:
            box = 7
        else:
            box = 8
    return box


# # Algorithm X, mainly refered https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html
def solve(X, Y, solution):
    if len(X.keys()) == 0:
        return list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            X, cols = select(X, Y, r)
            sub_solution = solve(X, Y, solution)
            if sub_solution is not None:  # depth-first search success!
                return solution
            else:  # depth-first search failed. Restore X, Y, solution
                X = deselect(X, Y, r, cols)
                solution.pop()


def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return X, cols


def deselect(X, Y, r, cols):
    for j in reversed(list(Y[r])):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)
    return X
