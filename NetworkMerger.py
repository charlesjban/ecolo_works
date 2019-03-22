import argparse
import sys

## Add network file options 
options = argparse.ArgumentParser(description='Create a .tsv network file for network analysis, from correlation and p-value .csv matrix')
options.add_argument("-n1", help = "Add network file 1", default = None)
options.add_argument("-n2", help = "Add network file 2", default = None)
options.add_argument("-n3", help = "Add network file 3", default = None)
options.add_argument("-n4", help = "Add network file 4", default = None)
options.add_argument("-n5", help = "Add network file 5", default = None)
options.add_argument("-n6", help = "Add network file 6", default = None)
options.add_argument("-n7", help = "Add network file 7", default = None)
options.add_argument("-n8", help = "Add network file 8", default = None)
options.add_argument("-n9", help = "Add network file 9", default = None)
options.add_argument("-f", help = "Name of merged network file", default = "MergedNetwork.txt")
args = options.parse_args()

## check that 2 networks are included
if args.n1 == None or args.n2 == None:
	sys.exit("Error: Please add a minimum of 2 networks. -n1 and -n2 networks arguments are mandatory.")

networkFileNames = [args.n1, args.n2]
 
## add additional file to network File list if file is argument is present
additionalNetworkFileNames = [args.n3, args.n4, args.n5, args.n6, args.n7, args.n8, args.n9]
for arguments in additionalNetworkFileNames:
	if arguments != None:
		networkFileNames.append(args)

## define node class, which just has a name
class Node:
	def __init__(self, name):
		self.name = name

## define edge class
## contains 2 nodes, interaction type, counter, and a direction
class Edge:
	def __init__(self, node1, node2, interType, direction):
		self.node1 = node1
		self.node2 = node2
		self.type = interType
		self.count = 1
		self.direction = direction
	# function to add one to the counter (if edge is encountered again)
	def addOne(self):
		self.count += 1
	# function to change the direction to "conflicting"
	def conflicting(self):
		self.direction = "conflicting"


edgeList = []
networks = []


outfile = open(str(args.f), "w+")
print("Node1\tNode2\tInteraction Type\tInteraction direction\tInstances", file = outfile)

for i in range(0,len(networkFileNames)):
	fileName = networkFileNames[i]
	netFile = open(fileName, "r")
	networks.insert(i, netFile)

for file in networks:
	lines = file.readlines()[1:]
	for line in lines:
		node1 = Node(line.split()[0])
		node2 = Node(line.split()[1])
		corr = line.split()[2]
		pval = line.split()[3]
		interType= line.split()[4]
		direction = line.split()[5]
		# check if the edge already exists
		edgeHolder = None
		for existingEdge in edgeList:
			if (existingEdge.node1.name == node1.name and existingEdge.node2.name == node2.name) or (existingEdge.node2.name == node1.name and existingEdge.node1.name == node2.name):
				# add one to the counter if it does
				existingEdge.addOne()
				edgeHolder = "there was something!"
				# change the direction to conflicting, if it doesn't match
				if existingEdge.direction != direction:
					existingEdge.conflicting()
		# if there was no existing edge with the two nodes, create a new edge and add to the list
		if edgeHolder == None:
			newEdge = Edge(node1, node2, interType, direction)
			edgeList.append(newEdge)
# print edge credentials to output file	
for edge in edgeList:
	print("%s\t%s\t%s\t%s\t%s" %(edge.node1.name, edge.node2.name, edge.type, edge.direction, edge.count), file = outfile)

outfile.close()
	
