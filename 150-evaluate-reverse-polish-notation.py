#150. Evaluate Reverse Polish Notation Problem Description:
#You are given ana rray of strings tokens that represent an arithmetic expressrion in reverse polish notation.
#Evaluate the expression. Return an integer that represents the value of the expression.

class Solution(object):
    def evalPRN(self, tokens):

        #initiate a stack that will be used to store values
        stack = []

        #iterate over the elements in the input array tokens
        for c in tokens:

            #if the element we are at is an addition symbol, then we perform addition on the last 2 elements and add the sum to the stack
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            
            #if the element we are at is a subtraction symbol, perform subraction on the last 2 elements and add the difference to the stack
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            
            #if the element we are at is a multiplication symbol, perform multiplication on the last 2 elements and add the product to the stack
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            #if the element we are at is a divide symbol, perform division on the last 2 elements and add the quotient to the stack
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(b/a)
            
            #if the element we are at is not an operator, convert it to an integer and add it to the stack
            else:
                stack.append(int(c))
            
        #return the element that is left in the stack as it will be the anwser to the problem
        return stack[0]
    
            