'''
Author: Andy Wang
Description: Finds the Mass Matrix (the matrix in front
	of the d/dt^2 term)
	Because the Mass Matrix is a block matrix where 
	the blocks are simply the Reference Mass Matrix 
	multiplied by the Jacobian

Important Variables
ReferenceMassMatrix: [[1, 2, ... ];[3, 4, ... ]; ... ]
## MassMatrix: [[1, 2, ... ];[3, 4, ... ]; ... ]
'''
from readMesh import Nodes, Elements, Faces, Neighbors
from getBaseFunctions import ReferenceBaseFunctions
from integrals import ReferenceVolumeIntegral
from numpy.linalg import inv




numBaseFunctions = len(ReferenceBaseFunctions)
ReferenceMassMatrix = [[None for j in range(numBaseFunctions)] for i in range(numBaseFunctions)]


for i, polyI in enumerate(ReferenceBaseFunctions):
	for j, polyJ in enumerate(ReferenceBaseFunctions):
		ReferenceMassMatrix[i][j] = ReferenceVolumeIntegral(polyI * polyJ)

print inv(ReferenceMassMatrix)


# lenMass = len(Jacobians) * len(ReferenceMassMatrix)
# MassMatrix = [[0 for i in range(lenMass)] for j in range(lenMass)]

# for Ji in range(len(Jacobians)):
# 	for i in range(len(ReferenceMassMatrix)):
# 		for j in range(len(ReferenceMassMatrix)):
# 			xy = Ji * len(ReferenceMassMatrix)
# 			MassMatrix[xy + i][xy + j] = Jacobians[Ji] * ReferenceMassMatrix[i][j]















