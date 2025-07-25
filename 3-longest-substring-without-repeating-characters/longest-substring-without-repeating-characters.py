class Solution:
  """below is the O(n^2) complexity algorithm """ 
    def lengthOfLongestSubstring(self, s: str) -> int:
        # DP?  
        # sliding window is O(n^2) worst case 
        # if not s: 
        #     return 0 

        # i cant sort since it has natural ordering 
        # if len(s) == 0: 
        #     return 0
        
        # maxLength = 1 
        # for i in range(len(s)-1):
        #     currStr = ""
        #     for j in range(i+1, len(s)): 
        #         if s[j] not in currStr: 
        #             currStr += s[j] 
        #         if len(currStr) > maxLength: 
        #             maxLength = len(currStr)
        # return maxLength


        

        ## can use sliding window with 2 pointers 


      
        # startPointer = 0 
        endPointer = 0 

        

        dictHolder = {}

        if not s: 
            return 0 
        maxWindow = 1

        for i in range(len(s)): 

            currLength = 1 # count itself 
            
            startPointer = i
            dictHolder[s[startPointer]] = True 

            endPointer = i + 1 

            while endPointer < len(s):
                print("dictHolder is", dictHolder)
                if s[endPointer] not in dictHolder: 
                    currLength += 1 
                    dictHolder[s[endPointer]] = True 
                    endPointer += 1

                    if currLength > maxWindow: 
                        maxWindow = currLength

                else: 
                    dictHolder = {}
                    break  
                

            dictHolder = {}
        return maxWindow



            



           




