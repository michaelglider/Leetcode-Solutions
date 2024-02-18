#33. Search in Rotated Sorted Array
#There is an integer array nums sorted in ascending order (with distinct values).
#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index. 
#Given the array nums after the possible rotation and an integer target, return the index of 
#if it is in nums or -1 if it is not in nums.

class Solution(object):
    def search(self, nums, target):

        #initiate two pointer for binary search
        l = 0
        r = len(nums) - 1

        #while the left pointer is less than or equal to the right pointer
        while l <= r:
            
            #set the middle pointer
            mid = (l + 2) // 2

            #if we have found the target which return the index
            if target == nums[mid]:
                return mid
            
            #if the left pointer value is less than or equal to the middle pointer value, we search the left sorted portion
            if nums[l] < nums[mid]:

                #if target is greater than the value of the middle pointer or target is less than the value of the left pointer
                if target > nums[mid] or target < nums[l]:
                    
                    #set the left pointer to the right of the middle pointer to look at the right section
                    l = mid + 1
                
                #otherwise set the right pointer to the left of the middle pointer to look at the left section
                else:
                    r = mid - 1
                
            #if the left pointers value is greater than or equal the middle pointers value
            else:

                #if the target value is less than the middle pointer value or the target value is greater than the right pointer value
                if target < nums[mid] or target > nums[r]:

                    #set the right pointer to the left of the middle pointer to look at the left section
                    r = mid - 1
                
                #otherwise
                else:
                    
                    #set the left pointer to the right of the middle pointer to look at the right section
                    l = mid + 1
                
        #if target is not in the array then we just return -1
        return -1