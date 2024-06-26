'''
For Given Number A, find if it's a COLORFUL number or not.

COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Return 1 if A is a COLORFUL number, else return 0
'''

class Solution:
	# @param A : integer
	# @return an integer
    def colorful(self, A):
        # Step 1: Convert the number to a string
        num_str = str(A)
        products = set()

        # Step 2: Generate all contiguous subsequences
        for i in range(len(num_str)):
            product = 1
            for j in range(i, len(num_str)):
                product *= int(num_str[j])
                # Step 3: Check for duplicate products
                if product in products:
                    return 0
                products.add(product)

        # If no duplicates are found, it's a colorful number
        return 1

s = Solution()
A = 3245
print(s.colorful(A)) # 1

A = 23
print(s.colorful(A)) # 1

A= 111
print(s.colorful(A)) # 0