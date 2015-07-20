'''
Author: Andy Wang
Description: Finds the Stiffness Matrix (the matrix in front
	of the term with no time derivative)
Note: When calculating the actual StiffnessMatrix, do not forget that
	there is an element-dependent 'c' term representing the velocity
	of the P waves.

Important Variables
ReferenceStiffnessMatrix: [[1, 2, ... ];[3, 4, ... ]; ... ]
'''
from globalVars import R
from getBaseFunctions import ReferenceBaseFunctions
from integrals import ReferenceVolumeIntegral
from sympy.physics.vector import gradient
from sympy.physics.mechanics import dot

numBaseFunctions = len(ReferenceBaseFunctions)
ReferenceStiffnessMatrix = [[None for j in range(numBaseFunctions)] for i in range(numBaseFunctions)]

for i, polyI in enumerate(ReferenceBaseFunctions):
	for j, polyJ in enumerate(ReferenceBaseFunctions):
		gradientDotProduct = dot( gradient(polyI, R), gradient(polyJ, R) )
		ReferenceStiffnessMatrix[i][j] = ReferenceVolumeIntegral(gradientDotProduct)







