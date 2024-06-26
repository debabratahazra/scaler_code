'''
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:  

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.

'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = -1
        max_start_index = -1
        max_end_index = -1
        current_sum = 0
        current_start_index = 0

        for i, val in enumerate(A):
            if val >= 0:
                current_sum += val
                if (current_sum > max_sum) or \
                (current_sum == max_sum and i - current_start_index > max_end_index - max_start_index) or \
                (current_sum == max_sum and i - current_start_index == max_end_index - max_start_index and current_start_index < max_start_index):
                    max_sum = current_sum
                    max_start_index = current_start_index
                    max_end_index = i
            else:
                current_sum = 0
                current_start_index = i + 1

        if max_start_index >= 0:  # this checks if there was at least one non-negative number
            return A[max_start_index:max_end_index + 1]
        else:
            return []
    
s = Solution()
A = [1, 2, 5, -7, 2, 3]
print(s.maxset(A)) # [1, 2, 5]