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

Così come in altri container Python, i contenuti di un array sono accessibili e modificabili mediante l'indicizzazione o lo slicing dell'array. A differenza del tipico container, però, diversi array possono condividere gli stessi dati, per cui i cambi fatti su un array possono essere visibili in un altro.

Gli attributi di un array riflettono informazioni intrinseche sull'array stesso. Se dobbiamo accedere o impostare delle proprietà di un array senza crearne uno nuovo, si può spesso accedere ad un array mediante is uoi attributi.

### Costruire un array

I nuovi array possono essere creati mediante un apposito costruttore.

ndarray(shape, **kwargs)

E' però più semplice farlo tramite una delle funzioni messe a disposizione da NumPy. Ad esempio, possiamo farlo usando la funzione np.array(), che ci permette di crearlo usando una semplice lista e, opzionalmente, impostando il tipo di dato:

```py
>>> a = np.array([1, 2, 3])
```

Esistono ovviamente numerose altre funzioni per la creazione di un array. Ad esempio, se volessimo creare una matrice con valori unitari, potremmo usare np.ones():

```py
>>> u = np.ones(2)
array([1., 1.])
```

mentre per una matrice con tutti valori pari a zero usiamo np.zeros():

```py
>>> u = np.zeros(2)
array([0., 0.])
```

#### Creazione di un array vuoto

Possiamo anche creare un array vuoto. Questo può essere particolarmente utile quando vogliamo preallocare un array di una certa dimensione.

```py
>>> np.empty(2)
array([42., 42.])
```

!!!note "Nota"
    In realtà, possiamo osservare un fenomeno interessante: infatti, l'array vuoto sarà, in realtà, popolato da valori. Tuttavia, questi valori sono completamente casuali, e dipendenti dallo stato della memoria del sistema in un determinato istante.

https://numpy.org/doc/stable/user/absolute_beginners.html