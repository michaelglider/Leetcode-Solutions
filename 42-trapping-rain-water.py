#42. Trapping Rain Water Problem Description:
#Given n non-negative integers representing an elevation map
#where the width of each bar is 1, compute how much water it can
#trap after raining

class Solution(object):
    def trap(self, height):

        #if the input array is empty, then just return 0
        if not  height:
            return 0
        
        #initiate left and right pointers
        l = 0
        r = len(height)

        #initiate variables to keep track of the max right and left heights
        leftMax = height[l]
        rightMax = height[r]

        #iniate a variable to keep track of the amount of water to return
        res = 0

        #while the left pointer position is greater than the right pointer positon
        while l < r:

            #if the leftMax variable is less than the rightMax variable
            if leftMax < rightMax:

                #iterate the left pointer
                l += 1

                #update the leftMax variable if the new position has a greater height than the left pointer
                leftMax = max(leftMax, height[l])

                #update the result variable with the difference between the leftMax variable and the height we are looking at on the left
                res += leftMax - height[l]
            
            #otherwise we decrement the right pointer
            else:
                r -= 1

                #update the rightMax variable if the new positiion has a greater height than the right pointer
                rightMax = max(rightMax, height[r])

                #update the res variabkle with the difference between the rightMax variable and the height we are looking at on the right
                res += rightMax - height[r]
            
            #return the res varible which keepts track of how much water can be stored
            return res