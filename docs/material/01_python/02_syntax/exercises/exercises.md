# Esercizi 2 - Programmare in Python

## Esecizio 2.1

Scriviamo un ciclo che iteri fino a che il valore associato ad un contatore intero risulta essere minore di 10. Usiamo sia un ciclo `while`, sia un ciclo `for`.

**Soluzione**: Per prima cosa, è opportuno tracciare un breve diagramma di flusso che mostri l'andamento delle informazioni all'interno del nostro codice.

```mermaid
flowchart TD
A(START) --> B[i = 1]
B --> C{i <= 10}
C --> |No| E[/print(i)/]
C --> |Sì| D[i = i + 1]
E --> F(END)
```

Implementiamo il codice in primis utilizzando un ciclo `while`. Per farlo, inizializziamo a zero un contatore `i` e come condizione verifichiamo che `i` sia minore di `10`:

```py
>>> i = 1
>>> while i <= 10:
...     print(f'Il valore di i è {i}')
...     i = i + 1
```

Se proviamo ad eseguire questo codice, otterremo il seguente risultato:

```py
Il valore di i è 1
Il valore di i è 2
Il valore di i è 3
Il valore di i è 4
Il valore di i è 5
Il valore di i è 6
Il valore di i è 7
Il valore di i è 8
Il valore di i è 9
Il valore di i è 10
```

Proviamo adesso ad usare un `for`. In questo caso, potremo limitarci ad usare in maniera opportuna la funzione `range()`:

```py
>>> for i in range(1, 11):
...     print(f'Il valore di i è {i}')
```

Eseguendo questa istruzione, otterremo un risultato analogo al precedente.

## Esercizio 2.2

Data una lista di numeri, scrivere una funzione che iteri fino a che non si trova un numero divisibile per $7$. Utilizzare un ciclo `for`.

**Soluzione**: La soluzione a questo esercizio prevede l'utilizzo dell'istruzione `break`, che dovrà essere lanciata quando troveremo un multiplo intero di $7$.

```py linenums="1"
def multiplo_sette(lista):
    for el in lista:
        if el % 7 == 0:
            print(f'{el} è multiplo di 7. Uscita in corso.')
            break
        else:
            print(f'{el} non è multiplo di 7.')
```

In pratica:

* alla riga 2 iteriamo su ogni elemento della lista;
* alla riga 3, se l'elemento è perfettamente divisibile per $7$ (e, quindi, il modulo della divisione è $0$), stampiamo a schermo un messaggio ed usciamo dalla funzione;
* se la precedente non è verficata, continuiamo l'iterazione sulla lista.

Ad esempio:

```py
>>> l = [1, 2, 5, 13, 21, 5]
>>> multiplo_sette(l)
1 non è multiplo di 7.
2 non è multiplo di 7.
5 non è multiplo di 7.
13 non è multiplo di 7.
21 è multiplo di 7. Uscita in corso.
```

## Esercizio 2.3

Estraiamo tutti gli indici pari di una lista arbitraria di dieci elementi in ordine inverso. Per farlo, usiamo sia la funzione `range` sia lo slicing.

**Soluzione**: Una possibile implementazione delle funzioni è la seguente:

```py linenums="1"
def estrai_con_slice(l):
    return l[-1::-2]

def estrai_con_range(l):
    l_out = []
    for i in range(len(l) - 1, -2, -2):
        l_out.append(l[i])
    return l_out
```

Partiamo dalla funzione `estrai_con_slice(l)`. Qui sfruttiamo il meccanismo di slicing su lista, che ricordiamo essere dato dall'espressione:

```py
l[i:f:s]
```

dove `l` è la lista sotto analisi, `i` è l'indice iniziale, `f` è l'indice di terminazione, ed `s` è lo step da utilizzare. In questo caso, stiamo specificando `i` pari a `-1`, per cui lo slicing partirà dall'ultimo elemento della lista, ed andrà verso l'indice finale (che omettiamo). Tuttavia, se omettessimo anche `s`, lo slicing ci restituirebbe esclusivamente l'ultimo elemento della lista; di conseguenza, specifichiamo un passo negativo, che ci assicurerà che `l` venga completamente attraversata considerando soltanto gli elementi pari. Un altro modo sarebbe stato il seguente:

```py
>>> l_out = l[1::2]
>>> l_out.reverse()
>>> l_out
[10, 8, 6, 4, 2]
```

In questo caso, aabbiamo potuto utilizzare uno slicing "classico", da sinistra verso destra, ma abbiamo dovuto utilizzare il metodo `reverse()` per invertire l'ordine della lista.

Applichiamo la funzione alla lista `l`:

```py
>>> l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> estrai_con_slice(l)
[10, 8, 6, 4, 2]
```

Nella funzione `estrai_con_range()`, invece, definiamo un ciclo `for` su una sequenza generata dalla funzione `range(i, f, s)`, specificando `i = len(l) - 1`, ovvero `9`, ed `f = 0`. Ciò è legato al fatto che `l[9]` è, a causa dello 0-indexing di Python, l'ultimo elemento della lista. Come step manteniamo, come prevedibile, `-2`.

```py
>>> estrai_con_range(l)
[10, 8, 6, 4, 2]
```

!!!tip "Suggerimento"
    Nel caso della funzione `estrai_con_range()`, anche `f = -1` è valido. Tuttavia, se impostassimo `f = -2`, il risultato sarebbe `[10, 8, 6, 4, 2, 10]`. Il motivo è legato al fatto che, all'ultima iterazione, staremmo considerando `l[-1]`, che è proprio `10`.

## Esercizio 2.4

Duplicare una lista passata come argomento in ingresso. Provare ad utilizzare un ciclo `for`.

**Soluzione**: Potremmo essere tentati di scrivere una funzione come la seguente:

```py
def raddoppia_lista(lista):
    for elemento in lista:
        lista.append(elemento)
        print(f"Lista all'iterazione attuale: {lista}")
```

Se provassimo ad utilizzare questa funzione, faremmo finire l'interprete in un ciclo infinito. Infatti, la funzione tenta di agire sulla lista originaria che, ad ogni iterazione, aumenta le sue dimensioni di un elemento, il che, ovviamente, rende impossibile raggiungere il termine della stessa!

Per ottenere il risultato previsto, dobbiamo usare una *deep copy*, ovvero fare una copia *esatta* della lista. Per chi ha familiarità con il C, si tratta, in poche parole, di una copia per valore. Usiamo il metodo `deepcopy`:

```py
from copy import deepcopy

def raddoppia_lista_deep(lista):
    lista_appoggio = deepcopy(lista)
    for elemento in lista_appoggio:
        lista.append(elemento)
        print(f"Lista di appoggio: {lista_appoggio}")
        print(f"Lista attuale: {lista}")
```

Stiamo creando una nuova lista, chiamata `lista_appoggio`, che sarà utilizzata come base per duplicare la lista originaria. Provando a chiamare questa funzione, otterremo il risultato desiderato:

```py
>>> raddoppia_lista_deep([1, 2])
Lista di appoggio: [1, 2]
Lista attuale: [1, 2, 1]
Lista di appoggio: [1, 2]
Lista attuale: [1, 2, 1, 2]
```

## Esercizio 2.5

Generare una lista di elementi casuali compresi tra $0$ e $10$. Usare sia una funzione con un unico parametro opzionale.

**Soluzione**: Scriviamo la seguente funzione:

```py
import random

def genera_lista_casuale(lunghezza=5):
    l = []
    for i in range(lunghezza):
        l.append(random.randint(0, 10))
    return l
```

In particolare, `genera_lista_casuale()` accetta come parametro opzionale `lunghezza`, il cui valore è 5, ed usa la funzione `append()` per aggiungere un valore generato casualmente.

Volendo, è possibile usare anche una list comprehension:

```py
def genera_lista_casuale_con_l_c(lunghezza=5):
    return [random.randint(0, 10) for i in range(lunghezza)]
```

Verifichiamo entrambe le funzioni:

```py
>>> genera_lista_casuale()
[0, 2, 1, 0, 2]
>>> genera_lista_casuale(lunghezza=10) 
[2, 2, 2, 9, 5, 1, 5, 10, 9, 6]
>>> genera_lista_casuale_con_l_c()
[10, 7, 2, 5, 1]
>>> genera_lista_casuale_con_l_c(lunghezza=10) 
[0, 9, 3, 7, 1, 3, 9, 3, 8, 7]
```
