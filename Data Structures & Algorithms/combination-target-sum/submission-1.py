class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]
        def backtrack(i,curr_sum):
            #base case1
            if curr_sum==target:
                res.append(sol[:])
                return
            #base case if curr sum>target or we ran out of elements
            if curr_sum>target or i==n:
                return
            #Left Branch: Don't pick nums[i] 
            #move to the next index without adding nums[i] to curr sum
            backtrack(i+1,curr_sum)

            #Pick nums[i] 
            #include nums[i] in our solution, recurse forward and backtrack
            sol.append(nums[i])
            backtrack(i,curr_sum+nums[i])
            sol.pop()
        backtrack(0,0)
        return res        