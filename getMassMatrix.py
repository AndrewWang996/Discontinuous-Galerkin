'''
Author: Andy Wang
Description: Finds the Mass Matrix (the matrix in front
	of the d/dt^2 term)
	Because the Mass Matrix is a block matrix where 
	the blocks are simply the Reference Mass Matrix 
	multiplied by the Jacobian

Important Variables
ReferenceMassMatrix: [[1, 2, ... ];[3, 4, ... ]; ... ]
MassMatrixBlocks: [ [[...]], [[...]], ... ]
'''
from readMesh import Nodes, Elements, Faces, Neighbors
from getBaseFunctions import ReferenceBaseFunctions
from integrals import ReferenceVolumeIntegral
from getJacobians import Jacobians
from numpy.linalg import inv
from numpy import multiply




numBaseFunctions = len(ReferenceBaseFunctions)
ReferenceMassMatrix = [[None for j in range(numBaseFunctions)] for i in range(numBaseFunctions)]


for i, polyI in enumerate(ReferenceBaseFunctions):
	for j, polyJ in enumerate(ReferenceBaseFunctions):
		ReferenceMassMatrix[i][j] = ReferenceVolumeIntegral(polyI * polyJ)

MassMatrixBlocks = []

for J in Jacobians:
	MassMatrixBlock = map(list, multiply(J, ReferenceMassMatrix) )
	MassMatrixBlocks.append( list( MassMatrixBlock ) )













