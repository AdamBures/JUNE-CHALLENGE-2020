class Solution:
# @param A, a list of integer
# @return an integer
    def singleNumber(self, A):
        ec1, ec2, ec3 = 0, 0, 0
        for ai in A:
            ec3 = ec2 & ai
            ec2 = (ec2 | (ec1 & ai)) & (~ec3)
            ec1 = (ec1 | ai) & (~ec3)        
        return ec1
