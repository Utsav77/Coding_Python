class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        n=a+b
        return bin(n).replace("0b","")
        