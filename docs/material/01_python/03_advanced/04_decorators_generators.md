# 1.3.4 - Decoratori e Generatori

In questa lezione esploreremo due funzionalità avanzate di Python che distinguono un programmatore principiante da un esperto: i **Decoratori**, per estendere le funzionalità delle funzioni, e i **Generatori**, per gestire flussi di dati in modo efficiente.

## Decoratori

Un decoratore è un design pattern che permette di modificare o estendere il comportamento di una funzione (o metodo) senza modificarne il codice sorgente. In Python, i decoratori sono funzioni che accettano un'altra funzione come argomento e restituiscono una nuova funzione "arricchita".

Si applicano usando la sintassi `@nome_decoratore` sopra la definizione della funzione.

### Creare un Decoratore: Il Pattern Standard

Il caso d'uso più comune per un decoratore è eseguire del codice *prima* e *dopo* la funzione target (es. logging, timing, controllo accessi).

Per scrivere un decoratore, usiamo una struttura a "matrioska": una funzione esterna (il decoratore) che definisce una funzione interna (il wrapper).

```python
import functools
import time

def timer(func):
    """Stampa il tempo di esecuzione della funzione decorata."""
    
    # @functools.wraps preserva il nome e la docstring della funzione originale
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # 1. Eseguiamo la funzione originale
        value = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        run_time = end_time - start_time
        
        # 2. Aggiungiamo il comportamento extra (logging)
        print(f"La funzione {func.__name__!r} ha impiegato {run_time:.4f} secondi")
        
        # 3. Restituiamo il valore originale
        return value
        
    return wrapper
```

### Applicare il Decoratore

Ora possiamo applicare `@timer` a qualsiasi funzione per misurarne le performance senza toccare la logica interna:

```python
@timer
def waste_time(num_times: int):
    for _ in range(num_times):
        sum([i**2 for i in range(10_000)])

waste_time(100)
# Output: La funzione 'waste_time' ha impiegato 0.3201 secondi
```

!!!tip "Best Practice: `functools.wraps`"
    Notate l'uso di `@functools.wraps(func)` dentro il decoratore. Senza di esso, la funzione decorata perderebbe la sua identità (il nome `__name__` diventerebbe `wrapper` invece di `waste_time`), rendendo difficile il debugging.

### Decoratori built-in utili

Python offre decoratori potentissimi nella libreria standard. In Data Science, il più importante è `@lru_cache` (Least Recently Used Cache) dal modulo `functools`. Serve per la **memoization**: salva i risultati delle funzioni costose e li restituisce istantaneamente se gli stessi argomenti vengono ripassati.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# La prima esecuzione calcola, le successive leggono dalla cache
print(fibonacci(30)) 
```

## Generatori

I generatori sono funzioni speciali che permettono di creare iteratori in modo semplice. A differenza delle funzioni normali che restituiscono un valore e terminano (`return`), i generatori producono una sequenza di valori nel tempo, sospendendo l'esecuzione tra un valore e l'altro (`yield`).

### Lazy Evaluation (Valutazione Pigra)

Il vantaggio principale è l'efficienza della memoria. Una lista carica tutti i dati in RAM. Un generatore calcola il valore successivo solo quando richiesto (**Lazy Evaluation**).

Immaginiamo di dover processare una sequenza di un milione di numeri:

```python
# Approccio con LISTA (Eager): Occupa molta RAM
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Approccio con GENERATORE (Lazy): Memoria quasi zero
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2  # Mette in pausa la funzione e restituisce il valore
```

Utilizzo:

```python
# Creiamo il generatore (non calcola nulla ancora)
squares = get_squares_gen(5)

# Otteniamo i valori uno alla volta
print(next(squares)) # 0
print(next(squares)) # 1

# O iteriamo con un ciclo for
for num in get_squares_gen(5):
    print(num)
```

### Generator Expressions

Esattamente come le *List Comprehension*, Python offre le *Generator Expressions*. La sintassi è identica ma usa le parentesi tonde `()` invece delle quadre `[]`.

```python
import sys

# List Comprehension: Crea subito una lista di 10.000 elementi
lista = [i * 2 for i in range(10000)]

# Generator Expression: Crea un oggetto generatore (leggerissimo)
generatore = (i * 2 for i in range(10000))

print(f"Dimensione Lista: {sys.getsizeof(lista)} bytes")
# Output: ~85 KB
print(f"Dimensione Generatore: {sys.getsizeof(generatore)} bytes")
# Output: ~100-200 bytes (costante, indipendentemente da n!)
```

## Caso d'uso reale: Data Pipelines

In progetti di Machine Learning, spesso i dataset sono troppo grandi per stare nella RAM (es. file di log da 50GB o dataset di immagini). I generatori sono la soluzione standard per creare **Data Pipelines**.

Esempio di lettura file "pigra":

```python
def read_large_file(file_path: str):
    """Generatore che legge un file una riga alla volta."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

# Pipeline di processamento dati
log_lines = read_large_file("server_logs.txt")

# Possiamo processare file infiniti senza crashare la RAM
for line in log_lines:
    if "ERROR" in line:
        print(f"Trovato errore: {line}")
```

### Yield vs Return

| Caratteristica | `return` | `yield` |
| :--- | :--- | :--- |
| **Comportamento** | Termina la funzione e restituisce il risultato finale. | Sospende la funzione, restituisce un valore e salva lo stato. |
| **Memoria** | Deve costruire l'intero output in memoria. | Produce un elemento alla volta (memory efficient). |
| **Uso** | Funzioni standard, calcoli immediati. | Stream di dati, file grandi, sequenze infinite. |