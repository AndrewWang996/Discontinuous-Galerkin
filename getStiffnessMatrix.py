'''
Author: Andy Wang
Description: Finds the Stiffness Matrix (the matrix in front
	of the term with no time derivative)
Note: When calculating the actual StiffnessMatrix, do not forget that
	there is an element-dependent 'c' term representing the velocity
	of the P waves.

Important Variables
ReferenceStiffnessMatrix: [[1, 2, ... ];[3, 4, ... ]; ... ]
StiffnessMatrixBlocks: [ [[...]], [[...]], ... ]
'''
from sympy.physics.vector import gradient, Vector
from sympy.physics.mechanics import dot
from numpy import multiply, transpose
from numpy.linalg import inv
from globalVars import R, N, Zero, dimension
from getBaseFunctions import ReferenceBaseFunctions, ReferenceGradients
from integrals import ReferenceVolumeIntegral
from getJacobians import Jacobians, Dilations

numBaseFunctions = len(ReferenceBaseFunctions)
ReferenceStiffnessMatrix = [[None for j in range(numBaseFunctions)] for i in range(numBaseFunctions)]

for i, polyI in enumerate(ReferenceBaseFunctions):
	for j, polyJ in enumerate(ReferenceBaseFunctions):
		gradientDotProduct = dot( gradient(polyI, R), gradient(polyJ, R) )
		ReferenceStiffnessMatrix[i][j] = ReferenceVolumeIntegral(gradientDotProduct)

StiffnessMatrixBlocks = []

def matrixToVectorList(m):
	if len(m) == 0:
		return m
	iterator = ( m[j][i] * N[j] for j in range( len(m) ) )
	return [sum(iterator, Zero) for i in range( len(m[0]) )]

for J, A in zip(Jacobians, Dilations):
	invA = matrixToVectorList(inv(A))

	invAGradientProducts = []
	for i, gradI in enumerate(ReferenceGradients):
		product = sum( (dot(invA[i], gradI) * N[i] for i in range(dimension) ), Zero )
		invAGradientProducts.append(product)

	StiffnessMatrixBlock = [[None for j in range(numBaseFunctions)] for i in range(numBaseFunctions)]
	for i, lhs in enumerate(invAGradientProducts):
		for j, rhs in enumerate(invAGradientProducts):
			dotProduct = dot( lhs, rhs )
			StiffnessMatrixBlock[i][j] = ReferenceVolumeIntegral(dotProduct)

	StiffnessMatrixBlock = map(list, multiply(J, StiffnessMatrixBlock) )
	StiffnessMatrixBlocks.append( list( StiffnessMatrixBlock ) )







