# Last updated: 16/07/2025, 18:07:58
class Solution:
    def longestPalindrome(self, s: str) -> int:
        #store hashmap of all letters? O(n) time 
        
        a = Counter()
        for char in s: 
            a [char] += 1

        length = 0 
        hasOdd = False 

        for key in a: 
            if (a[key] % 2 == 0): # even 
                length += a[key]
            else: 
                length += a[key] - 1
                hasOdd = True 
        
        if hasOdd: 
            length += 1

        return length

        