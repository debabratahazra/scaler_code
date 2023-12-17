# https://www.scaler.com/academy/mentee-dashboard/class/159483/homework/problems/22295?navref=cl_tt_nv

'''
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
'''


def check_anagram(s1, s2):
    '''Input: s1,s2 are the two strings
       Output: return True if given strings are anagrams else False'''

    # YOUR CODE GOES HERE
    s1_list = list(s1)
    s2_list = list(s2)
    for ch in s1_list:
        if ch in s2_list:
            s2_list.remove(ch)
        else:
            return False
    if len(s2_list) == 0:
        return True

    return False


s1 = "abcdefg"
s2 = "acbedgf"
print(check_anagram(s1, s2))
