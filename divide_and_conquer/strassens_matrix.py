
#It's a method to multiply two square matrices
#Time Complexity is O(N3)

def multiply(A, B, C):

	for i in range(N):
	
		for j in range( N):
		
			C[i][j] = 0
			for k in range(N):
			
				C[i][j] += A[i][k]*B[k][j]

#
