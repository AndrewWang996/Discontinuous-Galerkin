from math import exp
from sympy import symbols, Symbol

X,Y,Z = symbols('X Y Z')

dimension = 2
order = 1

meshPath = "../MAILLAGES/"
meshName = "couches5"


sourceFunction = lambda t: exp( - t * t )

'''



'''