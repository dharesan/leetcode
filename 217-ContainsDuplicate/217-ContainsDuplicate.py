# Last updated: 24/05/2025, 12:53:15
class Solution(object):
    def containsDuplicate(self, nums):
      hashset = set()

      for n in nums: 
        if n in hashset: 
          return True 
        hashset.add(n)
      
      return False
        