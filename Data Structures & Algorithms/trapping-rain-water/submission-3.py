class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        i=0
        while i<len(height)-1:
            if height[i]!=0:
                j=i+1
                maxx=0
                maxxi=0
                while height[j]<height[i]:
                    if height[j]>maxx: 
                        maxx=height[j]
                        maxxi=j         
                    if j==len(height)-1:
                        if maxx==0: return res
                        j=maxxi
                        break
                    j+=1
                for k in range(i+1,j):
                    res+=(min(height[i],height[j])-height[k])
                i=j
                continue    
            i+=1
        return res
        