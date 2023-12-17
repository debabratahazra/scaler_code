class Solution:

    def multiply(self, A, B):
        # perform A X B

        a_row = len(A)
        a_col = len(A[0])

        b_row = len(B)
        b_col = len(B[0])

        # Create a result matrix of appropriate size filled with zeros
        C = [[0 for row in range(len(B[0]))] for col in range(len(A))]

        for ai in range(a_row):
            for bj in range(b_col):
                for bk in range(b_row):
                    C[ai][bj] += A[ai][bk]*B[bk][bj]
                    print("C[i][j] =", ai, bj)

        return C

    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        # A x B is possible if A's column number and B's rows numbers are same
        # B x A is possible if B's column number and A's rows numbers are same

        if len(A) == len(B[0]):
            # perform A x B
            return Solution.multiply(self, A, B)

        elif len(B) == len(A[0]):
            # perform B x A
            return Solution.multiply(self, B, A)

        else:
            # can't perform matrix multiplication
            pass
            print("Can't perform matrix multiplication")

        return 0


s = Solution()
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]


]

B = [
    [1, 2, 3],
    [2, 6, 1],
    [7, 3, 9]
]

multi = s.solve(A, B)
print(multi)
