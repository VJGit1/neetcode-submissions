class Solution:
    def hammingWeight(self, n: int) -> int:
        #Brute:convert the integer to binary & then we count 1
        #return bin(n).count("1")
        count=0
        while n:
            if n & 1:
                count+=1
            n>>=1
        return count