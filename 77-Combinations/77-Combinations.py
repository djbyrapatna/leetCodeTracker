# Last updated: 8/18/2025, 7:04:16 PM
class Solution:

    
    def combine(self, n: int, k: int) -> List[List[int]]:
        solArray = []
        
        def backtrack(currCombo, currNumber):
            #print(currCombo, currNumber)
            if len(currCombo)==k:
                solArray.append(currCombo[:])
                #print("Added", currCombo)
                return
            else:
                for i in range(currNumber+1, n+1):
                    #print(i, currCombo)
                    currCombo.append(i)
                    #print(i, currCombo)
                    backtrack(currCombo, i)
                    #print(i, currCombo, "After")
                    currCombo.pop()
                    
        
        backtrack([],0)
        return solArray
