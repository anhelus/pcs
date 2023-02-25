# 1.6 - La gestione degli errori

Nella maggior parte dei linguaggi interpretati, l'esecuzione di un programma termina non appena viene individuato un errore.

In Python, esistono due tipi di errore: il primo è quello *sintattico*, mentre il secondo è chiamato *eccezione*.

## 1.6.1 - Errori sintattici ed eccezioni

Gli errori di sintassi avvengono qunado il parser individua un'istruzione scritta in maniera non corretta. Ad esempio:

```py
>>> print(0/0))
  File "<stdin>", line 1
    print(0/0))
              ^
SyntaxError: unmatched ')'
```

In questo caso, notiamo la presenza di una parentesi di chiusura di troppo. Di conseguenza, Python lancia un `SyntaxError`, indicandoci anche dove è occorso l'errore (in questo caso, mediante l'informazione `unmatched ')'`).

Proviamo adesso a rimuovere la parentesi.

```py
>>> print(0/0)
```

Se proviamo ad eseguire questa istruzione, avremo l'altro tipo di errore, ovvero l'eccezione. In questo caso, infatti, il codice risulta essere (sintatticamente) corretto, ma è comunque occorso un evento ritenuto "impossibile", che viene adeguatamente descritto nel `Traceback`:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

In particolare, notiamo come il traceback ci dia diverse informazioni:

* il *file* dove è stata generata l'eccezione. In questo caso, viene riportato `<stdin>` perché il codice precedente è stato inserito mediante interprete;
* la *riga* dove è occorsa l'eccezione. In questo caso, notiamo che è riportato `line 1`;
* il *tipo* di eccezione occorsa, con una breve descrizione dell'errore. In questo caso, notiamo come venga lanciata una [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError), che occorre quando il secondo argomento della divisione è pari a 0.

!!!note "Eccezioni built-in"
    Notiamo come l'eccezione `ZeroDivisionError` sia una *built-in exception*, ovvero un'eccezione già integrata nel linguaggio Python, che comunque ci offre la possibilità di definire da noi nuovi tipi di eccezione. Per una panoramica completa, consultare la [reference](https://docs.python.org/3/library/exceptions.html#built-in-exceptions).

## 1.6.2 - Lanciare un'eccezione

Possiamo lanciare una specifica eccezione all'occorrenza di una condizione non voluta all'interno del nosro codice utilizzando l'istruzione `raise`. Ad esempio, possiamo verificare che il valore di una variabile non sia superiore ad un dato numero:

```py
x = 10
if x > 5:
    raise Exception(f'x vale {x}. Non deve superare 5.')
```

Provando ad eseguire il codice precedente, avremo il seguente risultato:

```py
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Exception: x vale 10. Non deve superare 5.
```

Dal traceback, notiamo come sia stata lanciata un'eccezione generica con il messaggio da noi elaborato.

## 1.6.3 - L'istruzione assert

Un altro modo di gestire situaizoni impreviste è quello di utilizzare l'istruzione `assert`, che verifica la condizione passata come parametro. Se tale condizione risulta essere vera, il programma continuerà la sua esecuzione; in alternativa, sarà lanciata un'eccezione di tipo `AssertionError`.

Possiamo, ad esempio, verificare che il nostro codice sia eseguito su un sistema Windows.

```py
import sys
assert ('win32' in sys.platform), 'Questo codice può essere eseguito solo su una macchina Windows!'
```

Eseguendo questa istruzione su una macchina Windows, non sarà lanciata alcuna eccezione, ed il programma continuerà tranquillamente l'esecuzione. Eseguendo invece lo stesso codice su una macchina Unix, sarà lanciata un'`AssertionError`, ed il programma terminerà:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Questo codice può essere eseguito solo su una macchina Windows!
```

## 1.6.4 - Gestione delle eccezioni: il blocco try/except

Abbiamo visto come le istruzioni `raise` ed `assert` permettano di verificare rispettivamente l'occorrenza di un errore o di una determinata condizione. Tuttavia, è possibile *gestire* le situazioni in cui avviene un errore; per farlo, è necessario utilizzare il blocco `try/except`.

Nella pratica, durante l'esecuzione normale del programma, Python eseguirà regolarmente le istruzioni contenute nella clausola `try`. Tuttavia, se viene riscontrata un'eccezione, il controllo passerà direttamente alla clausola `except`, cui è delegato il compito di gestirla. Questo funzionamento è schematizzato nella figura successiva.

```mermaid
---
title: Flusso in un blocco try/except
---
stateDiagram-v2
    state if_state <<choice>>
    state join_state <<join>>
    "Programma" --> "Blocco try/except"
    "Clausola try" --> if_state
    if_state --> "Clausola except": Eccezione
    "Clausola except" --> join_state
    if_state --> join_state
    join_state --> "Programma"
```

Notiamo come l'esecuzione del programma debba (idealmente) continuare, che la clausola `except` venga eseguita o meno. Proviamo a definire la funzione `controlla_sistema_operativo()`, che controlla se siamo su Windows:

```py
def controlla_sistema_operativo():
    assert ('win32' in sys.platform), 'Questo codice può essere eseguito solo su una macchina Windows!'
    print('Il sistema operativo è Windows!')
```

Nella funzione `controlla_sistema_operativo()`, l'istruzione `assert` controlla che si sia su una macchina Windows; in caso contrario, sarà lanciata un'eccezione di tipo `AssertionError`. Proviamo ad integrare la funzione all'interno di un blocco `try/except`:

```py
try:
    controlla_sistema_operativo()
except:
    pass
```

In questo caso, la gestione dell'errore sarà delegata ad un'istruzione `pass` che, come sappiamo, non fa nulla. Eseguendo questo codice su una macchina Windows, sarà mandato a schermo il messaggio `Il sistema operativo è Windows!`, indice del fatto che l'`assert` non ha lanciato un'eccezione di tipo `AssertionError`. Se invece dovessimo eseguire questa funzione su una macchina Linux, non avremmo alcun risultato: infatti, la clausola `try` catturerebbe l'`AssertionError` e ne delegherebbe la gestione alla clausola `except`, che si limita ad eseguire un'istruzione `pass`.

Proviamo a modificare il codice precedente come segue:

```py
try:
    controlla_sistema_operativo()
except:
    print('Sembra che non siamo su Windows!')
```

Eseguendo questo codice su macchina Linux, avremo il seguente messaggio:

```sh
Sembra che non siamo su Windows!
```

### 1.6.4.1 - Gestione di eccezioni specifiche

Come è possibile verificare dal codice precedente, qualora venga lanciata un'eccezione, non sarà più disponibile il Traceback visto in precedenza, bensì il messaggio `Sembra che non siamo su Windows!`. Ciò comporta un problema: infatti, non avremo informazioni a riguardo di *quale eccezione* sia stata lanciata. Per recuperare queste informazioni, dovremo fare una modifica all'istruzione `except`:

```py
try:
    controlla_sistema_operativo()
except AssertionError as error:
    print(error)
    print('Sembra che non siamo su Windows!')
```

Eseguendo questa funzione su macchina Linux, l'output sarà stavolta il seguente:

```sh
Questo codice può essere eseguito solo su una macchina Windows!
Sembra che non siamo su Windows!
```

Il primo messaggio, quindi, è lanciato a valle della mancata verifica della condizione nella clausola `assert` specificata in `controlla_sistema_operativo()`, mentre il secondo è direttamente specificato nella clausola `except`.

Vediamo un altro esempio, nel quale proviamo ad aprire un file, gestendo l'eccezione lanciata quando questo non esiste:

```py
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Impossibile aprire il file specificato.')
```

Eseguendo questo codice, una volta appurato che `file.log` non esiste, avremo il seguente messaggio:

```sh
Impossibile aprire il file specificato.
```

Nonostante il messaggio sia abbastanza informativo, stiamo comunque gestendo *tutte* le possibili eccezioni all'interno della clausola `except`. Cerchiamo quindi di trovarne una più adatta al nostro scopo tra quelle specificate nella [reference Python](https://docs.python.org/3/library/exceptions.html). In particolare, scegliamo l'eccezione [FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError), e modifichiamo il codice come segue:

```py
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as error:
    print(error)
```

In questo caso, se `file.log` non esiste, in output sarà mandato il messaggio associato all'eccezione `FileNotFoundError`, ovvero:

```sh
[Errno 2] No such file or directory: 'file.log'
```

### 1.6.4.2 - Eccezioni multiple

A questo punto è importante sottolineare come il blocco `try/except` sia in grado di gestire situazioni anche abbastanza complesse. Infatti, laddove è evidente come la clausola `try` sia in grado di contenere diverse istruzioni, anche la clausola `except` può gestire diverse tipologie di eccezione.

In tal senso, proviamo a modificare il nostro codice, controllando dapprima il sistema operativo, e poi provando a leggere un file:

```py
try:
    controlla_sistema_operativo()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print('Il file specificato non esiste.')
except AssertionError as error:
    print(error)
    print('Sembra che non siamo su Windows!')
```

Vediamo cosa succede in due diversi casi. Per prima cosa, eseguiamo il codice su macchina Linux, con `file.log` non esistente. In questo caso, il codice darà in output i seguenti messaggi:

```sh
Questo codice può essere eseguito solo su una macchina Windows!
Sembra che non siamo su Windows!
```

In pratica, la prima istruzione del `try`, delegata al controllo del sistema operativo, riscontra un'eccezione, per cui viene chiamata la seconda clausola `except`. Nel caso invece si esegua il codice su macchina Windows, e supponendo sempre l'assenza di `file.log`, il risultato sarà il seguente:

```sh
Siamo su Windows!
Il file specificato non esiste.
```

In questo caso, la clausola `try` non ha riscontrato problemi nell'esecuzione della prima istruzione. Tuttavia, l'eccezione è stata lanciata in corrispondenza della fase di lettura del file, lanciando un'eccezione gestita dalla prima clausola `except`.

## 1.6.5 - La clausola else

La clausola `else` può essere usata in abbinamento al blocco `try/except` per eseguire un certo blocco di codice *soltanto in assenza di eccezioni*. Ad esempio:

```py
try:
    controlla_sistema_operativo()
except AssertionError as error:
    print(error)
else:
    print('Il sistema operativo è Windows!')
```

Eseguendo questo codice su Windows, il programma non riscontrerà alcuna eccezione, e l'output sarà quello esplicitato nella clausola `else`:

```sh
Siamo su Windows!
Il sistema operativo è Windows!
```

Potremmo usare una clausola `else` per gestire ulteriori eccezioni. Ad esempio, proviamo ad eseguire questo blocco di codice su una macchina Windows (e senza il file `file.log`):

```py
try:
    controlla_sistema_operativo()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError:
        print('Il file specificato non esiste.')
```

Il risultato sarà:

```sh
Siamo su Windows!
Il file specificato non esiste.
```

!!!tip "Suggerimento"
    Ricordiamo sempre che la clausola `else` viene eseguita *soltanto se non sono state trovate eccezioni*. Se è stata trovata un'eccezione, e gestita nell'`except`, il flusso del programma continuerà comunque la sua regolare esecuzione, ma l'`else` non sarà invocato.

## 1.6.6 - La clausola finally

La clausola `finally` ci permette di eseguire delle istruzioni indipendentemente dal fatto che siano state riscontrate o meno eccezioni in un blocco `try/except` antecedente. Andiamo a modificare leggermente il codice relativo all'ultimo esempio:

```py
try:
    su_windows()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError:
        print('Il file specificato non esiste.')
finally:
    print('Istruzioni eseguite indipendentemente dal resto del programma.')
```

In questo caso, ciò che viene inserito nella clausola `finally` sarà sempre eseguito, indipendentemente da ciò che è accaduto nel codice precedente. Provando ad eseguire questo codice su macchina Windows in assenza di `file.log`, avremo il seguente output:

```sh
Siamo su Windows!
Il file specificato non esiste.
Istruzioni eseguite indipendentemente dal resto del programma.
```

!!!tip "L'utilità della clausola `finally`"
    La clausola `finally` trova utilità in tutte quelle situazioni nelle quali è necessario effettuare delle operazioni a valle della gestione dell'eccezione. Queste operazioni sono spesso definite "di pulizia", perché prevedono l'eliminazione di stati o variabili che possono occupare memoria e che non sono più utili ai fini dell'esecuzione del programma.

## 1.6.6 - Per ricapitolare...

In questa lezione, abbiamo:

* visto la differenza tra *errore sintattico* ed *eccezione*;
* utilizzato l'istruzione `raise` per lanciare un'eccezione in qualsiasi momento;
* utilizzato l'istruzione `assert` per verificare il rispetto di una determinata condizione, lanciando in caso contrario un `AssertionError`;
* utilizzato la clausola `try` per verificare l'occorrenza di eccezioni all'interno di un blocco di istruzioni;
* utilizzato la clausola `except` per catturare e gestire una o più delle eccezioni trovate nella clausola `try` corrispondente;
* utilizzato la clausola `else` per eseguire blocchi di codice *esclusivamente* nel caso non siano state individuate eccezioni nel `try` precedente;
* utilizzato la clausola `finally` per eseguire blocchi di codice *indipendentemente* dal fatto che siano state individuate o meno eccezioni.

Nella [prossima lezione](../07_func_prog/lecture.md) andremo ad introdurre i principi alla base della programmazione funzionale.
