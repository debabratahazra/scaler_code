'''
Problem Description
Complete the function, which accepts a string consisting of some numbers and blanks (underscores), 
separated by commas, and fills these blanks as per the given conditions:
blanks to the left of a number should be filled by the number distributed equally, into the number of 
blanks to the left, along with the number position itself
middle blanks of two numbers should be filled by their sum equally distributed, along with their two positions
right blanks of a number should be again distributed equally by that number, along with the position of the 
number itself.
Refer to sample input, output, and explanation for better clarity.



Example Input

_,_,30,_,_,_,50,_,_


Example Output
[10, 10, 12, 12, 12, 12, 4, 4, 4]


Example Explanation
30 is distributed to the left two blanks and its position itself. The list becomes now: 
(10,10,10,_ ,_ ,_ ,50,_ ,_ )
Then the sum of 10 and 50 is distributed among the blanks between 10 and 50, as well as the 
position of 10 and 50: (10,10,12,12,12,12,12,_ ,_ )
Finally, 12 is distributed to the rest blanks in the right and the position of 12 itself: 
(10,10,12,12,12,12,4,4,4)

'''

def data_distribute(input_data):
    '''
    input:
    input_data -> the input data in the form of a string, such as "_,10,_"
    output:
    filled_data -> the output python list with the missing data filled up in place of the blanks
    '''
    filled_data = None

    # Splitting the data on the basis of ',' so that we can separately get the blanks(_) and the numbers.
    filled_data = input_data.split(',')

    # Intialising a position variable to keep a track at which index we are at while iterating
    pos = 0

    # Looping until there are '_' in the data
    while('_' in filled_data):
        # Intialising count variable to count the number of blanks we encounter before getting a number
        count = 0
        
        # Intialising a variable to store the sum till we encounter another number
        acc = 0
       
        # Iterating through the entire input
        for i in range(pos,len(filled_data)):
            count +=1

            # If the data is not a blank we simply add the value to the acc variable
            if filled_data[i] != '_':
                acc+=int(filled_data[i])

                # If the count is greater than 1 we break out from the for loop because it signifies we have got the second number
                # this condition is important for dealing blanks between 2 numbers
                if(count >1):
                    break
        
        # After we break out of loop we need to distribute the sum in the blanks. So we divide it by the count
        acc = acc//count
        
        # We fill the position from the starting position to the position where we broke out from loop with the value of acc
        filled_data[pos:pos+count]= [acc]*count

        # Update the position of pos to start from the position where the loop broke out.
        pos = pos + count-1

    # Returning the required array
    return filled_data


s = "_,_,30,_,_,_,50,_,_"
print(data_distribute(s))

s = "80,_,_,_,_"
print(data_distribute(s))

s = "40,_,_,_,60"
print(data_distribute(s))