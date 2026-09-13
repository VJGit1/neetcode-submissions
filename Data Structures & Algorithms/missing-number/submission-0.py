class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n+1):
            ans=ans+i
        actual=0
        for i in nums:
            actual=actual+i
        return ans-actual