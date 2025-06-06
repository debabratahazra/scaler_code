
import numpy as np

X = np.array( [ [ 1, -1], [-1, 1], [2, 2], [-2, -2] ] )
cov_x = np.dot(X.T, X) / (len(X)-1)
eigenval,eigenvec=np.linalg.eig(cov_x)
print(f"eigen value={eigenval} and eigen vector={eigenvec}")