# Last updated: 24/05/2025, 12:53:22
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[] for _ in range(numRows)]
        if numRows == 0: 
            return [[]]

        currRow = 1 
        for i in range (numRows): 
            arr [i] =  [1] * currRow 
            currRow += 1 

        print(arr)
        
        if numRows <= 2: 
            return arr 
        
        for i in range (2,numRows): 
            for j in range (1,i): 
                arr [i][j] = arr [i-1][j-1] + arr [i-1][j]
                
        return arr 
