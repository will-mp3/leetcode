"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            # got through if statements, character found
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1))

            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False

"""
this solution is a brute force backtracking solution that utilizes a depth first search recursive funciton.
the way it works is by going through the entire matrix and calling the dfs on each cell.
what that does is checks if that cell is the character we are looking for, and if so calls the dfs again on all of its neighbors.
this function continues until either the word is found (i == len(word)) or the all cells are checked and the word is not found.
if ever found, true will be returned.
otherwise it will return false.
"""