'''
Author: Andy Wang
Description: Main program: Finds solution to Acoustic Wave Equation. 
'''
import readMesh    			# run readMesh.py
import readData    			# run readData.py
import getBaseFunctions # run getBaseFunctions.py
import getMassMatrix    # run getMassMatrix.py

from readMesh import Nodes, Elements, Faces, Neighbors
from readData import Tags
from getBaseFunctions import ReferenceBaseFunctions
from getMassMatrix import Jacobians, ReferenceMassMatrix

from globalVars import X,Y,Z


print X,Y,Z


'''

'''










