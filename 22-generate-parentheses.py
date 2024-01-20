class Solution(object):
    def generateParenthesis(self, n):

        #make a stack for storing the parentheses
        stack = []

        #make an array list to return the resulting strings
        res = []

        #create a recursive function that will use backtracking to generate all valid parentheses combinations
        #OpenN and closedN are counters for the number of open and closed parentheses
        def backtrack(openN, closedN):

            #base case for the recursion, if the count of both open and closed partnehteses reaches n
            if openN == closedN == n:

                #append the resulting string to the res array list
                res.append("".join(stack))

                #end the current call of the function
                return
            
            #if the count of open is less than the input value of n
            if openN < n:

                #add an open paranthese to the stack
                stack.append("(")

                #recursively call the backtrack function with an incremented openN value
                backtrack(openN + 1, closedN)

                #pop the last element from the stack to backtrack
                stack.pop()
            
            #if the count of closing parentheses is less than the count of opening parentheses
            if closedN < openN:

                #append a closing parenthese to the stack
                stack.append(")")

                #recursively call the backtrack function with an incrmented closedN value
                backtrack(openN, closedN + 1)

                #pop the last element from the stack to backtrack
                stack.pop()
            
            #call the backtrack function with initial values of 0 too serve as a staring point where it represents the state where no parentheses have been added yet
            backtrack(0, 0)

            #return the resulting array list
            return res