import numpy as np

def make_mat_product(mat_A, mat_B):
	'''
	Parametrar:
		mat_A och mat_B: matriser av typen ndarray
	Returvärde:
		Givet att matriserna är multiplicerbara:
			matris av typen ndarray, som utgör
			matrisprodukten
		Givet att matriserna inte är multiplicerbara:
				None
	'''
	mat_C = None
	# Ta reda på antalet rader och kolonner
	# för resultatmatrisen (givet att mat_A och mat_B
	# är multiplicerbara)

	rows_A = mat_A.shape[0]
	cols_A = mat_A.shape[1]
	rows_B = mat_B.shape[0]
	cols_B = mat_B.shape[1]
	rows_C = rows_A
	cols_C = cols_B

	if cols_A == rows_B:
		mat_C = np.zeros([rows_C, cols_C])

		for row in range(rows_C):
			for col in range(cols_C):
				mat_C[row][col] = get_element(mat_A, mat_B, row + 1, col + 1)

	# Processa multiplikationen genom upprepade
	# anrop till get_element. Uppdatering av
	# innehållet i result.
	return mat_C

def get_element(mat_A, mat_B, i, j):
	'''
	Parametrar:
		mat_A och mat_B: matriser av typen ndarray
		i och j: index, 1-baserat
	Returvärde:
		Givet att matriserna är multiplicerbara:
			talet på den önskade positionen
		Givet att matriserna inte är multiplicerbara:
			None
	'''
	result = None
	# Här processas matriserna mat_A och mat_B
	# samt att värdet på result uppdateras

	cols_A = mat_A.shape[1]
	rows_B = mat_B.shape[0]

	if cols_A == rows_B:
		result = 0
		for col in range(cols_A):
			result += A[i - 1][col] * B[col][j - 1]

	return result

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]]) # 3x2-matris

# Ändra inget under denna rad,
C = make_mat_product(A, B)
if C is None:
	print("De angivna matriserna är inte multiplicerbara med varandra")
else:
	print(f"C =\n {C}")
	# Skriver ut
	# [[28. 34.]
	# [64. 79.]]
	# givet matriserna A och B som de var från början
print("Programmet avslutades normalt")
