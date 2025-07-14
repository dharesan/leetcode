# Last updated: 14/07/2025, 15:55:46
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
    #     # Greedy Approach - O(n^2)
    #     possibleStartingStations = []

    #     for i in range(len(gas)): 
    #         if gas [i] >= cost [i]: 
    #             possibleStartingStations.append(i)
    #     # print(possibleStartingStations)

    #     if len(gas) == 0: 
    #         return -1 

    #     if len(possibleStartingStations) == 0: 
    #         return -1 

    #    # fuelMeter = 0 

    #     for j in possibleStartingStations: ## j is a starting index
    #         currIdx = j 
    #         fuelMeter = 0 


    #         for i in range(len(gas)): # run n times
    #             #print("currIdx is", currIdx)
    #             fuelMeter += gas [currIdx]
    #             fuelMeter -= cost [currIdx]

    #             if fuelMeter < 0: 
    #                 #print("fuel meter < 0 !")
    #                 break # does it go to the next value of j? 
    #                 #print("prints after break")

    #             currIdx = ((currIdx + 1) % len(gas))

    #         #print("currIdx at the final step is" ,currIdx)  
    #         #print(possibleStartingStations)
    #         if currIdx == j: 
    #             return j 

    #     return -1 
            
    ## Try O(n) method 

        start = 0 
        tank = 0 

        totalGas = 0
        totalCost = 0 

        for i in range(len(gas)): 
            tank += gas [i] 
            tank -= cost [i]

            totalGas += gas [i] 
            totalCost += cost [i]

            if tank < 0: 
                start = i + 1
                tank = 0 

        if totalCost > totalGas: 
            return -1 
        else: 
            return start 




        