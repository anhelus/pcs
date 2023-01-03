# 1.6: Le eccezioni in Python

Un programma Python termina appena trova un errore. Un errore in Python può essere di due tipi: un errore di sintassi, o un'eccezione. In questa lezione, parleremo delle seconde.

## 1.6.1 Eccezioni vs Errori di sintassi

Gli errori di sintassi avvengono quando il parser individua un'istruzione non corretta. Facciamo un breve esempio:

```py
>>> print(0/0))
  File "<stdin>", line 1
    print(0/0))
              ^
SyntaxError: unmatched ')'
```

In questo caso, le frecce indicano dove il parser ha trovato un errore sintattico. In particolare, vi era una parentesi di troppo. Se la rimuoviamo ed eseguiamo nuovamente il codcie:

```py
>>> print(0/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Stavolta abbiamo un altro tipo di errore, ovvero un'eccezione. Questo tipo di errore avviene quando del codice Python sintatticamente corretto ha un errore. L'ultima riga del messaggio indica che tipo di eccezione abbiamo riscontrato. In questo caso, era una ZeroDivisionError. Python offre diverse eccezioni integrate, così come la possibilità di creare eccezioni defintie da noi.

## Lanciare un'eccezione

Possiamo usare la parola chaive `raise` per lanciare un'eccezione nel caso avvenga un'eccezione., L'istruzione può avere anche un'eccezione custom associata.

Se vogliamo lanciare un errore quando occorre una certa condizione usando raise, possiamo fare come segue:

```py
>>> x = 10
>>> if x > 5:
...     raise Exception(f'x vale {x}. Non deve superare 5.')
```

Quando eseguiamo questo codice, avremo il seguente risutlato.

```py
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Exception: x vale 10. Non deve superare 5.
```

Il programma si ferma, e visualizza l'eccezione a schermo, offrendo dei suggerimenti chje indicano cosa sia andato storto.

## L'eccezione AssertionError

Invece di attender che un programma termini, possiamo anche iniziare usando una *assertion*. In altre parole, affermiamo che avvenga una certa condizione. SE questa condizione è vera, il programma può continuare. Altrimenti, il programma può lanciare un'eccezione di tipo AssertionError.

Facciamo un esempio. Verifichiamo, ad esempio, che il codice sia eseguito su un sistema Windows.

```py
>>> import sys
>>> assert ('win32' in sys.platform), 'Questo codice può essere eseguito solo su Windows'
```

Se eseguiamo questo codice su una macchina Windwos, non accadrà nulla, ed il programma continuerà la sua esecuzione. Se invece il codice viene eseguito su una macchina Unix, avremo un'eccezione del seguente tipo:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Questo codice può essere eseguito solo su Windows
```

Ovviamente, se viene incontrata un'eccezione di questo tipo, il programma si arresta. Tuttavia, cosa accadrebbe se volessimo che l'esecuzione continuasse?

## Gestione delle eccezioni

La gestione delle eccezioni in Python avviene mediante il blocco definito dalle istruzioni `try` ed `except`. Python esegue il codice contenuto in un'istruzione `try` come "ramo normale" del programma. Invece, il codice che segue l'istruzione `except` rappresenta la risposta del programma ad una qualsiasi eccezione trovata nella precedente clausola try.

Come abbiamo visto prima, quanod il coidce sintatticamente corretto trova un errore, Python lancerà un'eccezione. Questa farà terminare il programma se non correttamente gestita. Il blocco `except` determina come il programma risponda alle eccezioni.

La seguente funzione può aiutarci a comprendere il blocco `try/except`.

```py
def su_windows():
    assert ('win32' in sys.platform), 'Dobbiamo usare un sistema Windows'
    print('Siamo su Windows!')
```

La funzione `su_windows()` può essere eseguita soltanto su un sistema Windows. L'istruzione `assert` infatti farà in modo che venga lanciata un'eccezione `AssertionError` se chiamiamo la funzione `su_windows()` su un sistema che non è di questo tipo.

Proviamo a lanciare la funzione usando un `try/except`:

```py
try:
    su_windows()
except:
    pass
```

Usando questa sintassi, gestiremo l'errore mediante un'istruzione `pass`. Se eseguiamo questo codice su una macchina Linux, non avremo nulla in output. L'unico risultato che saremo riusciti ad ottenree sarà che il programma non sarà andato in crash: tuttavia, sarebbe utile avere un qualche tipo di avviso o gestione dell'eccezione. Per farlo, proviamo a cambiare il codice precedente come segue:

```py
try:
    su_windows()
except:
    print('Sembra che non siamo su Windows!')
```

Eseguiamo questo codice su una macchina Linux:

```sh
Sembra che non siamo su Windows!
```

Quando avviene un'eccezione in un programma che esegue questa funzione, il programma continuerà informandoci del fatto che la chiamata a funzione non ha avuto successo. Quello che non abbiamo visto è stato il tipo di errore lanciato come risultato della chiamata a funzione. Per vedere quello che è andato male, dobbiamo catturare l'errore lanciato dalla funzione.

Il seguente codice è un esempio dove catturiamo l'`AssertionError` e mandiamo a schermo questo messaggio:

```py
try:
    su_windows()
except AssertionError as error:
    print(error)
    print('La funzione su_windows() non è stata eseguita')
```

Se eseguiamo questa funzione su una macchina Linux, avremo il seguente output:

```sh
Dobbiamo usare un sistema Windows
La funzione su_windows() non è stata eseguita
```

Il primo messaggio è dato dall'`AssertionError`, che ci dice che la fuznione può essere eseguita soltanto su una macchina Windows. Il secondo messaggio ci indica quale funzione non è stata eseguita.

Nell'esempio precedente, abbiamo chiamato una funzione che abbiamo scritto noi stessi. Quando eseguiamo la funzione, catturiamo l'eccezione `AssertionError` e la stampiamo a schermo.

Ecco un altro esempio dove apriamo un file ed usiamo un'eccezione built-in:

```py
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Impossibile aprire il file')
```

Dato che file.log non esiste, il coidce precedente manderà in uscita il seguente:

```sh
Impossibile aprire il file
```

Questo è un messaggio abbastanza informativo, ed il nostro programma continuerà laa sua esecuzione. Nei [documenti Python](https://docs.python.org/3/library/exceptions.html), possiamo vedere come ci siano molte eccezioni built-in che è possibile utilizzare. Un'eccezione descritta su questa pagina è FileNotFoundError, che viene lanciata quanod il file o la cartella richiesti non esistono.

Per catturare questo tipo di eccezione e mandarla a schermo, possiamo usare il codice seguente:

```py
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as error:
    print(error)
```

In questo caso, se `file.log` non esiste, avremo il seguente output:

```sh
[Errno 2] No such file or directory: 'file.log'
```

Da notare che nell'istruzione `try` è possibile avere più di un'istruzione, e che l'`except` può gestire diverse eccezioni. Da notare inoltre come il codice nel `try` si fermerà non appena si trova un'eccezione.

La gestione delle eccezioni "nasconde" i diversi errori che possono comparire nel codice, compresi quelli inattesi. Per questo motivo, dovremmo evitare di scrivere degli except "generici", ma dovremmo focalizzarci su specifiche classi di eccezione da gestire.

Vediamo questo esempio, nel quale prima chiamiamo `su_windows()` e poi proviamo ad aprire un file:

```py
try:
    su_windows()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('La funzione su_windows() non è stata eseguita')
```

Se `file.log` non esiste, eseguire questo codice su una macchina Linux darà in uscita i seguenti messaggi:

```sh
Dobbiamo usare un sistema Windows
La funzione su_windows() non è stata eseguita
```

All'interno del `try`, abbiamo immediatamente riscontrato un'eccezione, non arrivando alla parte dove proviamo ad aprire `file.log`. Vediamoa desso cosa accade quando eseguiamo il codice su una macchina Windows.

```sh
Siamo su Windows!
[Errno 2] No such file or directory: 'file.log'
```

Di conseguenza:

* il `try` viene eseguito fino al punto dove si trova la prima eccezione;
* all'interno dell'`except`, determiniamo come il programma risponde all'eccezione.

In definitiva, è meglio *evitare l'utilizzo di `except` generici*.

## L'else

In Python l'uso dell'istruzione `else` ci permette di dire ad un programma di eseguire un certo blocco di codice soltanto ina ssenza di eccezioni.

Vediamo il seguente esempio:

```py
try:
    su_windows()
except AssertionError as error:
    print(error)
else:
    print('Eseguo la clausola else.')
```

Se eseguiamo questo codice su un sistgema Widnows, l'output sarà il seguente:

```sh
Siamo su Windows!
Eseguo la clausola else.
```

Dato che il programma non ha trovato alcuna eccezione, è stata eseguita la clausola else. Possiamo anche provare ad eseguire del codice all'interno della clausola else, catturando le possibili eccezioni:

```py
try:
    su_windows()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
```

Proviamo ad eseguire questo codice su macchina Windows. Il risultato sarà:

```sh
Siamo su Windows!
[Errno 2] No such file or directory: 'file.log'
```

Vediamo quindi come la funzione `su_windows()` sia stata correttamente eseguita. Dato che non è stata trovata alcuna eccezione, il programma ha provato ad aprire `file.log`. Tuttavia, questo file non esiste, ed invece di aprirlo, è stata catturata l'eccezione `FileNotFoundError`.

## Pulizia dopo l'uso di finally

Immaginiamo che dobbiamo sempre implementare un qualche tipo di azione per pulire il codice dopo l'esecuzione. Python ci permette di farlo mediante la clausola `finally`.

Facciamo un esempio:

```py
try:
    su_windows()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Istruzioni di pulizia. Eseguite indipendentemente dal resto del programma.')
```

Nel codice precedente, ciò che è presente nella clausola `finally` sarà sempre eseguito. Non importa che si sia trovata un'eccezione nelle clausole `try` o `else`. Se provassimo ad eseguire questo codice su una macchina Windows, avremmo il seguente output:

```sh
Siamo su Windows!
[Errno 2] No such file or directory: 'file.log'
Istruzioni di pulizia. Eseguite indipendentemente dal resto del programma.
```

## Conclusioni

Abbiamo visto la differenza tra gli errori sintattici e le eccezioni, ed abbiamo visto come lanciare e gestire le eccezioni in Python. In particolare:

* usando la clausola `raise`, potremo lanciare un'eccezione in qualsiasi momento;
* mediante la clausola `assert`, potremo verificare se una certa condizione èp rispettata, e lanciare un eccezione se non lo è;
* nella clausola `try`, tutte le istruzioni sono eseguite fino a che non si trova un'eccezione;
* la clausola `except` è usata per catturare e gestire una o più eccezioni trovate nella clausola `try`;
* la clausola `else`, in questo contesto, ci permette di eseguire blocchi di codice esclusivamente qunado non sono individuate delle eccezioni nel `try`;
* la clausola `finally` ci permette di eseguire sezioni di codice *indipendentemente* dal fatto che si siano trovate o meno eccezioni in precedenza.
