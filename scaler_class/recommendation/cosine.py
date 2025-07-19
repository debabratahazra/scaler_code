import numpy as np
from numpy.linalg import norm
 
def cosineSimilarity(A, B):
  """
  Write your code here
  """
  cosSim = np.dot(A, B) / (norm(A) * norm(B))  
  
  return np.round(cosSim,3)


A = np.array([2,1,2,3,2,9])
B = np.array([3,4,2,4,5,5])
cos = cosineSimilarity(A, B)
print(cos)