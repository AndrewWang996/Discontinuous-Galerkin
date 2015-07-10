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
from globalVars import dimension, order
from readMesh import Nodes, Elements, Edges, Neighbors
from getBaseFunctions import ReferenceBaseFunctions
from Polynomial import Polynomial
from copy import deepcopy as COPY
from numpy.linalg import det

Jacobians = []

if dimension == 2:
	for element in Elements:
		attribute = element[3]
		nI = element[:3]
		points = [Nodes[nI[i]] for i in range(3)]
		b = COPY(points[0])
		A = COPY(points[1:])
		A = [[node[i] - b[i] for i in range(2)] for node in A]
		Jacobian = det(A)
		Jacobians.append(Jacobian)

elif dimension == 3:
	for element in Elements:
		attribute = element[4]
		nI = element[:4]
		points = [Nodes[nI[i]] for i in range(4)]
		b = COPY(points[0])
		A = COPY(points[1:])
		A = [[node[i] - b[i] for i in range(3)] for node in A]
		Jacobian = det(A)
		Jacobians.append(Jacobian)





ReferenceMassMatrix = []

for i, polyI in enumerate(ReferenceBaseFunctions):
	for j, polyJ in enumerate(ReferenceBaseFunctions):
		












