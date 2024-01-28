#125. Valid Palindrome Problem Description:
#A phrase is a palindrome if, after converting all upercase letters into lowercase letters and removing 
#all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise

class Solution(object):
    def isPalindrome(self, s):

        #initiate an empty string to store the input string in reverse
        newStr = ""

        #iterate through the input string
        for c in s:

            #check if the element that we are looking at is alphanumeric
            if c.isalnum():

                #add the character to the empty string in lowercase
                newStr += c.lower()

        #return true if the string is the same as it is in reverse and false otherwise
        return newStr == newStr[::-1]
    

    #second solution:
    def isPalindrome2Pointer(self, s):
          
        #helper function that checks the askey value and returns true if the character is within the ranges of the askeys
        def alphaNum(self, c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        
        #initialize the pointers
        #end of the string
        r = len(s) - 1

        #beginning of the string
        l = 0

        #while the beginning pointer is less than the end pointer and alphanumeric
        while l < r:

            #while the end pointer is greater and alphanumeric
            while l < r and not self.alphaNum(s[l]):

                #iterate the beginning pointer
                l += 1
            
            #while the end pointer is greater and alphanumeric
            
            while r > l and not self.alphaNum(s[r]):

                #decrement the end pointer
                r -= 1
            
            #if the beginning and end pointers do not equal eachother return false
            if s[l].lower() != s[r].lower():

                #return false
                return False
            
            #iterate the left pointer
            l = l + 1

            #decrement the right pointer
            r = r - 1
        
        #return true if false was not returned
        return True
            