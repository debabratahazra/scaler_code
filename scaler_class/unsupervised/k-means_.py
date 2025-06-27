import numpy as np

points = np.array([(10,10), (11,11), (12,12), (15,15),(1,2),(3,4),(1,4),(0,4),(0,5),(-2,4),(-3,5),(6,-8),(5,6),(-1,-2),(3,-5),(4,-8),(5,-10),(-4,-4),(-2,-1),(0,0),(-3,0),(3,3),(4,4),(1,2),(6,7),(-9,0)])
centroids = np.array([(1,1),(-1,1),(-1,-1)])

# function returns the manhattan distance between points p1 and p2
def calc_dist(p1, p2):
    """p1 and p2 are two tuples representing the points"""
    dist = np.sum(np.abs(np.array(p1) - np.array(p2)))
    return dist

# function returns the updated centroid for the points in lst which represent a cluster
def update_centroid(lst):
    """lst is a list consisting of points in a cluster"""
    if len(lst) == 0:
        return np.array([0, 0])
    
    lst_arr = np.array(lst)
    new_centroid = np.mean(lst_arr, axis=0)
    return new_centroid

# function performs one iteration of k-means
def k_means(points, centroids):
    """points is a 2d numpy array consisting of points whereas
    centroids is a 2d numpy array consisting of initial centroids"""
    
    # Initialize empty clusters - each cluster is a list of points
    clusters = [[] for i in range(len(centroids))]
    
    for pnt in points:
        # Calculate distances from current point to all centroids
        distances = []
        for centroid in centroids:
            distances.append(calc_dist(pnt, centroid))
        
        # Find the cluster with minimum distance
        cluster_id = np.argmin(distances)
        clusters[cluster_id].append(pnt)
    
    # Update the centroid of each cluster
    new_centroids = []
    for cluster in clusters:
        new_centroids.append(update_centroid(cluster))
    
    return np.array(new_centroids)

# Perform 5 iterations of k-means
for i in range(5):
    centroids = k_means(points, centroids)
    print(np.round(centroids, 2))