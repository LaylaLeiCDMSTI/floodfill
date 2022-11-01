from itertools import count
from typing import List
import sys
from unittest.util import _count_diff_all_purpose
sys.setrecursionlimit(50000)

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#.............##..",
    "....###############...",
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
    countlist = []
    if input_board[x][y] == old:
        input_board[x] = input_board[x].split("#")
        print(input_board[x])
        if len(input_board[x]) !=1:
            for i in range(len(input_board[x])):
                if input_board[x][i] != '':
                    countlist.append(i)
            print(countlist)
            countlist.remove(countlist[0])
            countlist.remove(countlist[len(countlist)-1])
            print(countlist)
            for n in countlist:
                input_board[x][n] = new * len(input_board[x][n])
        input_board[x] = '#'.join(input_board[x])
        #print(input_board)
        #input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
        flood_fill(input_board=input_board, old=old, new=new, x=x-1, y=y)

        #flood_fill(input_board=input_board, old=old, new=new, x=x, y=y+1)
        
        #flood_fill(input_board=input_board, old=old, new=new, x=x, y=y-1)

        flood_fill(input_board=input_board, old=old, new=new, x=x+1, y=y)

    return input_board

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)