class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs={}
        for i in strs:
            key=''.join(sorted(i))
            hs[key]=hs.get(key,[])+[i]
        return list(hs.values())


        