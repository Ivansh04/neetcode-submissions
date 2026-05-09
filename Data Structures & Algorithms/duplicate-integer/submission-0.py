class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash=defaultdict(int)
        for num in nums:
            hash[num]+=1
        for i in hash:
            if hash[i]>1:
                return True
        return False
