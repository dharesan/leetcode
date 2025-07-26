"""Solution is O(n x k) time complexity"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # I think o(n) time complexity 
        startPointer = 0
        endPointer = startPointer + k 

        result = []

        while endPointer <= len(nums): 
            temp = nums [startPointer:endPointer]
            #temp = list(map(lambda x: nums[startPointer:endPointer], nums))
            #print(temp)
            a = max(temp)
            print(type(a))
            print("maxtempis,", a)

            result.append(max(temp))


            startPointer += 1
            endPointer += 1 
        return result 

