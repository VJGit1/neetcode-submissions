class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algo
        currMax=nums[0]
        globalMax=nums[0]
        for i in range(1,len(nums)):
            currMax=max(nums[i],currMax+nums[i])
            globalMax=max(currMax,globalMax)
        return globalMax