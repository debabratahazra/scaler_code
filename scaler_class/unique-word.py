# https://www.scaler.com/academy/mentee-dashboard/class/159473/assignment/problems/22407?navref=cl_tt_nv

def set_operation(sent1, sent2):
    ''' input:sent1,sent2-two sentences taken as inputs
         output:return the sum of length of unique words.'''

    # YOUR CODE GOES HERE
    str1_tuple = tuple(sent1.split())
    str2_tuple = tuple(sent2.split())
    length = 0
    str_set = set()
    str_set.update(str1_tuple)
    length = len(str_set)

    str_set = set()
    str_set.update(str2_tuple)
    length += len(str_set)
    return length


str1 = "in data analysis we use data and process it further to create better interpreted data"
str2 = "more and more data will be passively collected"

print(set_operation(str1, str2))
