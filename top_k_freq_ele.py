class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        c=0
        res=[]
        for i in sort_d:
            c+=1
            res.append(i[0])
            if(c==k):
                break
        return res
