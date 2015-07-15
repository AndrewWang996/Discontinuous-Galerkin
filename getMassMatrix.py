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
from readMesh import Nodes, Elements, Edges, Neighbors
from getBaseFunctions import ReferenceBaseFunctions
from copy import deepcopy as COPY
from numpy.linalg import det

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

xL, xU = 0, 1
yL, yU = 0, 1-X
zL, zU = 0, 1-X-Y

if dimension == 2:
	for i, polyI in enumerate(ReferenceBaseFunctions):
		for j, polyJ in enumerate(ReferenceBaseFunctions):
			integral = polyI * polyJ
			integral = integrate(integral,(Y,0,1-X))
			integral = integrate(integral,(X,0,1))
			ReferenceMassMatrix[i][j] = float(integral)

elif dimension == 3:
	for i, polyI in enumerate(ReferenceBaseFunctions):
		for j, polyJ in enumerate(ReferenceBaseFunctions):
			integral = polyI * polyJ
			integral = integrate(integral,(Z,0,1-X-Y))
			integral = integrate(integral,(Y,0,1-X))
			integral = integrate(integral,(X,0,1))
			ReferenceMassMatrix[i][j] = float(integral)














