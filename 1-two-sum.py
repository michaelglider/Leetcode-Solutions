#1. Two Sum Problem Description:
#Given an array of integers nums and an integer target, return indices of the two numbers such
#that they add up to target. You may assume that each input would have exactly one solution,
#and you may not use the same element twice.

class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #initiate a dictionary
        prevMap = {}

        #iterate throuugh the nums array
        #i = index, n = value
        for i, n in enumerate(nums):

            #make a variable that is the difference between the target and the current element
            diff = target - n
            
            #if the difference between the target and current element is in the dictionary, then we can return the indices of each element
            if diff in prevMap:
                #return the indice of the element that is equal the difference of the current and target, and return the current indice
                return [prevMap[diff], i]
            
            #if the variable diff is not found in the dictionary, then add it to the dictionary
            prevMap[n] = i
             