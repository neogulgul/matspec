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

	''' kod vi skrivit: start '''
	# några variabler
	rows_A = mat_A.shape[0]
	cols_A = mat_A.shape[1]
	rows_B = mat_B.shape[0]
	cols_B = mat_B.shape[1]
	rows_C = rows_A # antalet rader i resultat matrisen är densamma som antalet rader i den första matrisen
	cols_C = cols_B # antalet kolonner i resultat matrisen är densamma som antalet kolonner i den andra matrisen

	if cols_A == rows_B: # kollar att matriserna går att mutliplicera med varandra
		mat_C = np.zeros([rows_C, cols_C]) # skapar resultat matrisen

		for row in range(rows_C): # för varje rad...
			for col in range(cols_C): # och varje kolonn...
				# anropar vi funktionen get_element och
				# tilldelar värdet till den korresponderande
				# positionen i resultat matrisen
				mat_C[row][col] = get_element(mat_A, mat_B, row + 1, col + 1)
	''' kod vi skrivit: slut '''

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
