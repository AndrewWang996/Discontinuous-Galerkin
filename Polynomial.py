'''
Author: Andy Wang
Description: Polynomial class created for integration of base functions


Important Classes
Polynomial: {(0,2): 6, (1,1): 7} = 7 xy + 6 y^2
'''
# class Monomial:

# 	def __init__(self, (coeff, expos)):
# 		self.coeff = coeff
# 		self.expos = tuple(expos)

# 	def __str__(self):
# 		return str(self.coeff) + "*" + str(self.expos)

# 	# def __add__(self, monom):
# 	# 	if self.expos == monom.expos:
# 	# 		return Polynomial( [self.coeff + monom.coeff], [self.expos] )
# 	# 	return Polynomial( [self.coeff, monom.coeff], [self.expos, monom.expos] )

# 	def __mul__(self, monom):
# 		expos = [self.expos[i] + monom.expos[i] for i in range( len(self.expos) )]
# 		return Polynomial( [self.coeff * monom.coeff], [expos])
from copy import deepcopy as COPY
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
			newPoly = newPoly.__add__(nPoly)

		return newPoly

	def copy(self):
		coeffs, expos = [], []

		for expo in self.Monomials:
			expos.append(expo)
			coeffs.append(self.Monomials[expo])

		return Polynomial(coeffs, expos)




