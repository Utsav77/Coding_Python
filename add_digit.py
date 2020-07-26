class Solution:
    def addDigits(self, num: int) -> int:
        x=num % 9
        if(num<=9):
            return num
        if(x==0):
            return 9
        else:
            return x
        