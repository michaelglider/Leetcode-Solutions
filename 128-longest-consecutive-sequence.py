#.128 Longest Consecutive Sequence Problem Description:
#Given an unsorted array of integers nums, return the length of the
#longest consecutive elements sequence

def longestConsecutive(self, nums):

    #put the input array into a set
    numSet = set(nums)

    #initiate longest variable which will be used to store the anwser
    longest = 0

    #iterate through the array of numbers
    for n  in nums:

        #if the number we are evaluating does not have one less than itself
        #it can possibly be the start of a sequence
        if (n - 1) not in numSet:

            #initiate a variable to track the lenght of the sequence
            length = 0

            #check if the current number is in the array, and iterate through to see if the next number is also in the array
            while (n + length) in numSet:
                
                #increment length for the sequence
                length += 1
            
            #update the potential longest variable
            longest = max(length, longest)
        
        #return the output
        return longest
