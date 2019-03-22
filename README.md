# ecolo_works
A small collection of programs which creates networks for analysis, from variable-variable correlation coefficient tables

Please see individual .README.md files for full functionality of each program.


**NetworkCreate.py:**

Network Create is designed to work with the output of the R 'Hmisc' package 'rcorr', to produce a network in tab-separated-variable format, returning each edge (each variable as node1 and node2), the coefficient value, the p-value, the 'type' of interaction (this will be 'undefined' if node doesn't have a corresponsing variable type in the optional -varfile), and the 'direction' of the relationship (ie a positive correlation or a negative correlation). It was also return a file containing a tab separated table of each of the nodes and the respective variable type, both of which can be loaded into network visualisation software (such as Cytoscape) and used for visualisation and formatted based on edge and node parameters.


**NetworkMerger.py**

Network Merger will merge networks created by 'NetworkCreate.py', track the number of occurences of each edge, and report and conflicting correlation 'directions' (positive or negative correlations).
