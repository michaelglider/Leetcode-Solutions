#347. Top K Frequent Elements Problem Description:
#Given an integer array nums and an integer k, return the k most frequent elements.
#You may return the anwser in any order.

class solution(object):
    def topKFrequent(self, nums, k):

        #Initialize an empy dictionary that will be used to store the frequency of each element in nums
        count = {}

        #Create a list of empty lists, one for each possible frequency. The length of freq is "len(nums) + 1" because the max frequency an element can have is equal to the length of nums
        freq = [[] for i in range(len(nums) + 1)]

        #loop over each element in nums
        for n in nums:
            
            #increment the count in the dictionary for each element, if the element is not in the dictionary, then initialize it to 0
            count[n] = 1 + count.get(n, 0)
        
        #Iterate over each key-value pair in the count dictionary
        for n, c in count.items():

            #append each element to the list by their frequencies
            freq[c].append(n)

        #initialize an empty list which will store the final results
        res = []

        #iterate over the indices of 'freq' inreverse order
        for i in range(len(freq) -1, 0, -1):

            #iterate over the elements in 'freq' at index at index 'i', which are the elements with frequency 'i'
            for n in freq[i]:

                #append the current element to the results list
                res.append(n)

                #check if the length of "res" has reached k, if so return the results 'res'
                if len(res) == k:
                    
                    #return res
                    return res