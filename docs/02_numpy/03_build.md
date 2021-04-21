

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