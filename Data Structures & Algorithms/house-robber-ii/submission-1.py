class Solution:
    def rob(self, nums: List[int]) -> int:
        # #first and last houses will be adjacent
        # case1:start from first house but exclude the last one
        # case2:start from second house and include the last house
        n=len(nums)
        if n==1:
            return nums[0]
        def house_robber1(nums):
            n=len(nums)
            if n==1:
                return nums[0]
            dp=[0]*n
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            return dp[n-1]
        case1=house_robber1(nums[:-1])#exclude last house
        case2=house_robber1(nums[1:])#exclude first house
        return max(case1,case2)