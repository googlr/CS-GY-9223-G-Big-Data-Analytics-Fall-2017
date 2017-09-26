#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)
a = []
b = []
for i in range(0,n):
	a.append(0.0)
	b.append(0.0)


currentkey = None
current_x = ''
current_y = ''
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key, value = line.split('\t',1)

	#Parse key/value input (your code goes here)
	x,y = key.split(" ")
	mat,t,val = value.split(" ")
	index = int(t)
        val_f = float(val)




	#If we are still on the same key...
	if key==currentkey:

		#Process key/value pair (your code goes here)
		current_x = x
		current_y = y
		if mat=="A":
			a[index] = val_f
		elif mat=="B":
			b[index] = val_f


	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:

			#compute/output result to STDOUT (your code goes here)
			res = 0
			for j in range(0,n):
				res += a[j]*b[j]
			print '(%s, %s), %s' %(current_x, current_y, res)		


	
		currentkey = key
		current_x = x
		currnet_y = y
		for i in range(0,n):
			a[i] = 0.0
			b[i] = 0.0

		
		#Process input for new key (your code goes here)
		if mat=="A":
                        a[index] = val_f
                elif mat=="B":
                        b[index] = val_f



#Compute/output result for the last key (your code goes here)
res = 0
for j in range(0,n):
	res += a[j]*b[j]
print '(%s, %s), %s' %(current_x, current_y, res)



