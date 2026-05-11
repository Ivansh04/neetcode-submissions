class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        elif len(nums)==0: return 0
        nums.sort()
        cnt,ans=1,1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                cnt+=1
                ans=max(cnt,ans)
            elif nums[i+1]-nums[i]==0:
                continue
            else: cnt=1
        return ans
        