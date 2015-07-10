'''
Author: Andy Wang
Description: Polynomial class created for integration of base functions


Important Classes
Polynomial: {(0,2): 6, (1,1): 7} = 7 xy + 6 y^2
'''

from copy import deepcopy as COPY
from globalVars import dimension

class Polynomial:

	def __init__(self, coeffs, expos):
		if len(coeffs) != len(expos):
			raise Error("length of coefficients list" + 
				" not equal to length of exponents list")
		self.Monomials = dict()
		for i in range( len(coeffs) ):
			if expos[i] in self.Monomials:
				self.Monomials[expos[i]] += coeffs[i]
			else:
				self.Monomials[expos[i]] = coeffs[i]

	def __str__(self):
		return " + ".join(str(self.Monomials[expo]) + "*" + str(expo) for expo in self.Monomials )


	def __add__(self, poly):
		newPoly = self.copy()

		for expo in poly.Monomials:
			coeff = poly.Monomials[expo]

			if expo in newPoly.Monomials:
				newPoly.Monomials[expo] += coeff
			else:
				newPoly.Monomials[expo] = coeff

		return newPoly

	def __mul__(self, poly):
		newPoly = Polynomial([], [])

		for expoB in poly.Monomials:
			coeffB = poly.Monomials[expoB]

			coeffs, expos = [], []
			for expoA in self.Monomials:
				coeffA = self.Monomials[expoA]
				coeffs.append(coeffA * coeffB)
				expos.append( tuple(expoA[i] + expoB[i] for i in range( len(expoA) ) ) )

			nPoly = Polynomial(coeffs, expos)
			newPoly = newPoly + nPoly

		return newPoly

	def __pow__(self, n):
		result = self.identity()
		if n < 16:
			for i in range(n):
				result = result * self
			return result

		# use binary exponentiation
		result = self.identity()
		base = self.copy()
		while n > 0:
			if (n & 1) > 0: 
				result = base * result
			base = base * base
			n = (n >> 1)
		return result


	def identity(self):
		return Polynomial([1], [ tuple([0] * dimension) ])


	def copy(self):
		coeffs, expos = [], []

		for expo in self.Monomials:
			expos.append(expo)
			coeffs.append(self.Monomials[expo])

		return Polynomial(coeffs, expos)



