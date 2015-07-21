from math import exp
from sympy.physics.vector import ReferenceFrame
from sympy import symbols, Symbol

R = ReferenceFrame('R')
X,Y,Z = R[0], R[1], R[2]
N = [R.x, R.y, R.z]
Zero = 0 * N[0]

dimension = 2
order = 1

meshPath = "../MAILLAGES/"
meshName = "couches5"


sourceFunction = lambda t: exp( - t * t )

'''



'''