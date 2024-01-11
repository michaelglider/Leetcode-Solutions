#.49 Group Anagrams Problem Description:
#Given an array of strings strs, group the anagrams together. You can return the anwser in any order.

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):

        #initialize a dictionary where each key will have a default value of an empty list
        res = defaultdict(list)

        #iterate through the strings:
        for s in strs:

            #initialize a list names count, that has 26 zeros. Each element of this list is intended to count the occurrences of each letter in the alphabet in the string s
            count = [0] * 26

            #iterate over each character c in the current string
            for c in s:

                #use the ASCII value of the character c, and subract it by the ASCII value of "a" to give us the index of c, then increment it by 1
                count[ord(c) - ord("a")] += 1

            #append the string s to the list corresponding to the key res[count], but convert count into a tuple because tuples are immutable
            res[tuple(count)].append(s)

        #return the values of the dictionary which will be a list of the strings that are anagrams of eachother
        return res.values()