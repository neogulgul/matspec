import numpy as np

def dot_product(vec_1, vec_2):
	'''
	Parametrar:
		vec_1: en vektor av typen ndarray
		vec_2: en vektor av typen ndarray
	Returvärde:
		Om vektorerna går att multiplicera skalärt:
			Skalärprodukten
		Om vektorerna inte går att multiplicera skalärt:
			None
	Övrigt: Denna funktion bygger inte på NumPy:s implementering
	av skalärprodukt.
	'''
	result = None
	# Implementera koden nedan

	x1 = vec_1[0]
	y1 = vec_1[1]
	x2 = vec_2[0]
	y2 = vec_2[1]

	result = x1 * x2 + y1 * y2

	return result

def is_orthogonal(koord_axlar):
	'''
	Parameter:
		koord_axlar: en matris av typen ndarray som
		definierar de båda koordinat-axlarnas riktning i kolonnerna
	Returvärde:
		Om ortogonala axlar: True
		Om ej ortogonala axlar: False
	'''
	result = False
	# Här sker kontrollen
	# som eventuellt ställer om variabeln result
	# ...

	if dot_product(koord_axlar[0], koord_axlar[1]) == 0:
		result = True

	return result

def calc_proj(vektor, koord_axlar):
	'''
	Parametrar:
		vektor: en vektor med två komponenter av typen ndarray
		koord_axlar: en matris av typen ndarray som definierar
		de båda koordinat-axlarnas riktning i kolonnerna
	Returvärde:
		En matris av typen ndarray som innehåller projektionen
		på respektive koordinataxel i kolonnerna
	'''
	result = np.zeros([2, 2])
	# Här sker själva beräkningen som lagrar
	# resultatet i variabeln result
	# ...

	y = np.array([vektor[0][0], vektor[1][0]])
	u1 = koord_axlar[0]
	u2 = koord_axlar[1]

	factor = dot_product(y, u1) / dot_product(u1, u1)

	y1 = np.multiply(factor, u1)

	factor = dot_product(y, u2) / dot_product(u2, u2)

	y2 = np.multiply(factor, u2)

	result[0][0] = y1[0]
	result[0][1] = y2[0]
	result[1][0] = y1[1]
	result[1][1] = y2[1]

	return result

# Test-exempel
y = np.array([[3], [2]])
u1 = np.array([4, 1])
u2 = np.array([-1, 4])
u = np.array([u1.T, u2.T])
# Kontrollera hur y och u skrivs ut
# INNAN du börjar skriva funktionerna

### Ändra inget under denna rad
if is_orthogonal(u):
	proj = calc_proj(y, u)
	print(proj.round(2))
	# För en fungerande funktion och givna
	# data enligt räkneexemplet så skrivs ut:
	# [[3.29 -0.29]
	#  [0.82  1.18]]

	print("Längden på ovanstående projektionsvektorer:")
	norm_u1 = round(np.linalg.norm(proj[:, 0]), 2)
	norm_u2 = round(np.linalg.norm(proj[:, 1]), 2)
	print(f"||u1|| = {norm_u1}") # Blir 3.4
	print(f"||u2|| = {norm_u2}") # Blir 1.21
else:
	print("Angivna koordinataxlar är inte ortogonala.")
