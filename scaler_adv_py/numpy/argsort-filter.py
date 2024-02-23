import numpy as np

'''
Given a list of birds and their corresponding age, calculate the mean age of the Cranes bird 
(rounded off to 2 decimal points)
'''


def calculate_mean_age(birds, age):
    '''
    INPUT: birds, age -> 1D array

    OUPUT: mean_age -> float variable
    '''

    mean_age = None

    # STEP1. Create mask to get Crane birds from birds array
    mask = birds == 'Cranes'
    print("Mask:", mask)

    # STEP2. Get the age of crane birds

    crane_ages = age[mask]
    print("Crane age array:", crane_ages)

    # STEP 3. Calculate mean age of crane birds

    mean_age = np.mean(crane_ages, axis=None)
    print("Mean age:", mean_age)

    # STEP 4. Round off the mean age to 2 decimal points

    mean_age = np.round(mean_age, 2)
    print("Round mean value:", mean_age)

    return mean_age


birds = np.array(['spoonbills',  'plovers',  'plovers',  'plovers',
                 'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills'])
age = np.array([5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0])

print(calculate_mean_age(birds, age))
