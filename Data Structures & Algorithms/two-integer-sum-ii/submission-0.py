class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         hash1={}
         for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hash1:
                return[hash1[diff]+1,i+1]
            hash1[nums[i]]=i