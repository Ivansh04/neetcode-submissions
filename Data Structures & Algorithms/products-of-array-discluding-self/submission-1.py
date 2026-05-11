class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd=1
        zr=0
        for i in nums:
            if i==0:
                zr+=1
                if zr>=2:
                  return [0]*len(nums)
                continue
            
            prd*=i
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i]=int(prd/nums[i])
            else: 
                nums=[0]*len(nums)
                nums[i]=prd
                return nums
        return nums 

        