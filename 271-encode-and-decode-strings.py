#271. Encode and Decode Strings Problem Description:
#Design an algotithm to encode a list of strings to a string. The encoded string is
#then sent over the network and is decoded back to the original list of strings

class Solution(object):
    def encode(self, strs):

        #initiate an empty string
        res = ''

        #iterate through the input string "strs"
        for s in strs:

            #take then length of the string and convert it into a string
            #take the legnth of the string and add it to the begining of the string as well as a "#"
            res += str(len(s)) + "#" + s
        
        #return the resulting string 
        return res
    
    
    def decode(self, str):

        #initiate an empty list and a pointer with the value 0
        res, i = [], 0

        #while the pointer is still in bounds of the inputed string "str"
        while i < len(str):
            
            #initialize another pointer with the same value as i which will be used to find the position of the delimiter
            j = i
            
            #while the pointer j is not at a delimiter
            while str[j] != "#":

                #iterate j by 1 to the next character in the string
                j += 1
            
            #once the "#" is found, then we set the legth of that word equal to the length of i to j, not including j
            length = int(str[i:j])

            #append the segment whcih starts from j + 1 (the character imediately after "#") and spand the length variable
            res.append(str[j + 1 : j + 1 + length])

            #update i to the position after the end of the current string segment, which sets up i for the next iteration
            i = j + 1 + length
        
        #return the resulting decoded string
        return res