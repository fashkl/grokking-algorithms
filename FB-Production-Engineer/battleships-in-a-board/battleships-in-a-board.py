"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board.
In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
where k can be of any size. At least one horizontal or vertical cell separates between two battleships
(i.e., there are no adjacent battleships).

"""


# ["X",".","X","X"],
# [".",".",".","X"],
# [".",".",".","X"]

def count_battleships_2(board):
    ships = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            # check above and left
            if board[row][col] == 'X':
                if (row - 1 >= 0 and board[row - 1][col] == 'X') or (col - 1 >= 0 and board[row][col - 1] == 'X'):continue
                ships += 1

    return ships


def dfs(board, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'X': return

    # mark cell as visited
    board[row][col] = '.'

    # check adjacent
    dfs(board, row - 1, col)
    dfs(board, row + 1, col)
    dfs(board, row, col - 1)
    dfs(board, row, col + 1)


def count_battleships(board):
    ships = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'X':
                ships += 1
                dfs(board, row, col)

    return ships


print(count_battleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
print(count_battleships_2([["X", ".", "X", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
