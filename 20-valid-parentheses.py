#20. Valid Parentheses Problem Desctiption:
#Given a string s containing just the characters '(', ')', '['. ']', '{', '}'
#determine if the input string is valid

class Solution(object):
    def isValid(self, s):

        #initiate a stack to store the input string
        stack = []

        #create a dictionary that maps each closing bracket as the key, and each opening bracket as the value pair
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        #iterate through each character in the input string "s"
        for c in s:

            #if the character is a closing bracket by seeing if it is in the dictionary
            if c in closeToOpen:

                #check whether the stack is not empty and that the last element in the stack is the matching opening bracket for c
                if stack and stack[-1] == closeToOpen[c]:

                    #if so then remove the last element from the stack
                    stack.pop()

                #otherwise the stack is empty or the last element in the stack is not the matching opening bracket for c
                else:
                    return False
                
            #if the current character c is not a closing bracket, then it is assumed to be an opening bracket and added to the stack
            else:
                stack.append(c)
            
        #return true if the stack is empty which means all opening brackets were properly closed and matched. Otherwise false which means there are unmatched opening brackets still int he stack
        return True if not stack else False
