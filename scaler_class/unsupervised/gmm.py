#import GMM from scikit-learn library
from sklearn.mixture import GaussianMixture 

data = [[4, 13, 2], [9, 8, 11], [14, 4, 2]]
no_of_components = 2

def make_clusters(data, no_of_components):
    """
       data -> numpy array for the data 
       no_of_components -> number of a mixture of components
       return a Numpy array of labels
    """
    
    # initialize gmm model
    gmm = GaussianMixture(n_components=no_of_components)
    
    # fit the model
    gmm.fit(data)
    
    #predict labels for the data 
    labels = gmm.predict(data)
    
    return labels


print(make_clusters(data, no_of_components))