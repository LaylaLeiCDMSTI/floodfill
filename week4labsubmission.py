from doctest import OutputChecker
from operator import ne
from tkinter import EW, N
from typing import List



def print_board(board):
    for row in board:
        print(''.join(row))


def flood_fill(board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    #print_board(input_list)
    # Implement your code here.
    if board[x][y] == old: 
        board[x][y] = new 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0 and board[x-1][y] != '#':
            flood_fill(board, old, new, x-1, y)
        if y < len(board[x])-1 and board[x][y+1] != '#':
            flood_fill(board, old, new, x, y+1)
        if y > 0 and board[x][y-1] != '#':
            flood_fill(board, old, new, x, y-1)
        if x < len(board)-1 and board[x+1][y] != '#':
            flood_fill(board, old, new, x+1, y)


def make_board(input):
    board = []
    for i in input:
        board.append(list(i))
    return board

board1 = make_board([
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
])

flood_fill(board1, old=".", new="~", x=1, y=1)
print_board(board1)


#for a in modified_board:
#   print(a)


# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

#This is a comment
