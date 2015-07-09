'''
Author: Andy Wang
Description: Reads the physical parameters of each region

Important Variables
Tags Dict{ tag : tuple(physical parameters) }
'''
import re

physicalParametersPath = "./"
f = open(physicalParametersPath + "physicalParameters.dat", "r")

n = int( re.split(" +", f.readline().strip())[0] )

Tags = dict()
for i in range(n):
	line = re.split(" +", f.readline().strip())
	tag = int(line[0])
	Tags[tag] = tuple(line[1:])

