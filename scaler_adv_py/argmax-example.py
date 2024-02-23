import numpy as np


def oldest_bird(birds, age):
    ''' birds[i] consist of the names of the type of ith bird
        age[i] consist of the age of ith bird'''

    print("birds", birds)
    print("age:", age)

    # STEP 1: Get the index of maximum age element

    max_age_index = age.argmax()
    print("Sort index:", max_age_index)

    # STEP 2: Get the bird with maxium age using the above index

    old_bird = birds[max_age_index]
    print(old_bird)

    return old_bird


# case 1
birds = np.array(['sparrow', 'peacock', 'parrot', 'owl',
                 'peacock', 'macaw', 'macaw', 'parrot', 'macaw', 'peacock'])
age = np.array([6, 1, 6, 5, 7, 6, 0, 9, 0, 7])

print(oldest_bird(birds, age))
# case 2
birds = np.array(['parrot', 'owl', 'macaw', 'macaw', 'owl', 'owl', 'macaw', 'macaw', 'sparrow', 'owl',
                 'sparrow', 'parrot', 'macaw', 'peacock', 'sparrow', 'macaw', 'peacock', 'owl', 'owl', 'parrot'])
age = np.array([8, 1, 12, 13, 13, 8, 11, 7, 6, 1,
               7, 4, 12, 6, 1, 8, 14, 13, 14, 1])
print(oldest_bird(birds, age))
