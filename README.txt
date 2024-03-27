Tool: miRNA Finder

Utility: 
In .vcf files, the variant position is given w.r.t to the entire genome of the organism. However, most miRNA databases will give the relative binding position to the UTR of the gene.
We utilized the UTR data from UCSC browser and the relative miRNA binding data from miRWalk to create a tool that can find miRNAs binding in the variant location.
This tool has been primarily used to analyze the miRNA binding change(gain or loss of binding site) due to a mutation. 

NOTE: The tool doesn't predict miRNA binding loss or gain. It finds all the miRNA binding to a particular position which currently is not possible from other databases. 

Usage:
Type the following command: python3 find_miRNA.py

Library dependencies: pandas, numpy

i. The input file needs to be a tab-separated file have following columns with headers: ID, chrom, Symbol, Position 
ii. The UTR data and miRNA data should be kept in the same folder as input file(or the path should be given accordingly in the script)
iii. The script is compatible with python3 interpreter 
iv. The output file could be renamed at the last line of the script.
v. The binding probability obtained in the output file is based on the binding of miRNA to the non-mutated sequence.  

Note: A sample for input file(input.tsv) and output file(output.tsv) has been provided. However, due to the large size of the databases for UTR and miRNA they aren't provided. 