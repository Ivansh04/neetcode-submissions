class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        res=[1]*len(nums)
        l1,r1=1,1
        while l<len(nums):
            if l>0:
                l1=nums[l-1]*l1
                res[l]*=l1
            if r<len(nums)-1:
                r1=nums[r+1]*r1
                res[r]*=r1
            r-=1
            l+=1
        return res

        
    