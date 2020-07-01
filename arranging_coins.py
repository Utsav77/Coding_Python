class Solution:
    def arrangeCoins(self, n: int) -> int:
        c=0
        s=0
        if(n==1):
            return 1
        for i in range(1,n):
            s+=i
            if(s>n):
                return c
            else:
                c+=1
        return c
                
            
            