# Matrismultiplikation

Du har tidigare sett hur matrismultiplikation är definierad och hur matriserna ska vara konstituerade för att matrismultiplikation ska vara definierad. I dessa uppgifter ska du skriva ett program i Python som uför denna matrismultiplikation (utan att använda några fördefinierade funktioner för detta).

## Uppgift 201:1

Detta program som du skriver här ska fungera så att du skapar en funktion `get_element(mat_A, mat_B, i, j)`, där parametrarna `mat_A` och `mat_B` är matriser av typen `ndarray` (som finns definierad i  `NumPy`-biblioteket) och `i, j` är tal som anger den position i resultatmatrisen som efterfrågas (startindex på dessa ska vara 1). Resultatet ska bli ett tal, nämligen det tal som står på plats `(i, j)` i resultatmatrisen.

### Kodskelett 1

```python
import numpy as np

def get_element(mat_A, mat_B, i, j):
    '''
    Parametrar:
        mat_A och mat_B: matriser av typen ndarray
        i och j: rad- och kolonnindex, 1-baserat
    Returvärde:
        Givet att matriserna är multiplicerbara:
            talet på den önskade positionen
        Givet att matriserna inte är multiplicerbara:
            None
    '''
    result = None
    # Här processas matriserna mat_A och mat_B
    # samt att värdet på result uppdateras
    return result

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]])  # 3x2-matris
i, j = 2, 1  # Sökt index, rad och kolonn

# Ändra inget under denna rad,
# men ta gärna inspiration till det som
# behöver skrivas i funktionen get_element.
number_of_rows_in_A = A.shape[0]
number_of_cols_in_B = B.shape[1]

if i <= number_of_rows_in_A and i > 0 and j <= number_of_cols_in_B and j > 0:
    c_ij = get_element(A, B, i, j)
    if c_ij != None:
        # Skriver ut talet 64 givet
        # ingångsvärdena som de var från början
        print(c_ij)
    else:
        print("De angivna matriserna är inte multiplicerbara med varandra")
else:
    print("Begärt index finns ej i resultatmatrisen")
print("Programmet avslutades normalt")
```

Matriserna `A` och `B` ska kunna ges med valfritt antal rader och kolonner.

Du kommer att behöva tillgång till antalet rader och kolonner i respektive matris. Dessa kan erhållas på två sätt:

```python
antal_rader = A.shape[0] # Ger antaler rader i A
antal_kolonner = A.shape[1] # Ger antalet kolonner i A
# eller:
antal_rader = len(A[:, 0]) # "Kolonnlängden"
antal_kolonner = len(A[0]) # "Radlängden"
```

De senare alternativet ger en "dellista" som innehåller raderna respektive kolonnerna, antalet element i dessa listor (`len`) blir då antalet rader respektive kolonner. Ibland kan själva innehållet i dellistan vara intressant, nu vet ni hur det erhålls!

En annan vanlig operation är att *transponera* matriser. Detta fungerar så här:

```python
import numpy as np
A = np.array([[a11, a12], [a21, a22]])
# A är nu
# [[a11, a12],
#  [a21, a22]]

# Transponera nu A:
A = A.T
# A är nu
# [[a11, a21],
#  [a12, a22]]
# dvs raderna blir kolonner och vice versa.
```

## Uppgift 201:2

I denna uppgift ska du skapa själva matrisprodukten, som en matris alltså. Utgå från ditt förra program, dvs du ska fortfarande ha kvar funktionen `get_element`, men skapa också funktionen `make_mat_product(mat_A, mat_B)`.

### Kodskelett 2

```python
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
    # Ta reda på antalet rader och kolonner
    # för resultatmatrisen (givet att mat_A och mat_B
    # är multiplicerbara) 
    result = np.zeros([antal_rader, antal_kolonner])

    # Processa multiplikationen genom upprepade
    # anrop till get_element. Uppdatering av
    # innehållet i result.
    return result

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
    return result

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]])  # 3x2-matris

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
```

Som du ser i kodskelettet ovan så ska du använda dig av den tidigare implementerade funktionen `get_element` när matrisen skapas (om den går att skapa, förstås). I exemplet skapas också en initial resultatmatris, med rätt antal rader och kolonner, som fylls med nollor. För att ändra en nolla till ett annat värde så kan följande utföras:

```python
result[i, j] = nytt_tal
```

Dessa `i` (radindex) och `j` (kolonnindex) är matrisens index; dessa index startar på noll.
