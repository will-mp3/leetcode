"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                # check for empty space
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

"""
for this problem we utilize hashsets to make checking for duplicates easier, it is also possible with arrays since we know its a 9x9 array.
to start we create hashsets for our rows, columns, and 3x3 squares within the board.
the board values are mapped using the column and row for rows and cols respectively and a special form of indexing for the squares.
the key for our squares hashset is acquired using integer division and maps all 9 squares as though they are coordinates.
for example, the top left square will have the key (0,0) which is acquired by integer dividing any of its row col indices by 3.
this is the same for the rest of them resulting in coordinates from (0,0) to (2,2).
once our hashsets are in place we can use a nested loop to traverse the entire 9x9 array.
as we traverse we check two things:
first, if the cell is empty (represented by a dot) in which case we continue to the next iteration without doing anything.
the next condition is if the cell is not empty.
in this case we check if the value is present in any of our hashsets, if so we return false.
if the value is not present we add it to all three sets using the correct key.
if the loop fully runs we return true.
this solution runs in O(9^2) time, which could be considered O(n^2) where n is the number of rows and columns.
"""