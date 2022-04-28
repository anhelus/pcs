# Risoluzione degli esercizi

1. Scriviamo la funzione `calcola_determinante(mat)` che permetta di calcolare il determinante di una matrice $2 \times 2$.

```py
def calcola_determinante(mat):
    if len(mat.shape) == 2 and mat.shape[0] == mat.shape[1] and mat.shape[0] == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    raise ValueError('La matrice non ha le dimensioni attese.')
```

2. Scriviamo la funzione `inverti_se_inveribile(mat)` che, data una matrice bidimensionale, restituisca l'inversa soltanto se `mat` è bidimensionale e quadrata, ed il determinante è diverso da zero. Usare esclusivamente le istruzioni `if`.

```py
def inverti_se_invertibile(mat):
    if len(mat.shape) == 2 \
        and mat.shape[0] == mat.shape[1] \
        and linalg.det(mat) != 0:
        return linalg.inv(mat)
    raise ValueError('La matrice passata non è invertibile.')
```
