class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    #skip duplicate left values
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    #skip duplicate right values
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return res

    #    #Brute Force
    #     n=len(nums)
    #     res=[]
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             for k in range(j+1,n):
    #                 if(nums[i]+nums[j]+nums[k]==0):
    #                     ans=sorted([nums[i],nums[j],nums[k]])
    #                     if ans not in res:
    #                         res.append(ans)
    #     return res