---
description: In questa lezione parleremo di come la libreria NumPy ci permette di manipolare matrici e tensori multidimensionali.
---

# 2.2.2 - Gli Array

Nella [lezione precedente](01_intro.md) abbiamo introdotto il concetto di array, la struttura dati "centrale" nell'ecosistema di NumPy. In questa lezione esploreremo come crearli, ispezionarli e manipolarli in modo efficiente.

## Creazione di un Array

Il metodo più immediato per creare un array è l'uso del costruttore `np.array()` a cui passare una lista Python:

```py
>>> import numpy as np
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> a
array([1, 2, 3, 4, 5, 6])
```

Passando una lista di liste, otteniamo un array bidimensionale (una matrice):

```py
>>> b = np.array([[1, 2, 3], [4, 5, 6]])
>>> b
array([[1, 2, 3],
       [4, 5, 6]])
```

### Upcasting (Conversione automatica)

A differenza delle liste, gli array NumPy *devono* contenere dati omogenei. Cosa succede se passiamo una lista con tipi misti, come un intero e un decimale?

```py
>>> d = np.array([1, 3.14])
>>> d
array([1.  , 3.14])
```

NumPy applica il principio dell'**upcasting**: converte automaticamente tutti gli elementi al tipo di dato più "capiente" per evitare perdita di informazioni. In questo caso, l'intero `1` è diventato il float `1.0`.

Se mescoliamo numeri e stringhe, tutto diventerà una stringa:

```py
>>> e = np.array([1, "python"])
>>> e
array(['1', 'python'], dtype='<U21')
```

## Ispezionare un Array (Shape, Ndim, Size)

Quando lavoriamo con dataset complessi (es. batch di immagini), è fondamentale conoscere la geometria dei nostri dati. NumPy offre tre attributi fondamentali:

```py
>>> matrice = np.array([[1, 2, 3],[4, 5, 6]])

>>> matrice.ndim  # Numero di dimensioni (Assi)
2

>>> matrice.shape # La forma: (righe, colonne)
(2, 3)

>>> matrice.size  # Numero totale di elementi (2 * 3)
6
```

## Altri metodi di creazione

Oltre a convertire liste esistenti, NumPy offre funzioni ottimizzate per generare array da zero (utilissime per preallocare memoria o creare dati fittizi).

### Zeri, Uni e Vuoti

```py
# Array 3x3 riempito di zeri
>>> z = np.zeros((3, 3))

# Array 2x4 riempito di uni
>>> u = np.ones((2, 4))

# Array non inizializzato (estremamente veloce da creare, 
# contiene i valori "spazzatura" già presenti in quel blocco di RAM)
>>> e = np.empty((2, 2)) 
```

### Generazione di sequenze (`arange` e `linspace`)

In Data Science, queste due funzioni sono onnipresenti per generare assi temporali o griglie di coordinate:

```py
# Come il range() di Python, ma genera un array e accetta numeri decimali
>>> np.arange(0, 10, 2)  # (start, stop_escluso, step)
array([0, 2, 4, 6, 8])

# Genera N numeri equamente distanziati tra due estremi
>>> np.linspace(0, 1, 5) # (start, stop_incluso, numero_di_elementi)
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
```

## Accesso agli elementi (Indexing)

!!!danger "L'Anti-pattern `[ ][ ]`"
    In Python standard, per accedere a una lista di liste scriveremmo `lista[0][1]`. In NumPy, questa sintassi è un **grave errore di performance** perché forza la creazione in memoria di un array temporaneo per la prima riga prima di estrarre la colonna.

La sintassi corretta, veloce e "NumPy-onica" utilizza la virgola per separare le dimensioni: `array[riga, colonna]`.

```py
>>> b = np.array([[10, 20, 30],[40, 50, 60]])

# Voglio l'elemento alla prima riga (indice 0) e seconda colonna (indice 1)
>>> b[0, 1]
20
```

## Slicing Multi-dimensionale

Lo slicing in NumPy (`start:stop:step`) è potentissimo perché agisce simultaneamente su più dimensioni. È la tecnica alla base del ritaglio di immagini (cropping) nella Computer Vision.

```py
>>> b = np.array([[1, 2, 3],
                  [4, 5, 6],[7, 8, 9]])

# Voglio le prime due righe (0:2), ma solo le ultime due colonne (1:)
>>> b[0:2, 1:]
array([[2, 3],[5, 6]])

# Voglio TUTTE le righe (:), ma solo la colonna centrale (1)
>>> b[:, 1]
array([2, 5, 8])
```

## Maschere Booleane (Masking)

Possiamo estrarre sottoinsiemi di dati applicando condizioni logiche. Questo processo crea una "maschera" di `True` e `False`.

```py
>>> b = np.array([1, 2, 3, 4, 5, 6])

# Quali elementi sono maggiori di 3?
>>> mask = b > 3
>>> mask
array([False, False, False,  True,  True,  True])

# Applichiamo la maschera per estrarre i dati
>>> b[mask]
array([4, 5, 6])

# Forma compatta
>>> b[b > 3]
array([4, 5, 6])
```

!!!warning "Operatori Logici in NumPy"
    Per combinare più condizioni sulle maschere, **non** possiamo usare le keyword di Python `and`, `or`, `not`. Dobbiamo usare gli operatori bit-a-bit `&` (AND), `|` (OR), `~` (NOT), assicurandoci di mettere le condizioni tra parentesi tonde:
    ```py
    # Valori pari E maggiori di 2
    >>> b[(b % 2 == 0) & (b > 2)]
    array([4, 6])
    ```

## Sostituzione condizionale: `np.where`

Spesso non vogliamo solo estrarre dati, ma modificarli in base a una condizione (es. "imposta a 0 tutti i valori negativi"). La funzione `np.where(condizione, valore_se_vero, valore_se_falso)` è la soluzione standard:

```py
>>> x = np.array([-2, 5, -1, 8])
>>> np.where(x < 0, 0, x)
array([0, 5, 0, 8])
```

## Fancy Indexing

Chiudiamo con una tecnica avanzata chiamata *fancy indexing*, che permette di usare un array di indici interi per estrarre elementi in un ordine specifico o ripetuto.

Per dimostrarlo, generiamo prima dei dati casuali usando l'API moderna di NumPy per la riproducibilità (`default_rng`):

```py
# Inizializziamo il generatore di numeri casuali (seed=42 per riproducibilità)
>>> rng = np.random.default_rng(42)

# Generiamo 10 numeri interi tra 0 e 100
>>> x = rng.integers(0, 100, size=10)
>>> x
array([ 8, 77, 65, 43, 43, 85,  8, 69, 20,  9])

# Vogliamo estrarre gli elementi agli indici 1, 5 e 2, in quest'ordine
>>> indici = np.array([1, 5, 2])
>>> x[indici]
array([77, 85, 65])
```

La potenza del fancy indexing sta nel fatto che la forma (`shape`) dell'array risultante non dipende dai dati di origine, ma *dall'array degli indici*:

```py
# Passiamo una matrice 2x2 di indici
>>> indici_2d = np.array([[1, 4], 
                          [5, 2]])
>>> x[indici_2d]
array([[77, 43],[85, 65]])
```