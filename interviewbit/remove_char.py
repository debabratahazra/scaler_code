'''Given a string A and integer B, remove all consecutive same characters that have length exactly B.


NOTE : All the consecutive same characters that have length exactly B will be removed simultaneously.'''

from itertools import groupby


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        # Use 2 pointers to traverse the
        # string and and keep removing elements
        # from the string when the length is
        # equivalent to given B.
        firstIndex = 0
        secondIndex = 0
        while secondIndex < len(A):
            # Keep going forward when the character
            # are same on a given index.
            if A[firstIndex] == A[secondIndex]:
                secondIndex += 1
            else:
                length = secondIndex-firstIndex
                # When the length is equal to given
                # B, remove that substring.
                if length == B:
                    A = A[:firstIndex]+A[secondIndex:]
                    secondIndex = firstIndex
                # If not, move forward both the pointers.
                else:
                    firstIndex = secondIndex
                    secondIndex += 1

        # Last occurance is not being removed in
        # the above loop. Remove it here.
        length = secondIndex-firstIndex
        if length == B:
            A = A[:firstIndex]+A[secondIndex:]

        # Return the modified string.
        return A

    def solve_my(self, A, B):
        res = ["".join(group) for ele, group in groupby(A)]
        new_str = ""
        for s in res:
            if len(s) == B:
                continue
            else:
                new_str += s
        return new_str


s = Solution()
A = "aabcd"
print(s.solve(A, 2))

A = "aabbccd"
print(s.solve(A, 2))
