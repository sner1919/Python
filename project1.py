import math
import sys
import numpy as np
import matplotlib.pyplot as plt


def array_construction(reference,rule_bits):
	if reference == "[1 1 1]":
		result = int(rule_bits[0])
	elif reference == "[1 1 0]":
		result = int(rule_bits[1])
	elif reference == "[1 0 1]":
		result = int(rule_bits[2])
	elif reference == "[1 0 0]":
		result = int(rule_bits[3])
	elif reference == "[0 1 1]":
		result = int(rule_bits[4])
	elif reference == "[0 1 0]":
		result = int(rule_bits[5])
	elif reference == "[0 0 1]":
		result = int(rule_bits[6])
	elif reference == "[0 0 0]":
		result = int(rule_bits[7])

	return result
	
def main(input):
	#reset the first row
	rule = int(input[1])
	rows = int(input[2])
	cols = 2*(rows-1)+3
	rule_bits = '{0:08b}'.format(rule) #convert the rule into 8 bits binary
	myarray = np.zeros((rows,cols),dtype=int)
	myarray[0,cols/2] = 1
	for x in range(1,rows):
		row_buffer = np.array([0]+myarray[x-1].tolist()+[0])
		for i in range(0,cols-1):
			unit = str(row_buffer[[i,i+1,i+2]])
			myarray[x,i] = array_construction(unit,rule_bits)
	
	return myarray	

input = sys.argv
myarray = main(input)		
		
# Plot black and white pixel 
plt.imshow(myarray,cmap='Greys',interpolation='nearest')
plt.show()

# Standard output the result as a portable bitmap
numrows = len(myarray)
numcols = len(myarray[0])
header = "p1"+" "+str(numrows)+" "+str(numcols)
print header
print "\n".join(" ".join(str(el) for el in row) for row in myarray.tolist())