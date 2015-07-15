'''
Author: Andy Wang
Description: Finds the Mass Matrix. 
	Because the Mass Matrix is a block matrix where 
	the blocks are simply the Reference Mass Matrix 
	multiplied by the Jacobian

Important Variables
Jacobians: [J_1, J_2, ... ]
ReferenceMassMatrix: [[1, 2, ... ];[3, 4, ... ]; ... ]
'''
from globalVars import dimension, order, X, Y, Z
from readMesh import Nodes, Elements, Faces, Neighbors
from getBaseFunctions import ReferenceBaseFunctions
from integrals import ReferenceVolumeIntegral
from copy import deepcopy as COPY
from numpy.linalg import det
from sympy import integrate

Jacobians = []

if dimension == 2:
	for element, attribute in Elements:
		points = [Nodes[element[i]] for i in range(3)]
		b = COPY(points[0])
		A = COPY(points[1:])
		A = [[node[i] - b[i] for i in range(2)] for node in A]
		Jacobian = det(A)
		Jacobians.append(Jacobian)

elif dimension == 3:
	for element, attribute in Elements:
		points = [Nodes[element[i]] for i in range(4)]
		b = COPY(points[0])
		A = COPY(points[1:])
		A = [[node[i] - b[i] for i in range(3)] for node in A]
		Jacobian = det(A)
		Jacobians.append(Jacobian)





numBaseFunctions = len(ReferenceBaseFunctions)
ReferenceMassMatrix = [[None for j in range(numBaseFunctions)] for i in range(numBaseFunctions)]


for i, polyI in enumerate(ReferenceBaseFunctions):
	for j, polyJ in enumerate(ReferenceBaseFunctions):
		ReferenceMassMatrix[i][j] = ReferenceVolumeIntegral(polyI * polyJ)
















