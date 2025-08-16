class Solution(object):
    def addBinary(self, a, b):
        sumBin = bin(int(a,2)+int(b,2))[2:]
        return sumBin
        