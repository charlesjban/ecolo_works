# ecolo_works
A small collection of programs for network creation and analysis from correlation tables

This currently being created for a Univeristy project
Please see individual .README.md files for full functionality of each program.

Programs are currently under construction and will be added as completed

**NetworkCreate.py:**

NetworkCreate.py is designed to work with the output of the R 'Hmisc' package 'rcorr', which produced two matrices; a correlation coefficient table, and a table of their associated p-values. These should be exported from R as .csv files for use with NetworkCreate. The program is not exclusive to the output of the 'rcorr' - any two files will work, although it assumes that the list of variables, and their order, in 'x' direction (first row of the table) matches the variables in the 'y' direction (first column of the table), and that the relative positioning of the variables in each of the two files is the same. This means the x = y matrix index for both files is expected to be a 'self-interaction' and is ignored. Users have the option to add a 'variable type' file which is used by Network Create to match each variable to its respective variable type and create 'edge types'. Users have the option to choose a minimum threshold value for the correlation coefficient and its respective p-value.

NetworkCreate.py will return a network in tab-separated-variable format, returning each edge (each variable as node1 and node2), the coefficient value, the p-value, the 'type' of interaction (this will be 'undefined' if node doesn't have a corresponsing variable type in the optional -varfile), and the 'direction' of the relationship (ie a positive correlation or a negative correlation). It was also return a file containing a tab separated table of each of the nodes and the respective variable type, both of which can be loaded into network visualisation software (such as Cytoscape) and used for visualisation and formatted based on edge and node parameters.


