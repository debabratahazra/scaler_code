'''
There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.

The positions of Mice are denoted by array A and the position of holes are denoted by array B.

A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.

Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.'''

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
    def mice(self, A, B):
        mice = A
        holes = B
        if len(mice) != len(holes):
            return -1  # Unequal number of mice and holes, cannot solve.

        # Sort the positions of mice and holes
        mice.sort()
        holes.sort()
        
        # Initialize the maximum time
        max_time = 0
        
        # Pair each mouse with a hole
        for i in range(len(mice)):
            # Calculate the time for mouse i to reach hole i
            time = abs(mice[i] - holes[i])
            # Update the maximum time
            max_time = max(max_time, time)
        
        # The maximum time is the answer
        return max_time

s = Solution()
# Example usage:
A = [4, -4, 2]  # Positions of mice
B = [4, 0, 5]   # Positions of holes
print(s.mice(A, B))  # Output will be 4