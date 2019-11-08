#!/urs/bin/env python3

# Replace a column with a single new 

# If line starts with '#', 	copy to new file as is
# If line starts with '#', 	copy columns 1 to 4
#				replace line 5 with '<NON_REF>'
#				copy all columns until end of line


# Load all relevant modules
import os, glob

# Set working directory to that where you need the files changed
path='/home/emma/Desktop/Project/data'
os.chdir(path)

# Set the extension of the files you want to change
for file in glob.glob("*.g.vcf"):

	infile = open(file, 'r')
	outfile = open('%s_not_ref.g.vcf' %infile.name, 'w')
	# output file to write the new data in
	
	# Read line by line
	while True:
		line = infile.readline()
		# If column starts by #, write it all in the output file
		if line[0:1] == '#':
			outfile.write(line + '\n')
		# If column doesn't start by #, change column 5 to <NON_REF>
		else:
			col = line.split('\t')
			# Separate line by tabulation to have every column
			c1to4 = '\t'.join(col[0:4])
			c5 = '<NON_REF>'
			# Set the
			c6toEnd = '\t'.join(col[5:-1])
			# 
			outfile.write(c1to4 + '\t' + c5 + '\t' + c6toEnd + '\n')




