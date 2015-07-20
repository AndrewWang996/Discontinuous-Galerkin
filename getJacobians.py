'''
Author: Andy Wang
Descriptions: Finds the Jacobians for all the transforms
	from the ReferenceElement to normal Elements. Used 
	to save computational costs.

Important Variables
Jacobians: [J_1, J_2, ... ]
'''
from numpy.linalg import det
from copy import deepcopy as COPY
from globalVars import dimension
from readMesh import Nodes, Elements

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