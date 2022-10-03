# Python program to print magic square of double order

def MSN(n):    #6 for
	          
	
    
	arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]

	# Change value of array elements at fix location
	# as per the rule (n*n+1)-arr[i][[j]
	
	# Corners of order (n/4)*(n/4)
	# Top left corner
	for i in range(0,n//4):
		for j in range(0,n//4):
			arr[i][j] = (n*n + 1) - arr[i][j];
	
	# Top right corner
	for i in range(0,n//4):
		for j in range(3 * (n//4),n):
			arr[i][j] = (n*n + 1) - arr[i][j];

	# Bottom Left corner
	for i in range(3 * (n//4),n):
		for j in range(0,n//4):
			arr[i][j] = (n*n + 1) - arr[i][j];
	
	# Bottom Right corner
	for i in range(3 * (n//4),n):
		for j in range(3 * (n//4),n):
			arr[i][j] = (n*n + 1) - arr[i][j];
			
	# Centre of matrix,order (n/2)*(n/2)
	for i in range(n//4,3 * (n//4)):
		for j in range(n//4,3 * (n//4)):
			arr[i][j] = (n*n + 1) - arr[i][j];
	
	# Printing the square
	for i in range(n):
		for j in range(n):
			print ('%2d ' %(arr[i][j]),end=" ")
		print()
		
# Driver Program
n=7

MSN(n)
print("This is the end of the program")

