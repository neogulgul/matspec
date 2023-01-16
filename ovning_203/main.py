import numpy as np

# representation av en rät linje
class linear_equation:
	def __init__(self, k, m):
		self.k = k
		self.m = m

	def __str__(self):
		return f"y = {self.k}x + {self.m}"

def least_squares(data):
	sample_size = data.shape[0]

	# A @ X = B => X = A_inv @ B
	# A = x_vals_T @ x_vals
	# B = x_vals_T @ y_vals

	x_vals = np.zeros([sample_size, 2])
	y_vals = np.zeros([sample_size, 1])

	for i in range(sample_size):
		x = data[i][0]
		y = data[i][1]
		x_vals[i] = [1, x]
		y_vals[i] = y

	x_vals_T = x_vals.transpose()

	A = x_vals_T @ x_vals
	B = x_vals_T @ y_vals

	A_inv = np.linalg.inv(A)

	X = A_inv @ B

	k = X[1][0]
	m = X[0][0]

	return linear_equation(k, m)

data = np.array(
	[
		[150.0,  74.3],
		[250.0, 127.0],
		[450.0, 230.0],
		[600.0, 289.0],
		[725.0, 367.0]
	]
)

l = least_squares(data)
print(l)
print("k värde:", round(l.k, 3))
print("m värde:", round(l.m, 3))
