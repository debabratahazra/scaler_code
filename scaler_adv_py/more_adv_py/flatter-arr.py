'''
Problem Description
Write a function flatten() that takes a nested list as input and returns a sorted flattened list.


Input Format
A nested list is taken as input


Output Format
A simple flat list sorted in ascending order is printed.
'''

def flatten(arr):
    '''
    input:
    arr -> given nested python list
    
    output:
    res_arr -> the nested list, flattened and sorted
    '''
    flat_arr = []
    flat_arr = flatten_recu(arr, flat_arr)

    res_arr = sorted(flat_arr)    
   
    return res_arr

def flatten_recu(A, flat_arr):
    for ele in A:
        if type(ele) == list:
            flatten_recu(ele, flat_arr)
        else:
            flat_arr.append(ele)
    return flat_arr
    

A = [10,[40,20],30,50]
print(flatten(A))