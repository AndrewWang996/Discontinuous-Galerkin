'''
Author: Andy Wang
Description: Finds the base functions in the reference element


Important Variables
DegreesOfFreedom: [(x_1,y_1), (x_2,y_2), ... ]
Monomials: [(ex_1,ey_1,ez_1), ...]
ReferenceBaseFunctions: [f_1, f_2, ... ]
'''
from globalVars import dimension, order
from numpy.linalg import inv
from Polynomial import Polynomial

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
		# def baseFunc(x,y):
		# 	s = 0
		# 	for i in range( len(Monomials) ):
		# 		C = column[i]
		# 		(ex,ey) = Monomials[i]
		# 		s += C * (pow(x,ex) * pow(y,ey))
		# 	return s
		# ReferenceBaseFunctions.append(baseFunc)
		ReferenceBaseFunctions.append( Polynomial(column, Monomials) )

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
		# def baseFunc(x,y,z):
		# 	s = 0
		# 	for i in range( len(Monomials) ):
		# 		C = column[i]
		# 		(ex,ey,ez) = Monomials[i]
		# 		s += C * (pow(x,ex) * pow(y,ey) * pow(z,ez))
		# 	return s
		# ReferenceBaseFunctions.append(baseFunc)
		ReferenceBaseFunctions.append( Polynomial(column, Monomials) )





