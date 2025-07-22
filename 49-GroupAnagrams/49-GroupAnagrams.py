# Last updated: 22/07/2025, 16:42:27
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: 
            return [[""]]

        holderDict = {}



        for word in strs: 
            # word is original word
            sortedString = ''.join(sorted(word))
            # print(sortedString)
            # print(type(sortedString))

            if sortedString in holderDict: 
                currList = holderDict [sortedString]
                #print(type(currList))
                currList.append(word)
                #print(currList)
                holderDict [sortedString] = currList
                #newList = [currList].append(word)
                #print(newList)
                
                #holderDict [sortedString] = currList.append(newList)
            
            else: 
                holderDict [sortedString] = [word]
        
       # print(holderDict)
        result = []
        for i in holderDict.values(): 
            result.append(i)

        return result

        

        ## test dictionary 

        ## can i sort by the no. of characters? 

        ## if they are anagrams, def will have the same number of letters 



        ## if sort all word in strs, they will give me the same letters 
        # -- right intuiton 

        # a = "eat"
        # b = "tea"
        # sortedString = ''.join(sorted(a))
        # print(sortedString)
        # #print(b.sort())


