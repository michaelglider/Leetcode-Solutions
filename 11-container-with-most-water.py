#11. Containger With Most Water Problem Desctiption:
#You are given an integer array height of length n. There are n vertical lines drawn
#such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container
#contains the most water.
#Return the maximum amount of water a container can store

class Solution(object):
    def maxArea(self, height):
        
        #create a variable to store the max area
        res = 0

        #make left and right pointers
        l = 0
        r = len(height) - 1

        #while the left pointer is further left than the right pointer
        while l < r:
            
            #calclate the area by multiplying the difference between the left and right pointer and the minimum of heights each pointer is looking at
            area = (r - l) * min(height[l], height[r])

            #update the result variable with the max area which we will return
            res = max(res, area)

            #if the height of the left pointer is less than the right
            if height[l] < height[r]:

                #iterate the left pointer
                l += 1
            
            #otherwise decrement the right pointer
            else:
                r -= 1
            
        #return the result variable
        return res
    