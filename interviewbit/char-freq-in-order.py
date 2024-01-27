'''Problem Description
 
 

Given a string A containing only lowercase characters.
Find the frequencies of the characters in order of their occurrence.'''

from collections import OrderedDict


class Solution:
    def find_char_indexes(self, input_string, char_to_find):
        return [i for i, char in enumerate(input_string) if char == char_to_find]
    # @param A : string
    # @return a list of integers

    def solve(self, A):
        frequency_table = []
        for i in range(len(A)):
            frequency_table.append(0)
        for ch in A:
            chars = self.find_char_indexes(A, ch)
            frequency_table[chars[0]] = len(chars)
        final_frequency_table = []
        for frequency in frequency_table:
            if frequency == 0:
                continue
            final_frequency_table.append(frequency)
        return final_frequency_table

    def solve2(self, A):
        frequency_table = OrderedDict((char, A.count(char)) for char in A)
        final_count = []
        for val in frequency_table.values():
            final_count.append(val)
        return final_count


s = Solution()
A = "interviewbit"
print(s.solve(A))

A = "scaler"
print(s.solve(A))

A = "scaler"
print(s.solve2(A))


class Solution2:
    # @param A : string
    # @return a list of integers
    def solve_good(self, A):
        dic = OrderedDict()
        for val in A:
            dic[val] = dic.get(val, 0)+1

        ans = []
        for k, v in dic.items():
            ans.append(v)
        return ans
