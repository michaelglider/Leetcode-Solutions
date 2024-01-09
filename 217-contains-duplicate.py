#217. Contains Duplicate Problem Description:
#Given an integer array nums, return true if any value appears at least twice
#in the array, and return false if every element is distinct

class Solutions(object):
    def containsDuplicate(self, nums):
        #create a hashset
        hashset = set()

        #use a for loop to go through the array
        for n in nums:
            #check if n is already in the hashset, and if so return true meaning there is a duplicate in the array
            if n in hashset:
                return True
            #if n is not in the hashset, then add it to the hashset
            hashset.add(n)
        #if gone through the array and no duplicates are found then return false
        return False
