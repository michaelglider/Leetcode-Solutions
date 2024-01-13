#238. Product of Array Except Self Problem Description:
#Given an integer array nums, return an array anwser such that anwser[i]
#is equal to the product of all the elements of nums except nums[i]

class solution(object):
    def productExceptSelf(self, nums):

        #create an integer array with all ones that is the size of the input array
        res = [1] * (len(nums))

        #initialize the prefix value as 1
        prefix = 1

        #iterate through the input array nums
        for i in range(len(nums)):

            #set all values in the results array as the prefix
            res[i] = prefix

            #update the value of the prefix for the next iteration
            prefix *= nums[i]
        
        #initialize the postifix value as 1
        postfix = 1

        #iterate through the array backwards
        for i in range(len(nums) - 1, -1, -1):
            
            #multiply the values in the results array by the postfix value
            res[i] *= postfix
            
            #update the postfix value for the next iteration
            postfix *= nums[i]
        
        #return the results array as the anwser
        return res