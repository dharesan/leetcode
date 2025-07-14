# Last updated: 14/07/2025, 13:46:01
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


    # Brute Force 

    # Sliding window? 

    # 1. CREATE ALL INTERVALs 
    # 2. sort all start times 
    # 0 5 15 

    # 30, 5, 15
    # 5, 15, 30  


    # for each start time 

    # allocate a room for the first slot 

    # give an index for each start time? 

    # keep track of numOfRooms 

        if not intervals: 
            return 0 

        totalRooms = 1 
        startPointer = 1 
        endPointer = 0 

        roomsAvailable = 0 # init

        startList = []
        endList = []

        for i in intervals: 
            startList.append(i[0])
            endList.append(i[-1])

        startList.sort() # in place sorting
        endList.sort()

        print(startList)
        print(endList)

        # assume startPointer points to index 1

        while (startPointer < len(startList)): 
            # if not roomsAvailable: 
            #     totalRooms += 1 

            #     startPointer += 1
            print(f"I am comparing {startList [startPointer]} with {endList [endPointer]}")

            if startList [startPointer] < endList [endPointer]: 
                if not roomsAvailable: 
                    totalRooms += 1
                else: 
                    roomsAvailable -= 1
                startPointer += 1

            else: 
                roomsAvailable += 1 
                endPointer += 1

            # startPointer += 1



        return totalRooms 



        



        