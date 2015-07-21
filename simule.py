'''
Author: Andy Wang
Description: Main program: Finds solution to Acoustic Wave Equation. 
'''
import readMesh    			# run readMesh.py
import readData    			# run readData.py
import getBaseFunctions 	# run getBaseFunctions.py
import getJacobians			# run getJacobians.py
import getMassMatrix    	# run getMassMatrix.py
import getStiffnessMatrix   # run getStiffnessMatrix.py
import getDampingMatrix     # run getDampingMatrix.py


from readMesh import Nodes, Elements, Faces, Neighbors
from readData import Tags
from getBaseFunctions import ReferenceBaseFunctions
from getJacobians import Jacobians
from getMassMatrix import ReferenceMassMatrix
from getStiffnessMatrix import ReferenceStiffnessMatrix

from globalVars import X,Y,Z


print X,Y,Z


'''

'''










