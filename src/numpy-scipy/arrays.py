import numpy as np


def main():

	# Manual way to create Arrays

	a = np.array([1,2,3])         						# Creates a rank 1 array
	print type(a)										# Prints "<type 'numpy.ndarray'>"
	print a.shape										# (3,)
	print a[0], a[1]


	b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
	print b.shape                     # Prints "(2, 3)"
	print b[0, 0], b[0, 1], b[1, 0]   # Prints "1 2 4"





	# Inbuilt methods to create arrays
	

	a = np.zeros((2,2))  # Create an array of all zeros
	print a              # Prints "[[ 0.  0.]
	                     #          [ 0.  0.]]"
	    
	b = np.ones((1,2))   # Create an array of all ones
	print b              # Prints "[[ 1.  1.]]"

	c = np.full((2,2), 7) # Create a constant array
	print c               # Prints "[[ 7.  7.]
	                      #          [ 7.  7.]]"

	d = np.eye(2)        # Create a 2x2 identity matrix
	print d              # Prints "[[ 1.  0.]
	                     #          [ 0.  1.]]"
	    
	e = np.random.random((2,2)) # Create an array filled with random values
	print e                     # Might print "[[ 0.91940167  0.08143941]
	                            #               [ 0.68744134  0.87236687]]"






	#  Array indexing





if __name__ == "__main__":
	main()
