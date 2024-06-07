'''
Given an array A, count the number of inversions in the array.
Formally speaking, two elements A[i] and A[j] form an inversion if A[i] > A[j] and i < j
'''

class Solution:
	# @param A : list of integers
	# @return an integer
    def countInversions(self, A):
        _, total_inversions = self.merge_sort_and_count(A)
        return total_inversions
    
    def merge_sort_and_count(self, arr):
        # Base case: if the list is a single element, return it with zero inversions
        if len(arr) <= 1:
            return arr, 0

        # Split the array into two halves
        middle_index = len(arr) // 2
        left_half, left_inversions = self.merge_sort_and_count(arr[:middle_index])
        right_half, right_inversions = self.merge_sort_and_count(arr[middle_index:])

        # Merge the two halves together, counting cross inversions
        merged_array, cross_inversions = self.merge_and_count(left_half, right_half)

        # Total inversions is the sum of inversions in left, right, and cross inversions
        total_inversions = left_inversions + right_inversions + cross_inversions

        return merged_array, total_inversions
    
    def merge_and_count(self, left, right):
        merged = []
        left_index = right_index = 0
        inversions = 0

        # Traverse both arrays and merge them in sorted order
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                # If an element in the right array is smaller, we found (mid - i) inversions
                merged.append(right[right_index])
                inversions += len(left) - left_index
                right_index += 1

        # Add any remaining elements of left/right to the merged array
        merged += left[left_index:]
        merged += right[right_index:]

        return merged, inversions
    
s = Solution()
A = [2, 4, 1, 3, 5]
print(s.countInversions(A))
