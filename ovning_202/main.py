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

	''' kod vi skrivit: start '''
	# endast tillåten båda vektorerna har lika många element
	if (len(vec_1) == len(vec_2)):
		result = 0
		for i in range(len(vec_1)):
			result += vec_1[i] * vec_2[i]
	''' kod vi skrivit: slut '''

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

	''' kod vi skrivit: start '''
	# stämmer om skalärprodukten är lika med noll
	if dot_product(koord_axlar[0], koord_axlar[1]) == 0:
		result = True
	''' kod vi skrivit: slut '''

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

	''' kod vi skrivit: start '''
	# y är den inmattade vektorn fast lite annorlunda eftersom
	# att vi vill ha vektorn i samma form som koordinat axlarna
	# på formen [x y] istället för: [[x]
	#                                [y]]
	y = np.array([vektor[0][0], vektor[1][0]])
	u1 = koord_axlar[0]
	u2 = koord_axlar[1]

	#   y • u1
	# ---------
	#  u1 • u1
	factor = dot_product(y, u1) / dot_product(u1, u1)

	y1 = np.multiply(factor, u1)

	#   y • u2
	# ---------
	#  u2 • u2
	factor = dot_product(y, u2) / dot_product(u2, u2)

	y2 = np.multiply(factor, u2)

	# tilldelar värdena i från projectionen till resultat matrisen
	# [[y11 y21]  | den andra siffran representerar
	#  [y12 y22]] | indexet i respektive matris
	result[0][0] = y1[0]
	result[0][1] = y2[0]
	result[1][0] = y1[1]
	result[1][1] = y2[1]
	''' kod vi skrivit: slut '''

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
