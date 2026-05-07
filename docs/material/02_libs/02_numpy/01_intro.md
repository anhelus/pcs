---
description: Introduciamo la libreria NumPy, che ci permette di estendere le capacità di Python portando al suo interno il calcolo numerico e matriciale.
---

# 2.2.1 - Introduzione a NumPy

La libreria **NumPy**, nome derivante dalla crasi tra *Num*erical *Py*thon, è il pilastro fondamentale per il calcolo scientifico e l'analisi dati in Python.

Nella pratica, NumPy è uno standard *de facto*: le sue strutture dati sono utilizzate come base (o "motore" interno) da quasi tutte le altre librerie di Data Science e Machine Learning, tra cui Pandas, Scikit-Learn e TensorFlow.

## Installare NumPy

Come visto nel[Modulo 1.3](../01_python/03_advanced/00_environments.md), è fondamentale installare le librerie esterne all'interno del nostro ambiente virtuale isolato.

Apriamo il terminale, attiviamo l'ambiente virtuale e usiamo `pip`:

```sh
# Assicurati di avere l'ambiente virtuale attivo, es: source .venv/bin/activate
pip install numpy
```

La convenzione universale per importare NumPy nei nostri script è utilizzare l'alias `np`:

```py
import numpy as np
```

## La struttura dati: `ndarray`

Il cuore pulsante di NumPy è l'oggetto `ndarray` (*n-dimensional array*). Si tratta di una struttura dati ottimizzata per rappresentare vettori, matrici e tensori a $n$ dimensioni, contenenti dati di tipo **strettamente omogeneo** (tutti numeri interi, o tutti decimali, ecc.).

Il metodo più semplice per creare un array è usare il costruttore `np.array()` passandogli una normale lista Python:

```py
>>> a = np.array([1, 2, 3, 4, 5])
>>> type(a)
<class 'numpy.ndarray'>
```

### Array vs Liste: Perché usare NumPy?

A prima vista, un array 1D di NumPy può sembrare identico a una lista Python. Tuttavia, dal punto di vista ingegneristico, sono mondi completamente diversi. 

| Caratteristica | `ndarray` di NumPy | Lista nativa Python |
| -------------- | ---------------------- | --------------------------- |
| **Elementi** | Omogenei (tutti dello stesso tipo) | Eterogenei (es. `[1, "ciao", True]`) |
| **Memoria** | Blocco contiguo di memoria (Backend in C) | Array di puntatori sparsi in memoria |
| **Dimensione** | Fissa alla creazione | Dinamica (può crescere con `.append()`) |
| **Performance**| Estremamente veloce | Molto lenta su grandi moli di dati |

**Il segreto delle performance:**
Le liste Python sono flessibili ma pesanti. Poiché una lista può contenere tipi di dati misti, Python deve controllare il tipo di *ogni singolo elemento* prima di eseguire un'operazione.
In NumPy, essendo l'array omogeneo, i dati sono salvati nella RAM in blocchi fisicamente contigui. Le operazioni matematiche vengono eseguite direttamente al livello del processore da codice scritto in **C** o **C++** super ottimizzato, bypassando completamente le lentezze dell'interprete Python.

## Vettorizzazione (Vectorization)

Gli array NumPy sono progettati specificamente per l'algebra lineare. Facciamo un esempio pratico: vogliamo moltiplicare due vettori (array 1D) *elemento per elemento*.

Se usassimo le normali liste Python, dovremmo ricorrere a un ciclo `for`:

```py
# Approccio standard Python (Lento)
a = [1, 2, 3]
b = [4, 5, 6]
c =[]

for i in range(len(a)):
    c.append(a[i] * b[i])
```

Se estendessimo il calcolo a un'immagine a colori (che è un array 3D: altezza, larghezza, canali RGB), avremmo bisogno di ben tre cicli `for` annidati! In Python, i cicli annidati su milioni di elementi richiedono secondi, se non minuti.

In NumPy, possiamo sfruttare la **Vettorizzazione**. Possiamo applicare l'operazione matematica direttamente all'intero oggetto array:

```py
# Approccio NumPy (Vettorizzato e Veloce)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a * b  # Risultato: array([4, 10, 18])
```

Questa sintassi, oltre ad essere infinitamente più leggibile (sembra vera e propria matematica scritta su carta), è ordini di grandezza più veloce. Il ciclo `for` avviene ancora, ma avviene "sotto il cofano" nel backend in C di NumPy, non in Python.

Questa è la regola d'oro del calcolo scientifico in Python: **evitare i cicli `for` ogni volta che è possibile ed esprimerli come operazioni su array NumPy.**

## Tipi di dato (`dtype`)

A differenza del normale Python (che ha solo `int` e `float`), NumPy fornisce un controllo granulare sulla memoria, mettendoci a disposizione tipi di dato derivati direttamente dal linguaggio C.

Questo è cruciale nel Data Science: elaborare un milione di numeri a 64-bit richiede il doppio della RAM rispetto a elaborarli a 32-bit.

I tipi a dimensione fissa (*sized aliases*) più utilizzati sono:

*   `np.int8`, `np.int16`, `np.int32`, `np.int64`: Interi con segno a 8, 16, 32 o 64 bit.
*   `np.float32`, `np.float64`: Numeri a virgola mobile (decimali). In ambito Machine/Deep Learning, il `float32` è lo standard assoluto per risparmiare memoria sulle GPU.

Possiamo specificare il tipo di dato esplicitamente al momento della creazione dell'array usando il parametro `dtype`:

```py
# Forziamo la creazione di un array di float a 32 bit
>>> arr = np.array([1, 2, 3], dtype=np.float32)
>>> arr.dtype
dtype('float32')
```

!!!tip "Type Hinting in NumPy"
    Nelle lezioni precedenti abbiamo visto quanto sia importante il *Type Hinting*. Ma come annotiamo un array NumPy?
    Nelle versioni moderne della libreria esiste un sottomodulo dedicato:
    ```py
    import numpy as np
    import numpy.typing as npt

    def normalizza(dati: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        # Logica della funzione
        pass
    ```