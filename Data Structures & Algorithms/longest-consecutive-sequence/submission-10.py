class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
       

        res = 1
        nums.sort()
        curr=1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                curr+=1
                res=max(curr,res)
            elif nums[i+1]-nums[i]==0:
                continue
            else: curr=1
        return res
            

        