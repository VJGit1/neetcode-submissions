class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        currMax,currMin,maxProd=nums[0],nums[0],nums[0]
        for i in range(1,n):
            temp=max(nums[i],nums[i]*currMin,nums[i]*currMax)
            currMin=min(nums[i],nums[i]*currMin,nums[i]*currMax)
            currMax=temp
            maxProd=max(maxProd,currMax)
        return maxProd