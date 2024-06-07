'''
Given an array, find the next greater element G[i] for every element A[i] in the array.  The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]

Output : [5, 10, 10, -1]
'''

class Solution:
	# @param A : list of integers
	# @return a list of integers
    def nextGreater(self, A):
        arr = A
        result = [-1] * len(arr)  # Step 2: Initialize the result array with -1
        stack = []  # Step 1: Initialize the stack

        for i in range(len(arr)):  # Step 3: Iterate through the input array
            # Step 4: Resolve indices where we can determine the next greater element
            while stack and arr[i] > arr[stack[-1]]:
                result[stack.pop()] = arr[i]
            # Step 5: Push the current index onto the stack
            stack.append(i)

        # Step 6: Indices left in the stack don't have a next greater element, so they remain -1
        # Step 7: Return the filled result array
        return result

s = Solution()
A = [4, 5, 2, 10]
print(s.nextGreater(A)) # [5, 10, 10, -1]

