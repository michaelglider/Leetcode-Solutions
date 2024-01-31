#167. Two Sum II - Input Array is Sorted Problem Description:
#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find to numbers such that they add up to a specific target number. let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length
#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2
#The tests are generated such that there is exactly one solution. you may not use the same element twice.

class Solution(object):
    def twoSum(self, numbers, target):
        
        #initiate two pointers left and right
        l = 0
        r = len(numbers) - 1

        #while the left pointer is less than the right
        while l < r:

            #set the current sum equal to the sum of the values where each pointer is indexed at
            curSum = numbers[l] + numbers[r]

            #if the current sum calculated is greater than the target then we move the right pointer to the left to look at lower values
            if curSum > target:
                r -= 1
            
            #if the current sum calculated is less than the target then we move the left pointer to the right to look at greater values
            if curSum < target:
                l += 1
            
            #otherwise we just return the indeces calulated and add 1 to each because of the problem describing the indexing added by one
            else:
                return[l + 1, r + 1]
        
        #return an empty array if we do not find any elements that add to the target
        return []