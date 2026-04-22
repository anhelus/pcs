


Questo file contiene concetti validissimi, ma nasconde alcune "trappole" storiche in cui cadono spessissimo i programmatori quando passano da Python puro a NumPy. 

Inoltre, alcune sezioni erano ripetitive (come `shape` e `ndim`, già viste nel file precedente) e mancavano di alcune *best practices* fondamentali introdotte nelle versioni recenti di Python (come l'operatore `@` per le matrici).

Ecco i **5 interventi chirurgici** che ho applicato per gli standard 2026:

1.  **L'operatore `@` per le Matrici:** Invece di usare solo `np.dot()`, ho introdotto l'operatore nativo `@` (es. `A @ B`). È lo standard assoluto nel Machine Learning moderno per la moltiplicazione matriciale perché rende le formule identiche a quelle matematiche.
2.  **Il trucco del `-1` nel `reshape`:** Ho aggiunto come usare `-1` per far calcolare automaticamente una dimensione a NumPy. In Scikit-Learn (che vedremo nel Modulo 4) si usa continuamente `reshape(-1, 1)`.
3.  **Il VERO significato di `axis`:** Ho chiarito meglio come funziona `axis=0` e `axis=1`. Spesso si fa confusione dicendo "somma per righe". In realtà `axis=0` significa *collassa le righe* (muoviti in verticale), ottenendo la somma di ogni colonna.
4.  **Il mega-warning su Append/Insert:** Ho mantenuto la spiegazione di `np.append()`, ma l'ho circondata di un avviso critico. Modificare la dimensione di un array in un ciclo `for` è l'errore di performance numero 1 in NumPy.
5.  **Rimozione ridondanze:** Ho eliminato il paragrafo "Dimensioni e forma di un array" ( `ndim`, `size`, `shape`), perché l'abbiamo già spiegato approfonditamente nella lezione precedente (2.2.2).

Ecco il file **Definitivo (Ready to Push)**:

---

# 2.2.3 - Operazioni fondamentali sugli array

Dopo aver visto come creare e ispezionare gli array nella[lezione precedente](02_array.md), passiamo ora alle operazioni fondamentali. La potenza di NumPy risiede nella capacità di eseguire calcoli complessi su enormi moli di dati senza scrivere un singolo ciclo `for`.

## Operazioni algebriche (Element-wise)

Tutti i normali operatori matematici in Python (`+`, `-`, `*`, `/`, `**`) applicati agli array NumPy vengono eseguiti **elemento per elemento** (element-wise).

```py
>>> import numpy as np
>>> a = np.array([10, 20, 30])
>>> b = np.array([1, 2, 3])

>>> a + b
array([11, 22, 33])

>>> a - b
array([ 9, 18, 27])

>>> a / b
array([10., 10., 10.])
```

!!!warning "Moltiplicazione `*` vs Moltiplicazione Matriciale"
    Se avete un background matematico o venite da MATLAB, fate molta attenzione: in NumPy, `a * b` calcola il prodotto *elemento per elemento* (Prodotto di Hadamard), **NON** il prodotto riga per colonna delle matrici. Per quello esiste un operatore apposito che vedremo a breve.

### Il Broadcasting (Cenni)

Cosa succede se sommiamo un array con un singolo numero (scalare)?

```py
>>> a + 100
array([110, 120, 130])
```

NumPy propaga (effettua il *broadcasting*) automaticamente il numero `100` su tutti gli elementi dell'array, evitandoci di dover creare un array di soli `100` delle stesse dimensioni di `a`.

## Moltiplicazione Matriciale (L'operatore `@`)

Per effettuare il vero e proprio prodotto riga-per-colonna tra due matrici o vettori (fondamentale nelle Reti Neurali e nell'Algebra Lineare), NumPy offre due strade.

La via classica è usare la funzione `np.dot()` o il metodo `.dot()`:

```py
>>> A = np.array([[1, 2], [3, 4]])
>>> B = np.array([[5, 6], [7, 8]])

>>> A.dot(B)
array([[19, 22],
       [43, 50]])
```

Tuttavia, in Python moderno lo standard assoluto è utilizzare l'**operatore nativo `@`**, che rende il codice infinitamente più leggibile quando si concatenano più operazioni:

```py
>>> C = A @ B
>>> C
array([[19, 22],
       [43, 50]])
```

## Aggregazioni e l'enigma del parametro `axis`

NumPy offre metodi ultra-veloci per calcolare statistiche di base: `.sum()`, `.mean()`, `.max()`, `.min()`.

```py
>>> a = np.array([1, 2, 3, 4])
>>> a.sum()
10
```

Quando lavoriamo con matrici a più dimensioni, possiamo specificare il parametro `axis` per decidere lungo quale direzione effettuare l'operazione. Questo concetto spesso confonde i principianti:

*   `axis=0`: Muoviti lungo l'asse 0 (le righe) e **collassale**. Il risultato sarà un'operazione fatta *in verticale* (per ogni colonna).
*   `axis=1`: Muoviti lungo l'asse 1 (le colonne) e **collassale**. Il risultato sarà un'operazione fatta *in orizzontale* (per ogni riga).

```py
>>> matrice = np.array([[1, 2, 3],[4, 5, 6]])

# Collassa le righe (somma in verticale colonna per colonna)
>>> matrice.sum(axis=0)
array([5, 7, 9])

# Collassa le colonne (somma in orizzontale riga per riga)
>>> matrice.sum(axis=1)
array([ 6, 15])
```

## Modificare la forma: `reshape()`

Spesso abbiamo i dati giusti, ma nella "forma" sbagliata. Ad esempio, potremmo avere un vettore 1D di 16 pixel, ma sapere che rappresenta un'immagine 4x4. La funzione `reshape()` riorganizza i dati senza alterarli.

```py
>>> vettore = np.arange(1, 17) # Array da 1 a 16
>>> matrice = vettore.reshape((4, 4))
>>> matrice
array([[ 1,  2,  3,  4],[ 5,  6,  7,  8],
       [ 9, 10, 11, 12],[13, 14, 15, 16]])
```

!!!tip "Il trucco del `-1`"
    In Scikit-Learn capiterà spesso di non conoscere a priori una delle dimensioni. Se passiamo `-1` come parametro al `reshape`, NumPy calcolerà automaticamente quella dimensione in base al numero di elementi totali.
    ```py
    # "Voglio 2 righe, calcola tu quante colonne servono"
    >>> vettore.reshape(2, -1) 
    array([[ 1,  2,  3,  4,  5,  6,  7,  8],[ 9, 10, 11, 12, 13, 14, 15, 16]])
    ```

## Appiattire un array: `flatten()` e `ravel()`

L'operazione inversa al reshape è il "flattening", ovvero prendere una matrice N-dimensionale e schiacciarla in un vettore 1D. Ci sono due metodi:

```py
# Metodo 1: flatten() restituisce una COPIA (più sicuro, consuma più RAM)
>>> matrice.flatten()
array([ 1,  2,  3, ..., 16])

# Metodo 2: ravel() restituisce una VISTA (più veloce, ma se modifichi 
# l'output, modifichi anche la matrice originale!)
>>> matrice.ravel()
```

## Concatenazione di Array

Per unire due o più array, si usa `np.concatenate()`, specificando l'asse lungo il quale effettuare l'unione:

```py
>>> x = np.array([[1, 2]])
>>> y = np.array([[3, 4]])

# Concatenazione verticale (axis=0)
>>> np.concatenate((x, y), axis=0)
array([[1, 2],
       [3, 4]])

# Concatenazione orizzontale (axis=1)
>>> np.concatenate((x, y), axis=1)
array([[1, 2, 3, 4]])
```

!!!tip "Funzioni helper visive"
    Per comodità e leggibilità, NumPy offre anche `np.vstack((x, y))` (concatenazione Verticale) e `np.hstack((x, y))` (concatenazione Orizzontale) che fanno esattamente la stessa cosa ma sono più immediate da leggere.

## Inserimento, Rimozione e Aggiunta (Anti-Pattern)

NumPy offre le funzioni `np.insert()`, `np.delete()` e `np.append()` per aggiungere o rimuovere elementi da un array. 

Ad esempio:
```py
>>> arr = np.array([1, 2, 3])
>>> np.append(arr, [4, 5])
array([1, 2, 3, 4, 5])
```

!!!danger "Attenzione alle performance: Mai in un ciclo for!"
    A differenza delle liste Python, **gli array NumPy hanno dimensione fissa in memoria**. 
    Ogni volta che chiamate `np.append()` o `np.insert()`, NumPy **non** aggiunge l'elemento in coda. Invece, alloca un nuovo blocco di memoria RAM, vi copia dentro tutto l'array vecchio e poi aggiunge il nuovo elemento.
    Fare un `np.append()` dentro un ciclo `for` per milioni di iterazioni bloccherà completamente il vostro computer.
    **Best practice:** Se dovete creare un array dinamicamente passo dopo passo, usate le normali liste Python (`.append()`) e, solo alla fine del ciclo, convertite la lista in array con `np.array()`. In alternativa, create un array vuoto delle dimensioni finali corrette (`np.zeros()`) e riempitelo tramite indice.