#704. Binary Search Problem Description:
#Given an array of integers nums which is sorted in ascending order,
#and an integer target, write a function to search terget in nums. If 
#target exists, then return its index. Otherwise, return -1.

class Solution(object):
    def search(self, nums, target):

        #initiate left and right pointers
        l = 0
        r = len(nums) - 1

        #while the left pointer is less than or equal to the right pointer
        while l <= r:

            #initiate a middle variable to be the value at the middle of the input array
            m = (l + r) // 2

            #if the middle value is greater than the target
            if nums[m] > target:

                #set the right pointer equal to the the middle point
                r = m - 1
            
            #else if the middle value is less than the target
            elif nums[m] < target:
                
                #set the left pointer equal to the middle point
                l = m + 1
            
            #otherwise we have found the target and must return the middle point
            else:
                return m
        
        #if the target does not exist in the input array we return false
        return -1