# Last updated: 16/07/2025, 19:15:07
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)

        answer[0] = 1 

        # R = 1 
        for i in range(1, len(nums)): 
            answer [i] = answer[i-1] * nums [i-1]
            # R *= nums [i-1]

        R = 1
        for j in reversed(range(len(nums))):
            answer[j] = R * answer[j]
            R *= nums[j]
        
        return answer



        




        """
        # result = []
        # for i in range(len(nums)): 
        #     result[i] = nums 

        # Take extra O(n) space 
        n = len(nums)
        answer = [1] * n  # Step 1: Init output with 1s

        # Step 2: Left-to-right pass for prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            # prefix *= nums[i]
            prefix = prefix * nums[i]
            #print("prefix after prefix is", prefix)

        print('answer here is', answer)

        # Step 3: Right-to-left pass for suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            print("i am at index", i)
            # answer[i] *= suffix
            answer [i] = answer[i] * suffix
            suffix = suffix * nums[i]
            #suffix *= nums[i]
            print("answer after suffix is", answer)


        return answer



        """
#         dictResult = {}
#         for alphabet in nums: 
#             if alphabet in dictResult: 
#                 dictResult [alphabet] += 1
#             else: 
#                 dictResult [alphabet] = 1 

#         keyHolder = []
#         for key in dictResult.keys(): 
#             keyHolder.append(key)
        
#         print(keyHolder)

#         memory = {}


#         for index in range(len(keyHolder)): 
            
#             memory [keyHolder[index]] = tempCalc 



            

    
#         # Brute force is O(n^2)


#         # DP 
#         # Sort first --> result can be shared for repeating 
# """
# """