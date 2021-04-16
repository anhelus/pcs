# Introduzione agli array

## Qual è la differenza tra una lista Python ed un array NumPy?

NumPy ci dà un enorme range di modi veloci ed efficienti per creare degli array e manipolare dei dati numerici al lroo interno. Mentre una lista python può contenere diversi tipi di dati al suo interno, tutti gli elementi in un array NumPy devono essere omogenei. Le operazioni matematiche che devono essere effettuate sugli array sarebbero state infatti estremamente inefficaci se gli array non fossero stati omogenei.

### Perché* usare NumPy?

Gli array numpy sono più veloci e compatti rispetto alle liste Python. Un array consuma meno memoria, ed è più conveniente da utilizzare. NumPy uisa molta meno memoria per memorizzare i dati e fornisce un meccanismo per specificare i tipi d dati. Qusto permette una ulteriore ottimizzzazione del codice.

## Cosa è un array?

Un array è la struttura dati centrale della libreria NumPy. E' considerato come una griglia di valori, e contiene informazioni circa gli elementi grezzi (raw), su come localizzare ciascun elemento, e come interpretarlo. Ha inotlre una griglia di elementi che può essere indicizzata in diversi modi. Gli elementi son tutto dello stesso tipo, indicato con `dtype`.

Un array può essere idnicizzato da una tupla di interi non negativi, booleani, o da un altro array, o da interi. Il rank dell'array è il numeor di dimensioni. La forma dell'array è una tupla di interi che da la dimensione dell'arry su ogni dimensione.

Un modo in cui si possono inziializzare gli array NumPy è dalle liste Python, usanod liste annidate per dati con due o più dimensioni. Ad esempio:

```py
>>> a = np.array([1, 2, 3, 4, 5, 6])
```

o

```py
>>> a = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
```

Possiamo accedere agli elementi nell'array usando le parentesi quadre. Quando si accede agli elementi, dobbiamo ricordarci che l'indicizzazione in NumPy inizia a 0. QUesto significa che se vogliamo accedere il primo elemento nell'array, staremo accedendo all'elemento 0.

```py
>>> print(a[0])
[1 2 3 4]
```

### Più informaizoni sugli array

Possiamo occasionalmente sentire un riferimento ad un array come ad un *ndarray*, che è una abbreviazione per *N-dimensional array* (array ad n dimensioni). Un array ad n dimensioni è semplicemente un array con un numero generico di dimensioni. Possiaom sentire infatti 1-D, o array monodimensionaloi, o 2-D, array multidimenzionali, e via dicendo.

La classe NumPy ndarray viene suata per rappresentare sia matrici sia vettori. Un vettore è un array con una singola dimensione (non vi è differenza tra i vettori riga ed i vettori colonna), mentre una matrice si riferisce ad un array con due dimensioni. Per array tridimensionali o con un maggior numero di dimensioni, si usa comunemente il termine tensore.

#### QUali sono gli attributi di un array?

Una rray è normalmente un contenitore a dimensione fissata di oggetti dello stesso tipo e dimensione. Il numero di dimensioni ed oggetti in un array è definito dalla sua forma. La forma di un array è una tupla di interi non negativi che specifica le dimensioni lungo ogni asse.

In numpy, gli assi sono indicati con axes. Questo indica che se abbiamo un array bidimensionale del tipo:

[[0.,0.,0.],
 [1.,1., 1.]]

il nsotro array avrà due assi. Il primo asse ha una lunghezza di 2, mentre il secondo una lunghezza di 3.



https://numpy.org/doc/stable/user/absolute_beginners.html