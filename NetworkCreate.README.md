
# NetworkCreate.py

NetworkCreate - Creates a network file for interactions of variables in a system, based off a table of Correlations (Pearson's or Spearman's coefficients) and their associated P-values. The network file is designed for use with a network visualisation software, such as Cytoscape.

## SYNOPSIS

networkCreate.py mandatory arguments: [-cfile correlationCoefficients.csv] [-pfile coefficentPvalues.csv] [-networkout Network.file]
  optional arguments: [-pvalue P-value threshold] [-cvalue correlation coefficient threshold] [-varfile VariableTypes.txt] [-nodeout NodeTypes.file]

## DESCRIPTION

NetworkCreate.py is designed to work with the output of the R 'Hmisc' package 'rcorr', which produced two matrices; a correlation coefficient table, and a table of their associated p-values. These should be exported from R as .csv files for use with NetworkCreate. The program is not exclusive to the output of the 'rcorr' - any two files will work, although it assumes that the list of variables, and their order, in 'x' direction (first row of the table) matches the variables in the 'y' direction (first column of the table), and that the relative positioning of the variables in each of the two files is the same. This means the x = y matrix index for both files is expected to be a 'self-interaction' and is ignored. Users have the option to add a 'variable type' file which is used by Network Create to match each variable to its respective variable type and create 'edge types'. Users have the option to choose a minimum threshold value for the correlation coefficient and its respective p-value.

NetworkCreate.py will return a network in tab-separated-variable format, returning each edge (each variable as node1 and node2), the coefficient value, the p-value, the 'type' of interaction (this will be 'undefined' if node doesn't have a corresponsing variable type in the optional -varfile), and the 'direction' of the relationship (ie a positive correlation or a negative correlation). It was also return a file containing a tab separated table of each of the nodes and the respective variable type, both of which can be loaded into network visualisation software (such as Cytoscape) and used for visualisation and formatted based on edge and node parameters.

## FILE ARGUMENTS

**Mandatory file arguments:**

	[-cfile] Correlation Coefficient File
This should be an existing .csv table of correlation coefficients between each of the variables. It is assumed that the same variables are in the same order in both the x and y directions (ie the 'headers' in the firt row and column respectively). The x=y position will therefore be a value for an interaction between the same variable, so the coefficient will  be 1 and is ignored. 
		
	[-pfile] P-value File
This should be an existing .csv table of p-values which correspond to the correlation coefficients. The positioning of the variables must match that of the correlation table. As with the correlation coefficient table, the x=y position will be a value for an interaction between the same variable, so the p-value will  be 'NA' and is ignored.
	
	[-networkout] Network File
The name of the new network output file.  '.tsv' or '.txt' suffix reccomended.



**Optional file arguments:**

	[-nodeout] Node Types File		file argument must be used in conjuction with [-varfile]
The name of the new node types output file. '.tsv' or '.txt' suffix reccomended.

	[-varfile] Variable Type File			file argument must be used in conjuction with [-nodeout]
This should be an existing plain text file containing 'lists' of each variable type. The first item in the 'list' should be the variable 'type' and the remaining items should be the variables which are of that 'type'. Each list should be on a separate line and variables should be separated by space only (not commas). Eg:

variableType1 variableA variableB variableC
variableType2 variableD variableE variableF
etc...

The same variable should be named exactly as they are in the correlation/pvalue tables, and should not be named under more than one variable 'type' in the varfile. Any variable found in correlation table by NetworkCreate that is not listed in the vartype file will be returned as 'undefined'.


## ADDITIONAL ARGUMENTS
**Optional**
	
	[cvalue] Minimim correlation value threshold
The minimum correlation coefficient value NetworkCreate should consider to include in the network. Default is 0.5, however is is reccomended users choose their own value.
	
	[-pvalue] Minimum p-value threshold
The minimum p-value (associated with a correlation coefficient) that NetworkCreate should consider to include in the network. Default is P = 0.05

## VERSIONS

NetworkCreate.py. Last Updated 21st March 2019

## AUTHORS

Charles Bannister

	
