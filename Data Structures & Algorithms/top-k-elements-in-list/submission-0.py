class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs={}
        for i in range(len(nums)):
            hs[nums[i]]=hs.get(nums[i],0)+1
        arr = []
        for i, j in hs.items():
            arr.append([j, i])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

            


        