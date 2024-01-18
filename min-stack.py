#155. Min Stack Problem Description:
#Design a stac that supports push, pop, top, and retrieving the
#minimum element in constant time

class MinStack(object):

    def __init__(self):

        #initiate an empty array list that will we will use as a stack
        self.stack = []

        #initiate an empty arraylist that will be used to track the minimum value
        self.minStack = []

    def push(self, val):

        #append the value "val" to the stack when this function is called
        self.stack.append(val)

        #update val to be equal to the minimum of itself or the top value of the minStack if minStack is non-empty, otherwise just use val
        val = min(val, self.minStack[-1] if self.minStack else val)

        #append the value to minStack to make sure the smallest value is on top of minStack
        self.minStack.append(val)

    def pop(self):
        
        #use the build in python functions
        self.stack.pop()

        self.minStack.pop()
    
    def top(self):

        #return the last element in the array list
        return self.stack[-1]
    
    def getMin(self):

        #return the last element in the minStack array list
        return self.minStack[-1]