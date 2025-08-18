# Last updated: 8/18/2025, 7:13:23 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #could do something like max subarray for first elem, then 1,2 then 1,2,3, then 1,2,3,4
        n = len(nums)
        maxSums = [-10001]*n
        maxSums[0] = nums[0]
        maxVal = maxSums[0]
        for i in range(1, n):

            maxSums[i] = max(maxSums[i-1]+nums[i], nums[i])

            if (maxSums[i]>maxVal):
                maxVal = maxSums[i]
        

        return maxVal


        


        