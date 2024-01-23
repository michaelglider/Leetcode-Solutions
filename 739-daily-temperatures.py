#739 Daily Temperatures Problem Description:
#Given an array of integers temperatures represents the daily temperatures, return an array anwser
#such that anwser[i] is the number of days you have to wait after the ith day to get a warmer tamperature.
#If there is no future day for which this is possible, keep anwser == 0 instead.

class Solution(object):
    def dailyTemperatures(self, temperatures):

        #create an array the size of the inputer array "temperatures"
        res = [0] * len(temperatures)

        #create a stack
        stack = []

        #iterate through the input array and keep track of each value (i = index, t = value)
        for i, t in enumerate(temperatures):

            #while there are elements in the stack, and the current temperature(t) is greater than the temperature at the top of the stack
            while stack and t > stack[-1][0]:

                #pop the top element from the stack and store it in stackT and stackInd
                stackT, stackInd = stack.pop()

                #calulate the number of days until a warmer day temp is found by subtracting the index of the temp from stackInd and the current index, then store it in the res list at position 'stackInd'
                res[stackInd] = (i - stackInd)
            
            #add the current temperature adn its index as a pair to the top of the stack
            stack.append([t, i])
        
        #return the res list
        return res