import numpy as np


def sort_birds(birds, age):
    '''
    INPUT: birds, age -> 1D numpy array

    OUTPUT: result -> sorted bird 1D array
    '''

    print(birds, age)

    # STEP 1 : Get the sorted index of age.

    sorted_age_index = age.argsort()
    print("Sorted age index: ", sorted_age_index)

    # STEP 2: Use the index from previous step to get sorted birds

    result = birds[sorted_age_index]

    return result


birds = np.array(['spoonbills',  'plovers',  'plovers',  'plovers',
                 'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills'])
age = np.array([5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0])

print(sort_birds(birds, age))
