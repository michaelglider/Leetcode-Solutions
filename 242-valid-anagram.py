#242 Valid Anagram Problem Description:
#Given two strings s and t, return true if t is an anagram of s, and false if otherwise.

class Solution(object):
    def isAnagram(self, s, t):

        #check if the lengths of both strings are the same, if they are not then return false because they cannot be anagrams
        if len(s) != len(t):
            return False
        
        #initiate two dictionaries that we will fill with the contents of both strings
        countS = {}
        countT = {}

        #loop over the length of the string s
        for i in range(len(s)):

            #For each character in both strings, increment the count in the dictionaries, use the get() method to handle characters that have not been encountered and initialize their count to 0
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #iterate over each chatacter in the countS dictionary
        for c in countS:

            #if the count of any character in s doesn't match the count in t, then return false
            if countS[c] != countT.get(c, 0):
                return False
        
        #return true because the strings have identical character counts for each unique character
        return True
