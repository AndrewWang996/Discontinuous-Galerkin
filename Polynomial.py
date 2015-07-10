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

	def __neg__(self):
		zipped = [(self.Monomials[expo], expo) for expo in self.Monomials]
		coeffs, expos = zip( * zipped )
		coeffs = [-c for c in coeffs]
		return Polynomial(coeffs, expos)

	def __sub__(self, poly):
		return ( - poly ) + self

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
		if n < 0:
			raise Exception("Negative exponents not allowed.")
		dim = len(self.Monomials.keys()[0])
		result = self.identity(dim)
		if n < 16:
			for i in range(n):
				result = result * self
			return result

		# use binary exponentiation
		result = self.identity(dim)
		base = self.copy()
		while n > 0:
			if (n & 1) > 0: 
				result = base * result
			base = base * base
			n = (n >> 1)
		return result


	def integrate(self, L, U):   	# assuming on the last variable
									# assuming L, U are polynomials
		s = Polynomial([], [])

		poly = self.copy()
		length = -1
		for expo in poly.Monomials:
			coeff = poly.Monomials[expo]
			if length < 0:
				length = len(expo)
			elif length != len(expo):
				raise Exception("Lengths of monomials are different")
			
			lastExponent = expo[-1]
			newExpo = tuple(expo[:-1])
			coeff /= float(lastExponent + 1)

			newPoly = (U ** (lastExponent + 1)) - (L ** (lastExponent + 1))
			s += newPoly * Polynomial([coeff], [newExpo])

		return s



	def identity(self, dim):
		return Polynomial([1], [ tuple([0] * dim) ])


	def copy(self):
		coeffs, expos = [], []

		for expo in self.Monomials:
			expos.append(expo)
			coeffs.append(self.Monomials[expo])

		return Polynomial(coeffs, expos)



# poly = Polynomial([1,1], [(1,0),(0,1)])
# poly = poly.integrate(Polynomial([0],[(0,)]), Polynomial([1,-1], [(0,), (1,)]))
# poly = poly.integrate(Polynomial([0],[()]), Polynomial([1], [()]))
# print poly

# poly += Polynomial([1], [(1,0)])
# print poly

# print poly ** 0
# print poly ** 1
# print poly ** 2

# print poly - poly



