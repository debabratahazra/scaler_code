import numpy as np


def entropy(s):
    '''
    Calculates the entropy given list of target(binary) variables
    '''
    # Write your code here
    
    # Caclulate entropy
    entropy = 0
    
    
    #Your code ends here
    # Calculate entropy
    unique_labels, counts = np.unique(s, return_counts=True)
    total_count = len(s)
    probabilities = counts / total_count
    entropy = np.sum(probabilities * np.log2(probabilities))
    
    return -entropy

def find_attr(attr1, attr2, y):
    '''
    attr1 : Attribute1
    attr2: Attribute2
    y: The class labels

    '''
    attr1 = np.asarray(attr1)
    attr2 = np.asarray(attr2)
    y = np.asarray(y)
    
    #calculate the entropy of the parent node
    par_entropy = entropy(y)
    
    m = len(y)

    #if we split using the attr1
    y_10 = y[attr1 == 0]  #this node consists of all the observations where attr1 has value 0
    entr_10 = entropy(y_10)
    y_11 = y[attr1 == 1]  #this node consists of all the observations where attr1 has value 1
    entr_11 = entropy(y_11)
    y_12 = y[attr1 == 2]  #this node consists of all the observations where attr1 has value 2
    entr_12 = entropy(y_12)

    #Calculate the information gain for attribute 1
    info_gain_1 = par_entropy - (len(y_10)/m)*entr_10 - (len(y_11)/m)*entr_11 - (len(y_12)/m)*entr_12
    
    info_gain_1 = np.round(info_gain_1, 2)
    
    #if we split using the attr2
    y_20 = y[attr2 == 0]  #this node consists of all the observations where attr2 has value 0
    entr_20 = entropy(y_20)
    y_21 = y[attr2 == 1]  #this node consists of all the observations where attr2 has value 1
    entr_21 = entropy(y_21)

    #Calculate the information gain for attribute 2
    info_gain_2 = par_entropy - (len(y_20)/m)*entr_20 - (len(y_21)/m)*entr_21
    info_gain_2 = np.round(info_gain_2, 2)

    #return the attribute name along with corresponding info_gain for which information gain is higher if used in splitting 
    return ("attribute1", info_gain_1) if  info_gain_1 > info_gain_2 else ("attribute2", info_gain_2)

attr1 = [0, 1, 2, 1, 2, 0, 1, 2, 2, 0, 1, 1, 0, 1, 2, 1, 1, 1, 0, 1]
attr2 = [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1]
y = [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0]

print(find_attr(attr1, attr2, y))