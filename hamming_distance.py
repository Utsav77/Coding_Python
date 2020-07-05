class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def countSetBits(n):
            count = 0
            while (n): 
                n &= (n-1)  
                count+= 1

            return count
        
        z=x ^ y
        return(countSetBits(z))
        
        