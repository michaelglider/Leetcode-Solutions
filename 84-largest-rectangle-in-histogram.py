#84. Largest Rectangle in Histogram Problem Descritption:
#Given an array of integers heights representing the histogram's bar height where 
#the width of each bar is 1, return the area of the largest rectangle in the histogram.

class Solution(object):
    def largestRectangleArea(self, heights):

        #initiate a variable to keep track of the max area
        maxArea = 0

        #initiate an empty stack
        stack = []

        #iterate through the input array of integers represnting heights and keep track of the index and value
        for i, h in enumerate(heights):
            
            #set a start variable equal to the index value
            start = i

            #while the stack is not empty and the last element in the stack is greter than current height
            while stack and stack[-1][1] > h:

                #set the index and height equal to the last element in the stack                
                index, height = stack.pop()

                #set the max variable equal to the max of either the already stored maxArea or the area of the last element in the stacks height and the length between the current index and the index of the last element added to the stack
                maxArea = max(maxArea, height * (i - index))

                #set the start variable equal the index of the last element on the stack
                start = index
            
            #add the value pair of the last index value on the stack  and current height we are at in the array
            stack.append((start, h))
        
        #iterate through the stack we created and keep track of the value pairs ()
        for i, h in stack:

            #update the max area to be equal to the already stores max area or the area of the hieght we are looking at in the stack by the difference between the length of the height array and the index in the stack we are currently at
            maxArea = max(maxArea, h * (len(heights) - i))
        
        #return the maxArea
        return maxArea