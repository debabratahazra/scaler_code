# https://www.scaler.com/academy/mentee-dashboard/class/159473/homework/problems/22222?navref=cl_tt_nv

def odd_even_split_tuple(tup):
    ''' input:tup-indicates the tuple
         output:print two tuples one for even indexed and odd indexed in the given output format'''

    # YOUR CODE GOES HERE
    odd_list = []
    even_list = []
    for index in range(len(tup)):
        if index % 2 == 0:
            # odd one
            odd_list.append(tup[index])
        else:
            even_list.append(tup[index])
    odd_tup = tuple(odd_list)
    even_tup = tuple(even_list)
    print(f"Odd: {odd_tup}")
    print(f"Even: {even_tup}")


tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
odd_even_split_tuple(tup)
