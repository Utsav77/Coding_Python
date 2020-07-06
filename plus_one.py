class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        t=str(int(s)+1)
        l=[]
        for i in t:
            l.append(i)
        return l
        