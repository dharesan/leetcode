# Last updated: 24/05/2025, 12:53:17
class Solution(object):
    def isAnagram(self, s, t):
        # sorted(s) == sorted(t)
        """
        :type s: str
        :type t: str
        :rtype: bool

        # #add to hash set each letter of s 
        # #pop or remove from hash if each letter of t have 
        # #if hash empty return true, if hash still got letter return false

        # #doesnt cosider case if t got more letters than s  
        # """
        # """brute force method: cancel out each word: O(n2)"""
        # counterS, counterT = {}, {}
        # totalLengthS = len(s)
        # if totalLengthS == len(t): #first thing check for length equal or not
        #     #iterate through each s and store each alphabet as a key 
        #     for i in range(totalLengthS): # i is an index 
        #         counterS[s[i]]= 1 + counterS.get(s[i], 0)
        #         counterT[t[i]] = 1 + counterT.get(t[i], 0)

        #     for key in counterS: 
        #         if counterS[key] != counterT.get(key,0):
        #             return False
        # else: 
        #     return True 
        # return True  
        if len(s) != len(t): 
            return False 
        counterS, counterT = {},{} #create two dicts 
        for i in range(len(s)): #same length
            counterS[s[i]] = 1 + counterS.get(s[i],0)
            counterT[t[i]] = 1 + counterT.get(t[i],0) 
        for alphabet in s: 
            if counterS.get(alphabet) != counterT.get(alphabet): 
                return False 

        return True 


