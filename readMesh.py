'''
Author: Andy Wang
Description: Parses mesh files into Python lists



Important Variables:
Nodes (x,y)
Elements ( (node_index_1, node_index_2, node_index_3), attribute)
Faces (node_index_1, node_index_2)
Neighbors (element_index_1, element_index_2, element_index_3)
'''
from globalVars import meshPath, meshName, dimension
import re

filePath = meshPath + meshName + ".1"

'''
Nodes
(x, y)
(x, y, z)
'''
firstLine = True
numLines = 0
Nodes = []
for line in open(filePath + ".node"):
	if firstLine:
		n = int( line.split(" ")[0] )
		firstLine = False
		continue

	line = re.split(" +", line.strip())
	t = map(float, line[1 : dimension + 1])
	Nodes.append( tuple(t) )

	numLines += 1
	if numLines >= n:
		break



'''
Elements
((node_index_0, node_index_1, node_index_2), attribute)
((node_index_0, node_index_1, node_index_2, node_index_3), attribute)
'''
firstLine = True
numLines = 0
Elements = []
for line in open(filePath + ".ele"):
	if firstLine:
		n = int( line.split(" ")[0] )
		firstLine = False
		continue

	line = re.split(" +", line.strip())
	t = [int(node_index) - 1 for node_index in line[1:] ]
	t, attr = tuple( sorted( t[ : 1 + dimension] ) ), t[1 + dimension]
	Elements.append( (t, attr) )

	numLines += 1
	if numLines >= n:
		break

'''
Faces
(node_index_0, node_index_1)
(node_index_0, node_index_1, node_index_2)
'''
firstLine = True
numLines = 0
Faces = []
for line in open(filePath + ".edge"):
	if firstLine:
		n = int( line.split(" ")[0] )
		firstLine = False
		continue

	line = re.split(" +", line.strip())
	t = [int(node_index) - 1 for node_index in line[1 : 1 + dimension] ]
	Faces.append( tuple( sorted(t) ) )

	numLines += 1
	if numLines >= n:
		break


'''
Neighbors
(element_index_0, element_index_1, element_index_2)
(element_index_0, element_index_1, element_index_2, element_index_3)
'''
firstLine = True
numLines = 0
Neighbors = []
for line in open(filePath + ".neigh"):
	if firstLine:
		n = int( line.split(" ")[0] )
		firstLine = False
		continue

	line = re.split(" +", line.strip())
	t = [int(element_index) - 1 for element_index in line[1:]]
	t = sorted(element_index for element_index in t if element_index != -2)
	Neighbors.append( tuple(t) )

	numLines += 1
	if numLines >= n:
		break



'''
Poly
eh, this is basically a summary of all the information above
'''
firstLine = True
numLines = 0
for line in open(filePath + ".poly"):
	if firstLine:
		n = int( line.split(" ")[0] )
		firstLine = False
		continue

	line = re.split(" +", line.strip())

	numLines += 1
	if numLines >= n:
		break




