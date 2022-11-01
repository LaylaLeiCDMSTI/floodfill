from doctest import OutputChecker
from operator import ne
from tkinter import EW, N
from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
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

    # Implement your code here.
    input_list = []
    for i in input_board:
        input_list.append(list(i))
    print(input_board)
    if input_list[x][y] == old: 
        input_list[x][y] = new 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0 and input_list[x-1][y] != '#':
            flood_fill(input_list, old, new, x-1, y)
        if y < len(input_list[x]) and input_list[x][y+1] != '#':
            flood_fill(input_list, old, new, x, y+1)
        if y > 0 and input_list[x][y-1] != '#':
            flood_fill(input_list, old, new, x, y-1)
        if x < len(input_list) and input_list[x+1][y] != '#':
            flood_fill(input_list, old, new, x+1, y)
  
    return input_list

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)


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