'''
Author: Andy Wang
Description: Various nested integrals for use in other modules

Important Functions
ReferenceVolumeIntegral: int int int (f) dV
ReferenceFaceIntegral: int int (f).dS
'''


from sympy import integrate
from globalVars import dimension, X, Y, Z

def ReferenceVolumeIntegral(f):
	if dimension == 2:
		v = integrate(f, (Y,0,1-X))
		v = integrate(v, (X,0,1))
		return float(v)
	elif dimension == 3:
		v = integrate(f, (Z,0,1-X-Y))
		v = integrate(v, (Y,0,1-X))
		v = integrate(v, (X,0,1))
		return float(v)

def ReferenceFaceIntegral(f, i):
	if dimension == 2:
		if i == 0:
			v = f.subs(Y, 0)
			v = integrate(v, (X,0,1))
		elif i == 1:
			v = f.subs(X, 0)
			v = integrate(v, (Y,0,1))
		elif i == 2:
			v = f.subs(Y, 1-X)
			v = integrate(v, (X,0,1))
		else:
			raise Exception("Please enter a value of 'i' in [0,2]")
	elif dimension == 3:
		if i == 0:
			v = f.subs(Z, 0)
			v = integrate(v, (Y,0,1-X))
			v = integrate(v, (X,0,1))
		elif i == 1:
			v = f.subs(Y, 0)
			v = integrate(v, (Z,0,1-X))
			v = integrate(v, (Z,))
		elif i == 2:
			v = f.subs(X, 0)
			v = integrate(v, (Z,0,1-Y))
			v = integrate(v, (Y,0,1))
		elif i == 3:
			v = f.subs(Z, 1-X-Y)
			v = integrate(v, (Y,0,1-X))
			v = integrate(v, (X,0,1))
		else:
			raise Exception("Please enter a value of 'i' in [0,3]")



