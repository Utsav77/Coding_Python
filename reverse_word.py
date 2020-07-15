class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=[]
        for i in s:
            l.append(i)
        q=''
        for i in range(len(l)-1,-1,-1):
            q+=' '
            q+=str(l[i])
        return q[1:]
        
        