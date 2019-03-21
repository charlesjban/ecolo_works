### networkCreate.py
### generates an undirected network in the form of a TSV text file
### input should be 2 .csv files, the output from "Hmisc"package in R:
###  	- pearsons corrlelation coefficient between variabes
###  	- corresponding p-values

import csv
import math
import argparse
import sys

## create arguments
options = argparse.ArgumentParser(description='Create a .tsv network file for network analysis, from correlation and p-value .csv matrix')
options.add_argument("-pfile", help="choose p-value.csv file ", default = None)
options.add_argument("-cfile", help="choose coeff.csv file ", default = None) 
options.add_argument("-pvalue", help="choose a p-value cutoff, default is 0.05", default=0.05)
options.add_argument("-cvalue", help="choose a correlation coefficient cutoff value, default is 0.5", default = 0.5)
options.add_argument("-networkout", help="choose name of output networkfile", default = None)
options.add_argument("-nodeout", help="choose name of output node table file", default = None)
options.add_argument("-varfile", help="choose a file to assign a variable label type to outout table", default = None)
args = options.parse_args()

## check that madatory arguments are present
if args.pfile == None or args.cfile == None or args.networkout == None:
	sys.exit("\nMissing arguments. Mandatory arguments are:\n-pfile\t-cfile\t-networkout\n\nSee .readme or use -help for more info")

if args.varfile != None and args.nodeout == None or args.varfile == None and args.nodeout != None:
	sys.exit("-varfile argument and -nodeout argument must both be present or absent")


networkFile = open(args.networkout, "w")
## Create 2 indexed lists:
##  one for the variable types
##  one list of lists of the variables

if args.varfile != None:
	VarFile = open(args.varfile, "r")
	VarFileLists = VarFile.readlines()

# lists of each type of variable
varLists = []
# Names of the variable types
varTypes = []

# add the corresponding variables to the lists
if args.varfile != None:
	for i in range(0,(len(VarFileLists))):
		split = VarFileLists[i].split(" ")
		varTypes.insert(i, split[0].strip(":"))
		varLists.insert(i, split[1:])

# create nodetype output file and add each node and corresponding type as table
if args.varfile != None:
	nodeType = open(args.nodeout, "w")
	print('Variable\tVariable Type', file = nodeType)
	for i in range(0,len(varTypes)):  # i is variable type
		for var in varLists[i]:
			print("%s\t%s"%(var.strip("\n"), varTypes[i]), file = nodeType)



### open input csv files and assign rows to create a list lists (ie a matrix)
with open(args.pfile, newline='') as csvfile:
    pValues = list(csv.reader(csvfile))
with open(args.cfile, newline='') as csvfile:
    coefficients = list(csv.reader(csvfile))

## create Node class to be passed a string (its name)
class Node:
	def __init__(node, name):
		node.name = name
## create Edge class to be passed two nodes, and their corresponsing coefficient and p values
class Edge:
	def __init__(edge, node1, node2, coeff, pVal, interactionType, correlationDirection):
		edge.node1 = node1
		edge.node2 = node2
		edge.coeff = coeff
		edge.pval = pVal
		edge.interactionType = interactionType
		edge.correlationDirection = correlationDirection


# list to contain edges (should contain no duplicates)
edgeList = []
# counter for NA values    has this been used???

## print coloumn headings
print("Node 1\tNode 2\tCorrelation Coefficient\tP-value\tInteraction Type\tCorrelation direction", file=networkFile)
## for each value in the matrix
for i in range(1,len(coefficients[0])):
	for j in range(1,len(coefficients[i])):
		# use of try as some values are 'NA'
		try:
			coefValue = float(coefficients[i][j])
			pVal = float(pValues[i][j])
		# error exception
		except:
			## print variables which contained NAs (apart from those which would be expected to ie variable-variable)
			if i != j:
				print("The correlation/P-value between %s and %s returned an error and was not be considered. Most likely an 'NA' value"%(coefficients[i][0],coefficients[0][j]))	

		## if coefficient and p values are above cutoff, create new nodes and an edge
		if (coefValue > float(args.cvalue) or coefValue < -float(args.cvalue)) and i != j:
		#and pVal < float(args.pvalue):
			var1Name = (coefficients[i][0]).strip()
			newNode1 = Node(var1Name)
			var2Name = (coefficients[0][j]).strip()
			newNode2 = Node(var2Name)
			## determine if the correlation is positive or negative
			if coefValue > 0:
				direction = "positive"
			elif coefValue < 0:
				direction = "negative"
			
			## determine and assign the interaction type from the input variable type file
			var1Type = "undefined"
			var2Type = "undefined"
			## for each ovf the vartypes in lists, if it matches the variables, assign it as the variable type
			if args.varfile != None:
				for k in range(0,len(varTypes)):
					for var in varLists[k]:
						if var1Name == var:
							var1Type = varTypes[k]
						if var2Name == var:
							var2Type = varTypes[k]

			# create a new edge with the above parameters
			newEdge = Edge(newNode1, newNode2, coefValue, pVal,("%s-%s"%(var1Type, var2Type)), direction)

			## add edge to the edgelist, only if the previous edge does not exist
			edgeHolder = None
			for existingEdge in edgeList:
				if (str(existingEdge.node1.name) == newNode1.name and existingEdge.node2.name == newNode2.name) or (existingEdge.node2.name == newNode1.name and existingEdge.node1.name == newNode2.name):
					edgeHolder = "this is an unused string"
			if edgeHolder == None:
				edgeList.append(newEdge)
		

## output each edge and corresponsing components to output network file
for edge in edgeList:
	print("%s\t%s\t%s\t%s\t%s\t%s" %  (edge.node1.name, edge.node2.name, edge.coeff, edge.pval, edge.interactionType, edge.correlationDirection), file = networkFile)
networkFile.close()
if args.varfile != None:
	nodeType.close()

