'''
You are planning to go to the 5 nearest tourist spots from your house. So you start calculating 
the distance of all possible places from your house. The 2d coordinates of the tourist spots are 
given in a list of tuples lis and the coordinates of your house are in the list pnt.

Complete the function compute_Dist(lis,pnt) that returns a list of tuples consisting of the 
coordinates of the 5 nearest tourist spots.

Input Format:

The first line consists of two space-separated integers representing the coordinates of your house.
The second line consists of an integer n representing the number of tourist spots for consideration.
After the 2nd line, there will be n lines of input each line will have two space-separated integers 
representing the coordinates of the tourist spots.
Output Format:

A list of 5 tuples is simply printed
Sample input:

0 0
6
5 5
1 1
2 2
3 3
4 4
6 6
Sample output:

[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
Note: You can use Euclidean distance for the calculation of distances. The returned order of 
coordinates in the list should be increasing in terms of distance from the house coordinates. 
In case the distance is same for 2 points, the order should be same as obtained in the input.
'''

import math

def compute_Dist(lis,pnt):
    '''input: lis = list of tuples representing coordinates of tourist spots
       output: a list of tuples of length 5 is expected to be returned.'''
       
    # Define a function to calculate Euclidean distance
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    # Calculate distance for each tourist spot, keep track of the original index
    distances = [(euclidean_distance(pnt, spot), index, spot) for index, spot in enumerate(lis)]
    
    # Sort by distance, then by original index
    distances.sort(key=lambda x: (x[0], x[1]))
    
    # Get the 5 nearest spots (only the coordinates, without the distance and index)
    nearest_spots = [spot for _, _, spot in distances[:5]]
    
    return nearest_spots




lis = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
pnt = [0,0]
print(compute_Dist(lis,pnt)) # [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
