# Last updated: 10/9/2025, 7:55:32 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        N = len(gas)
        sumArr = [x-y for x, y in zip(gas, cost)]
        total = sum(sumArr)
        testArr = [0]*N
        testArr[0] = sumArr[0]
        for i in range(1, N):
            testArr[i] = testArr[i-1]+sumArr[i]
        print(sumArr)
        if total<0:
            return -1
        else:
            index = testArr.index(min(testArr))
            if index!=N-1:
                return index+1
            else:
                return 0
        



        #brute force soln first
        N = len(gas)
        gas_dup = gas + gas
        cost_dup = cost+cost

        for si in range(N):
            tank = 0
            stationsVisited = 0
            i = si
            while stationsVisited < N:
                
                tank += gas_dup[i] - cost_dup[i]
                if tank >=0:
                    i+=1
                    stationsVisited+=1
                else:
                    break
            if stationsVisited == N:
                return si
        
        return -1
                
        