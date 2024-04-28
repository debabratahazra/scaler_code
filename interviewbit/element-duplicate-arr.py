'''
Given a sorted array A consisting of duplicate elements.

Your task is to remove all the duplicates and return the length of the sorted array of distinct 
elements consisting of all distinct elements present in A.

Note: You need to update the elements of array A by removing all the duplicates
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is not None or len(A) == 0:
            return 0

        count = 1
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                A[count] = A[i]
                count += 1
        return count

s = Solution()
A = [0]
print(s.removeDuplicates(A))