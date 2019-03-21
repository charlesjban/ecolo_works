
# NetworkCreate.py

NetworkCreate - Creates a network file for interactions of variables in a system, based off a table of Correlations (Pearson's or Spearman's coefficients) and their associated P-values. The network file is designed for use with a network visualisation software, such as Cytoscape.

## SYNOPSIS

networkCreate.py mandatory arguments: [-cfile correlationCoefficients.csv] [-pfile coefficentPvalues.csv]  [-networkout Network.file] [-nodeout NodeTypes.file]  [-varfile VariableTypes.txt]
  optional arguments [-pvalue P-value threshold] [-cvalue correlation coefficient threshold]

## DESCRIPTION

NetworkCreate.py is designed to work with the output of the R 'Hmisc' package 'rcorr', which produced two matrices; a correlation coefficient table, and a table of their associated p-values, which should be exported from R as .csv files for use with NetworkCreate. 

## FILES

## ARGUMENTS

## VERSIONS


## AUTHOR
Charles Bannister

	
