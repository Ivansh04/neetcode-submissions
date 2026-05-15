class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        for i in range(len(temperatures)):
            j=i+1
            while j<len(temperatures) and temperatures[j]<=temperatures[i]:
                j+=1
            if j==len(temperatures):
                temperatures[i]=0
                continue
            temperatures[i]=j-i
        return temperatures
        