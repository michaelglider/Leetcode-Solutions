#153. Find Minimum in Rotated Sorted Arrat
#Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
#For example, the array nums = [0, 1, 2, 3, 4, 5, 6, 7] might become:
#[4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times
#Given the sorted rotated array nums of unique elements, return the minimum element of this array.

class Solution(pbject):
    def findMin(self, nums):

        #initially set the result as the first value in the inputted array
        res = nums[0]

        #set the two pointer at each end of the input array
        l = 0
        r = len(nums) - 1

        #while the left pointer is to the left or on  the right pointer
        while l <= r:
            #if the value of the left pointer is less than the value of the right pointer
            if nums[l] < nums[r]:
                #the result is going to be the minimum of either whatever is already stored in res, or the value of the left pointer
                res = min(res, nums[l])
                #break out of the loop
                break

            #set the middle pointer
            m = (l + r) // 2

            #result is going to be the minimum of what is already stored in res, or the value of the middle pointer
            res = min(res, nums[m])

            #if the middle pointer is greater than or equal to the value of the left pointer
            if nums[m] >= nums[l]:
                #set the left pointer equal to the right of the middle pointer
                l = m + 1
            #otherwise
            else:
                #set the right pointer equal to the value left of the middle pointer
                r = m - 1

        #return the res variable when we break out of the loop
        return res