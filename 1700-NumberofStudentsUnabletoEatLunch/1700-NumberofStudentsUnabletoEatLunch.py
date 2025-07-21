# Last updated: 21/07/2025, 17:42:12
from queue import Queue 

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # queueSandwich = Queue (maxsize = len(sandwiches))
        # for sandwich in sandwiches: 
        #     queueSandwich.put(sandwich)

        queueStudents = Queue (maxsize = len(students))
        for preference in students: 
            queueStudents.put(preference)
        

        numOfStudents = len(students)

        preference_0 = 0 
        preference_1 = 0 

        for preference in students: 
            if preference == 0: 
                preference_0 += 1
            else: 
                preference_1 += 1 

        # Termination case 
        while preference_0 > 0 or preference_1 > 0 or sandwiches: 

            currSandwich = sandwiches [0]

            if currSandwich == 0 and preference_0 == 0: 
                break 

            if currSandwich == 1 and preference_1 == 0: 
                break 

            currPreference = queueStudents.get()

            print("currSandwich is", currSandwich)
            print("currPreference is", currPreference)

            if currSandwich == currPreference:
                sandwiches.pop(0) # remove sandwich
                if currSandwich == 0: 
                    preference_0 -= 1 # decrement finish the sandwich 
                else: 
                    preference_1 -= 1
            else: 
                queueStudents.put(currPreference) # requeue 
                # dont change the counter


        return preference_0 + preference_1

        # print (preference_0)
        # print(preference_1)

     


        # termination case: check if there are any one in the queue which
        # equals to sandwiches [0]
        # should check this with a variable 

