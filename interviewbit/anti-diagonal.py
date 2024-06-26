'''
Problem Description

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:

Input:

1 2 3
4 5 6
7 8 9

Return the following:
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
'''

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        matrix = A
        N = len(matrix)  # Assuming it is a square matrix
        if N == 0:
            return []

        # A list to store the anti-diagonals
        anti_diagonals = []

        # Process the first half of the anti-diagonals (including the main diagonal)
        for i in range(N):
            start_col = i
            start_row = 0
            anti_diagonal = []
            
            # Move down-left to collect the anti-diagonal elements
            while start_col >= 0 and start_row < N:
                anti_diagonal.append(matrix[start_row][start_col])
                start_row += 1
                start_col -= 1
            anti_diagonals.append(anti_diagonal)

        # Process the second half of the anti-diagonals
        for i in range(1, N):
            start_row = i
            start_col = N - 1
            anti_diagonal = []
            
            # Move down-left to collect the anti-diagonal elements
            while start_col >= 0 and start_row < N:
                anti_diagonal.append(matrix[start_row][start_col])
                start_row += 1
                start_col -= 1
            anti_diagonals.append(anti_diagonal)

        return anti_diagonals

s = Solution()
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(s.diagonal(matrix))