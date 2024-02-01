#15. 3Sum Problem Description:
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
#i != j, i!= k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that 
#the solution must not contain duplicate triplets

class Solution(object):
    def threeSum(self, nums):

        #initialize an empty list
        res = []

        #sort the input array
        nums.sort()

        #loop through the input array and set a variable equal to each value
        for i, a in enumerate(nums):

            #if the element is greater than 0 and the value we are looking at is equal to that same value we continue on
            if i > 0 and a == nums[i - 1]:
                continue

            #make two pointers one at the beginning of the array and one at the end
            l = i + 1
            r = len(nums) - 1

            #while the left pointer is less than the right
            while l < r:

                #set three sum equal to the value of the index we are looking at and the two pointers
                threeSum = a + nums[l] + nums[r]

                #if the threeSum value is greater than 0
                if threeSum > 0:
                    
                    #decrement the right pointer
                    r -= 1
                
                #if the threeSum value is less than 0
                elif threeSum < 0:
                    
                    #increment the left pointer
                    l += 1
                
                #otherwise we append the numbers to the array of lists
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    #increment the left pointer
                    l += 1
        
        #return the resulting array of lists
        return res