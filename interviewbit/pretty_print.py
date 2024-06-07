'''
Print concentric rectangular pattern in a 2d matrix. 

Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.

Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = 2*A - 1
        matrix = [[0]*size for _ in range(size)]
        
        for i in range(size):
            for j in range(size):
                # Calculate distances from each edge and use the maximum
                matrix[i][j] = max(abs(i - (A - 1)), abs(j - (A - 1))) + 1

        # Print the matrix
        for row in matrix:
            print(*row)

s = Solution()
A = 3
s.prettyPrint(A)