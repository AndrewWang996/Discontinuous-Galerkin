'''
Author: Andy Wang
Description: Finds the base functions in the reference element


Important Variables
DegreesOfFreedom: [(x_1,y_1), (x_2,y_2), ... ]
Monomials: [(ex_1,ey_1,ez_1), ...]
ReferenceBaseFunctions: [Poly_1, Poly_2, ... ]
ReferenceGradients: [Vector_1, Vector_2, ... ]
'''
from globalVars import dimension, order, X, Y, Z, R
from numpy.linalg import inv
from sympy.physics.vector import gradient

DegreesOfFreedom = []
Monomials = []


if dimension == 2:
	for i in range(order+1):
		for j in range(order+1):
			if i + j > order:
				break
			t = map(lambda x: x/float(order), [i,j] )
			DegreesOfFreedom.append( tuple(t) )
			Monomials.append( (i,j) )

elif dimension == 3:
	for i in range(order+1):
		for j in range(order+1):
			for k in range(order+1):
				if i + j + k > order: 
					break
				t = map(lambda x: x/float(order), [i,j,k] )
				DegreesOfFreedom.append( tuple(t) )
				Monomials.append( (i,j,k) )


ReferenceBaseFunctions = []
ReferenceGradients = []

if dimension == 2:
	for i in range( len(DegreesOfFreedom) ):
		matrix = []
		for (x,y) in DegreesOfFreedom:
			row = []
			for (ex,ey) in Monomials:
				row.append( pow(x,ex) * pow(y,ey) )
			matrix.append(row)
		inverse = inv(matrix)
		column = list( inverse[:,i] )       # inverse * vector

		expression = sum( column[i] * pow(X, Monomials[i][0]) 
									* pow(Y, Monomials[i][1]) 
										for i in range( len(column) ) )
		ReferenceBaseFunctions.append( expression )
		ReferenceGradients.append( gradient(expression, R) )

elif dimension == 3:
	for i in range( len(DegreesOfFreedom) ):
		matrix = []
		for (x,y,z) in DegreesOfFreedom:
			row = []
			for (ex,ey,ez) in Monomials:
				row.append( pow(x,ex) * pow(y,ey) * pow(z,ez) )
			matrix.append(row)
		inverse = inv(matrix)
		column = list( inverse[:,i] )       # inverse * vector

		expression = sum( column[i] * pow(X, Monomials[i][0])
									* pow(Y, Monomials[i][1])
									* pow(Z, Monomials[i][2])
										for i in range( len(column) ) )
		ReferenceBaseFunctions.append( expression )
		ReferenceGradients.append( gradient(expression, R) )





