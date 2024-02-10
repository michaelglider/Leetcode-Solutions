#74. Search a 2D Matrix Problem Description:
#You are given an m x n integer matrix matrix weith the following to properties
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if targets is in matrix or false otherwise.

class Solution(object):
    def searchMatrix(self, matrix, target):

        #initiate a pointer for the # of rows in the matrix
        ROWS = len(matrix[0])
        
        #initiate a pointer for the # if columns in the matrix
        COLS = len(matrix)

        #initiate a pointer for the top of the matrix
        top = 0

        #initiate a pointer for the bottom of the matrix
        bot = ROWS - 1

        #while the top row pointer is less than or equal to the bottom row pointer
        while top <= bot:

            #calculate the middle row of the matrix
            row = (top + bot) // 2

            #if the target valus is greatyer than the value at the calculated rows last element
            if target > matrix[row][-1]:

                #set the top row pointer equal to the current row we are looking at 
                top = row + 1
            
            #else if the target is less than the current row we are looking at's first value
            elif target < matrix[row][0]:
            #set the bottom row pointer equal to the current row we are looking at
                bot = row - 1
            
            #otherwise we break out of this while loop
            else:
                break
        
        #if the top is not less than or equal to the bottom
        if not (top <= bot):

            #return False 
            return False
        
        #initiate a pointer for the left side of the matrix
        l = 0

        #initiate a pointer for the right of the matrix
        r = COLS - 1

        #while the left pointer is less than or equal to the right pointer
        while l <= r:

            #calculate the midddle value
            m = (l + r) // 2

            #if the target value is greater than the element we are looking at
            if target > matrix[row][m]:

                #set the left pointer equal to the middle value
                l = m + 1
            
            #else if the target value is less than the element we are looking at
            elif target < matrix[row][m]:

                #set the right pointer equal to the middle valie
                r = m - 1
            
            #other wise we have found the target value and we return True
            else:
                return True
        
        #is we did not return true, then we have not found the target value and must return False
        return False