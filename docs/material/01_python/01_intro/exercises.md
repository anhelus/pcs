# Esercitazione 1.1

## Esercizio 1.1

**Traccia**: *Creiamo una stringa che assuma valore **PCS** usando l'interprete integrato.*

**Soluzione**

Apriamo l'interprete Python digitando `python` da riga di comando. A quel punto, inseriamo la seguente istruzione, e premiamo `Invio`:

```py
>>> s = 'PCS'
PCS
```

## Esercizio 1.2

**Traccia**: *Valutiamo la lunghezza della stringa creata nell'esercizio precedente, e verifichiamo che sia uguale a 3.*

**Soluzione**

Innanzitutto, possiamo usare la funzione [`len()`](https://docs.python.org/3/library/functions.html#len) che, come abbiamo visto nella lezione, accetta una *sequenza* (ovvero un oggetto su cui si possa iterare), e restituisce un intero rappresentativo della lunghezza dell'iterabile.

Dato che la stringa è una sequenza, possiamo invocare la funzione `len()` passandogli come argomento `s`:

```py
>>> len(s)
3
```

Chiamando la funzione `len(s)` notiamo come il valore restituito sia quello atteso, ovvero `3`.

Possiamo anche provare ad assegnare il valore restituito ad una variabile `l`:

```py
>>> l = len(s)
```

A questo punto, possiamo verificare che `l` sia pari a `3` utilizzando l'operatore di uguaglianza:

```py
>>> l == 3
True
```

## Esercizio 1.3

**Traccia**: *Verifichiamo che il numero `x` sia compreso tra `0` e `10`.*

**Soluzione**

Per prima cosa, dichiariamo un valore qualsiasi per `x`:

```py
>>> x = 1
```

A questo punto, verifichiamo che `x` sia compreso tra `0` e `10` mediante l'operatore booleano `and`:

```py
>>> x < 10 and x > 0
True
```

## Esercizio 1.4

**Traccia**: Creare una lista a partire dalla stringa definita negli esercizi precedenti.

**Soluzione**

Una prima possibilità è quella di utilizzare il costruttore di classe [`list()`](https://docs.python.org/3/library/functions.html#func-list) che accetta una sequenza e restituisce una lista a partire da questa. Possiamo quindi scrivere:

```py
>>> l_1 = list(s)
```

Se proviamo a visualizzare `l_1`, avremo il seguente risultato:

```py
>>> l_1
['p', 'c', 's']
```

Un altro modo è quello di usare l'operatore `[]`, che però avrà risultati leggermente differenti, in quanto creerà una lista con all'interno un unico elemento, ovvero la stringa `s`. In pratica:

```py
>>> l_2 = [s]
>>> l_2
['pcs']
```
