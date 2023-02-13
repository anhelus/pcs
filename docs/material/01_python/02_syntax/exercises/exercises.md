# Esercizi 2 - Programmare in Python

## Esecizio 2.1

Scriviamo un ciclo che iteri fino a che il valore associato ad un contatore intero risulta essere minore di 10. Usiamo sia un ciclo `while`, sia un ciclo `for`.

#### Soluzione 2.1

Per prima cosa, è opportuno tracciare un breve diagramma di flusso che mostri l'andamento delle informazioni all'interno del nostro codice.

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

Scriviamo una funzione che iteri fino a che una condizione booleana non è `False`. Usiamo un ciclo `for`, ponendo come numero massimo di iterazioni 100 e se necessario, usando il metodo [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint).

#### Soluzione 2.2

La soluzione a questo esercizio prevede l'utilizzo "non convenzionale" di un ciclo `for`. Dovremo quindi utilizzare un valore booleano (esterno)

```py
def itera_for():
    cond=True
    for i in range(100):
            eval = random.randint(-10, 10)
            print('Valuto numero {}'.format(eval))
            if eval < 0:
                    print('Esco')
                    cond=False
                    return cond
            else:
                    print('Continuo')
    return cond
```

Il risultato ottenuto sarà:

```py
>>> itera_for()
Valuto numero 6
Continuo
Valuto numero 7
Continuo
Valuto numero 8
Continuo
Valuto numero -4
Esco
False
```

TODO: DA QUI

## Esercizio 2.3

Estraiamo tutti gli indici pari di una lista arbitraria di dieci elementi in ordine inverso. Per farlo, usiamo sia la funzione `range` sia lo slicing.

### Soluzione

```py
def estrai_con_slice(lista):
    if len(lista) != 10:
            print('Errore!')
            return []
    else:
            return lista[-2::-2]

def estrai_con_range(lista):
    if len(lista) != 10:
        print('Errore!')
        return []
    else:
        l_out = []
        for i in range(8, -1, -2):
            l_out.append(lista[i])
        return l_out
```

Il risultato ottenuto sarà:

```py
>>> l = [1,2,3,4,5,6,7,8,9,10]
>>> estrai_con_slice(l)
[10, 8, 6, 4, 2]
>>> estrai_con_range(l)
[10, 8, 6, 4, 2]
```

## E2.4

Utilizzare il pattern matching per stampare a schermo la parola "Vero" se il valore di una variabile è `True`, e "Falso" altrimenti.

### S2.4 - Soluzione

```py
def match_case(true_or_false):
    match true_or_false:
        case True:
            return "Vero"
        case False:
            return "Falso"
```

Il risultato ottenuto sarà:

```py
>>> a = True
>>> match_case(a)
'Vero'
>>> b = False
>>> match_case(b)
'Falso'
```

## E2.5

Creare un metodo che raddoppi una lista passata come argomento in ingresso. Provare ad utilizzare un ciclo `for` e ricordare la differenza tra shallow e deep copy.

### S2.5 - Soluzione

Potremmo essere tentati di scrivere una funzione come la seguente:

```py
def raddoppia_lista(lista):
    for elemento in lista:
        lista.append(elemento)
        print(f"Lista all'iterazione attuale: {lista}")
```

Proviamo a chiamare questa funzione; avremo subito un output ingestibile. Ciò è legato al fatto che Python è fermo in un loop infinito: il metodo agisce sulla lista originaria, che ad ogni iterazione del ciclo "ingloba" un altro elemento, provocando di conseguenza un aumento delle dimensioni della lista e, quindi, un'ulteriore iterazione, e così via all'infinito.

Possiamo però ottenere il risultato che ci serve usando il metodo `deepcopy`:

```py
from copy import deepcopy

def raddoppia_lista_deep(lista):
    lista_appoggio = deepcopy(lista)
    for elemento in lista_appoggio:
        lista.append(elemento)
        print(f"Lista di appoggio: {lista_appoggio}")
        print(f"Lista attuale: {lista}")
```

In questo caso, stiamo creando un'altra variabile, chiamata `lista_appoggio`, che sarà utilizzata come "buffer" per aggiungere alla lista originaria gli elementi relativi a sé stessa. Provando a chiamare questo codice otterremo il risultato desiderato:

```py
>>> raddoppia_lista_deep([1, 2])
Lista di appoggio: [1, 2]
Lista attuale: [1, 2, 1]
Lista di appoggio: [1, 2]
Lista attuale: [1, 2, 1, 2]
```
