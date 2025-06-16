import math

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def single_linkage_distance(cluster1, cluster2):
    """
    Calculate single linkage distance between two clusters
    Single linkage = minimum distance between any two points from different clusters
    """
    min_distance = float('inf')
    closest_pair = None
    
    for i, point1 in enumerate(cluster1):
        for j, point2 in enumerate(cluster2):
            distance = euclidean_distance(point1, point2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (point1, point2)
    
    return min_distance, closest_pair

def single_linkage_similarity(cluster1, cluster2):
    """
    Calculate single linkage similarity between two clusters
    Similarity = 1 / distance (inverse of euclidean distance)
    """
    distance, closest_pair = single_linkage_distance(cluster1, cluster2)
    similarity = 1 / distance
    return similarity, distance, closest_pair

# Define the clusters
cluster1 = [(10,2), (4,15), (0,15), (3,12), (7,8), (4,8)]
cluster2 = [(-1,-5), (-8,-10), (-10,-20), (-4,-20), (-1,-25)]

print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print()

# Calculate similarity using single linkage
similarity, min_distance, closest_pair = single_linkage_similarity(cluster1, cluster2)

print("=== Single Linkage Analysis ===")
print(f"Minimum distance between clusters: {min_distance:.4f}")
print(f"Closest pair of points: {closest_pair[0]} from Cluster1 and {closest_pair[1]} from Cluster2")
print(f"Single Linkage Similarity = 1/distance = 1/{min_distance:.4f} = {similarity:.6f}")

print("\n=== Detailed Distance Matrix ===")
print("Distance between each pair of points:")
print("Cluster1 Point\t\tCluster2 Point\t\tDistance")
print("-" * 60)

for point1 in cluster1:
    for point2 in cluster2:
        distance = euclidean_distance(point1, point2)
        print(f"{point1}\t\t{point2}\t\t{distance:.4f}")