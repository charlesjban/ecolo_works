
# NetworkMerger.py

Network Merger - Merges multiple networks (created by or formatted as the output of NetworkCreate.py) and tracks the number of occurences of each edge and the correlation 'direction' (ie. positive/negative/conflicting). 

## SYNOPSIS

NetworkMerger.py mandatory arguments: [-n1 NetworkFile1] [-n2 NetworkFile2 ]
  optional arguments [-n3 AdditionalNetwork3] ...[-n9 AdditionalNetwork9] [-f MergedNetworkFileName]

## DESCRIPTION

NetworkMerger.py is designed to merge up to 9 network files created by NetworkCreate.py. The resulting output will be a NetworkFile containing each node. It will pass on information about the interaction 'type', and pass on correlation direction,  flagging up any 'conflicting' positive/negative correlations. The number of occurrences of each edge are also counted. As with the individual networks, the merged network file is designed for us with network visualisation software such as Cytoscape, in which conditional visual formatting can be used on nodes/edges highlight their properties, and used for more in-depth network analysis. 

FILEs / ARGUMENTS

**Mandatory file arguments:**

	[-n1] NetworkFile1
The first network file to merge as created by NetworkCreate.py
		
	[-n2] NetworkFile2
The second network file

**Optional file arguments:**

	[-n3]...[n9] Additional network files to merge
Users can choose to add up to 7 additional network files(9 in total) to add by using the argument '-nX additionalFile' where X is a number ranging from 3-9.

  [-f] Network File Name
 Users can choose the name of the merged network file. Default is "MergedNetwork.txt"


## VERSIONS

NetworkMerger.py. Last Updated 22nd March 2019

## AUTHORS

Charles Bannister

	
