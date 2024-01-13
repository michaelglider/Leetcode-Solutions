from collections import defaultdict

#36. Valid Sudoku Problem Description
#Determine if a 9x9 Sudoku board is valid.
#Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):

        #initialize hashsets for the columns
        cols = defaultdict(set)

        #initialize hashset for the rows
        rows = defaultdict(set)

        #initialize hashset for the squares (3x3) inside of the board (9x9)
        squares = defaultdict(set)

        #iterate through the rows
        for r in range(9):
            #iterate through the columns
            for c in range(9):

                #check if the space is empty and if so, just continue to the next position
                if board[r][c] == ".":
                    continue

                #check if we have found a duplicate, if we did then we need to return false
                #if the current number is already inside the current row, then it means it is a duplicate
                if (board[r][c] in rows[r] or
                    
                    #or if the current number is already inside the current columns, then it means it is a duplicate
                    board[r][c] in rows[c] or
                    
                    #or if the current number is already inside of the current square (3x3), then it means it is a duplicate
                    board[r][c] in squares[(r // 3, c // 3)]):

                    #return false if the conditions have been met, meaning it is a duplicate
                    return False
                
                #continue, and update the hashmaps we made above
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        #return true since all the conditions are valid
        return True