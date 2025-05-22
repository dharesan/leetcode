class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        distanceDict = {}
        for vertex in range(n): 
            distanceDict [vertex] = float("inf") 

        distanceDict [src] = 0 


        # # Create adjacency List 
        # for i in range(len(edges)): 
        #     departure_vertex = edges [i][0]
        #     arrival_vertex = edges [i][1]
        #     weight = edges [i][-1]

        #     adjDict [departure_vertex] 

        edges_copy = edges.copy()
        #print(edges_copy)

        queue = []

        heapq.heappush(queue, [0, src])
        
        while queue:
            curr = heapq.heappop(queue) [1]
            for i in range(len(edges_copy)): 
                if curr == edges_copy[i][0]: #edge exists
                    toVertex = edges_copy [i][1]
                    weight = edges_copy [i][-1]

                    if distanceDict[curr] + weight < distanceDict[toVertex]:
                        tempDistance = distanceDict[curr] + weight
                        distanceDict[toVertex] = tempDistance
                        heapq.heappush(queue,[tempDistance,toVertex])

                    #edges_copy.pop(i) # remove from the list 

        #print(distanceDict)
        for i in distanceDict: 
            if distanceDict [i] == float('inf'): 
                distanceDict [i] = -1
        return distanceDict
