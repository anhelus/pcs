# 1.7: La programmazione funzionale

La *programmazione funzionale* è un paradigma di programmazione che definisce l'elaborazione del dato attraverso e concetti di *funzione* e *stato immutabile*.

Per comprendere cosa questo comporti, è utile pensare alla programmazione imperativa. In questo paradigma, infatti, l'elaborazione avviene mediante le singole istruzioni scritte nel codice sorgente, le quali consistono di una serie di comandi la cui esecuzione modifica il valore di una variabile e, conseguentemente, lo *stato* del programma. Ad esempio, un ciclo esegue ripetutamente una certa istruzione, cambiando di volta in volta il valore di una variabile:

```py
contatore = 0
for i in range(10):
    contatore += 1
```

Man mano che il valore di `contatore` aumenta, lo stato delle variabili varia di conseguenza. Di contro, la programmazione funzionale elimina il concetto di stato. Invece di modificare i valori delle variabili, questo tipo di programmazione lavora soltanto su tipi *immutabili* che, come sappiamo, non possono essere alterati. Di conseguenza, la programmazione funzionale lavora esclusivamente su *copie* della strutture dati originarie. Inoltre, mentre nella programmazione imperativa usiamo normalmente costrutti come sequenze, cicli ed iterazioni, nella programmazione funzionale usiamo esclusivamente funzioni per modificare i dati, il che risulta in soluzioni più eleganti, maggiormente modulari, e potenzialmente più efficienti.

Prima di iniziare a parlare di programmazione funzionale in Python, tuttavia, è necessario introdurre alcuni concetti fondamentali.

## 1.7.1 - Le funzioni di ordine superiore

Le *funzioni di ordine superiore* sono ampiamente utilizzate nella programmazione funzionale, e non sono altro che funzioni che possono a loro volta accettare una funzione come argomento, o restituire una funzione in uscita. 

Le funzioni di ordine superiore sono lo strumento principale per definire l'elaborazione nella programmazione funzionale. Queste sono funzioni che possono accettare una funzione come argomento, o restituire una funzione in uscita. In Python, `reduce()`, `map()` e `filter()` sono alcune tra le più importanti funzioni di ordine superiore. Quando combinate con funzioni più semplici, possono essere usate epr eseguire operazioni complesse.

Vediamo un esempio di funzione di ordine superiore. In particoalre, `stampa_saluto()` accetta una funzione `f` ed una stringa `n` come argomenti, e restituisce la chiamata alla funzione `f` con argomento `n`, ovvero `f(n)`.

```py
>>> def saluto(nome):
...     return f'Buongiorno, {}!'
...
>>> def stampa_saluto(f, n):
...     print(f(n))
...
>>> stampa_saluto(saluto, 'Mondo')
Buongiorno, Mondo!
```

## Funzioni anonime

Abbiamo visto un esempio di una funzione che accetta come argomento un'altra funzione. `map()`, `filter()` e `reduce()` funzionano allo stesso modo: ognuno di loro accetta una funzione ed una sequenza di elementi, restituendo il risutato dell'applicazione della funzi0one ricevuta ad ogni elemento della sequenza. Nei due esempi precedenti, abbiamo definito le nostre funzioni suando la parola chiave `def` di Python. Questo crea un oggetto Python chiamabile che esegue l'istruzione specificata all'interno della sua definizione ogni volta che lo chiamiamo.

Tuttavia, nella programmazione funzionale, le funzioni anonime (anche chiamate *funzioni lambda*) sono preferite. Ne parleremo estesamente nella prossima lezione. Tuttavia, per ora ci basti sapere che sono chiamate anonime perché non sono "collegate" ad alcun nome, allineandosi quindi alla tendenza della programmaizone funzionale verso l'assenza di stato. In pratica, la differenza principale tra le funzioni lambda e le funzioni Python normali sta nel fatto che la funzione lambda valuta una singola espressione restituendo una funzione, mentre le funzioni normali non lo fanno (necessariamente). In altri termini, le funzioni lambda non possono usare delle istruzioni come le condizionali, o anche un semplice `return`. Ecco un esempio di funzione lambda:

```py
>>> (lambda x: x + 1)(5)
6
```

Potremmo definire questa operazione usando la parola chiave `def` ed otterremmo lo stesso output:

```py
>>> def aggiungi_uno(x):
...     return x + 1
...
>>> aggiungi_uno(5)
6
```

In pratica, nel primo snippet, abbiamo usato la keyword `lambda`per definire una funzione inline, chiamandola con argomento `x = 5`. La funzione è stata immediatamente valutata, ed un output prodotto. A differenza del secondo snippet, la funzione lambda non era legata ad un nome, per cui, per utilizzarla nuovamente, dovremmo riscrivere l'istruzione.

Le funzioni lambda sono importanti per `map()`, `filter()` e `reduce()` perché gli argomenti che passiamo a queste funzioni sono spesso funzioni brevi che devono essere usate soltanto una volta nei nostri programmi, per cui non vi è alcun motivo per salvarle. A differenza delle funzioni regolari che devono essere definite e salvate in memoria, le funzioni anonime sono più concise, e vengono eliminate dopo l'esecuzione.

Ora che abbiamo visto i preliminari, diamo uno sguardo più approfondito alle funzioni `map()`, `filter()` e `reduce()`.

## map()

La funzione `map()` di Python ha la seguente sintassi:

```py
map(function, *sequence)
```

In pratica, `map()` applica la funzione ricevuta al primo argomento ad ogni elemento nella sequenza `sequence`, restituendo la sequenza risultatnte. Nell'esempio successivo, creiamo una lista di interi ed usiamo `map()` e la funzione `str` di Python per convertire ogni intero in stringhe.

```py
>>> seq = list(range(10))
>>> list(map(str, seq))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

Notiamo come i risultati restituiti dalla funzione `map()` siano a loro volta racchiusi in una lista. Questo è legato al fatto che, in realtà, la funzione `map()` restituisce un generator.

```py
>>> map(str, seq)
<map object at 0x000001BB7143F100>
```

I generatori Python adottano una astrategia conosciutra come *lazy evaluation*, il che implica che Python non conosce il valore di un oggetto fino a che non lo usa. Anche se può sembrare controintuitivo, valuter un oggetto in maniera "lazy" permette di aumentare l'efficienza del codice riducendo il numero di elabroazioni non necessarie. Questo è il motivo per cui abbiamo racchiuso il generator creato da `map()` in una lista: farlo valuta l'espressione del generatore, e permette di inserire i risultati in un oggetto di tipo lista facilmente accessibile.

!!!note "Nota"
    Le list comprehension hanno lo stesso scopo della funzione `map()`. Tuttavia, in questo caso, non abbiamo lazy evaluation.

## filter()

La funzione `filter()` di Python ha la seguente sintassi:

```py
filter(function, *sequence)
```

In questo caso, filter() prende una funzione chiamata *predicato* che restituisce `True` se un elemento soddisfa la condizione definita nel predicato, e `Falso`altrimenti. L'output della funzione `filter()`consiste degli elementi della sequenza originaria che soddisfano il predicato.

Nel codice seguente, usiamo una funzione `filter()` su una sequenza di nomi per individuare quelli che iniziano per `A`:

```py
>>> nomi = ['Angelo', 'Andrea', 'Giovanni', 'Paolo', 'Mario', 'Luca']
>>> list(filter(lambda x: x[0] == 'A', nomi))
['Angelo', 'Andrea']
```

I nomi per i quali la funzione lambda restituisce `True` sono Angelo ed Andrea, come prevedibile. Il resto della sequenza viene quindi trascurato.

!!!note "Nota"
    Anche in questo caso avremmo potuto utilizzare una list comprehension, ottenendo una soluzione sicuramente maggiormente *pythonic*.

Potremmo anche concatenare le funzioni `map()` e `filter()` nella stessa chiamata. Se, ad esempio, volessimo ottenere i nomi che iniziano per `A` e convertirli in maiuscolo, potremmo usare la seguente istruzione:

```py
>>> list(map(lambda x: x.upper(), filter(lambda x: x[0] == 'A', nomi)))
['ANGELO', 'ANDREA']
```

In pratica, stiamo mappando la funzione lambda `x: x.upper()`, che trasforma le stringhe in maiuscolo, sui risultati della `filter()` precedentemente considerata.

## reduce()

La funzione `reduce()` non restituisce una nuova sequenza come `map()` o `filter()`. Invece, restituisce un singolo valreo. La sintassi è simile a quella delle altre due funzioni:

```py
reduce(function, *sequence)
```

In questo caso, `reduce()` applica la funzione agli elementi della sequenza, da sinsitra verso destra, iniziando con i primi due elementi della sequenza. Combiniamo quindi i risultati dellì'applciazione della funzione ai primi due elmeenti della sequezna con il terzo elemnto, passandolo ad un'altra chiamata alla stessa funzione. Questo processo si ripete fino a che non raggiungiamo la fine dell'iteratore, e questo viene ridotto ad un singolo valore.

Vediamo un esempio dove `reduce()` prende come argomento una funzione lambda che moltiplica due numeri consecutivamente:

```py
>>> from functools import reduce
>>> numeri = list(range(1, 5))
>>> numeri
[1, 2, 3, 4]
>>> reduce(lambda x, y: x*y, numeri)
24
```

!!!note "Nota"
    Notiamo che, a differenza di `map()` e `filter()`, la funzione `reduce()` non è integrata in Python, ma deve essere importata dalla libreria `functools`.

Se volessimo scrivere questa stessa funzione ricorrendo ad un approccio classic, potremmo usare un iteratore, oppure una serie ricorsiva di chiamate a funzione. Ad esempio:

```py
>>> def moltiplica(x, y):
...     return x*y
...
>>> moltiplica(moltiplica(moltiplica(4, 3), 2), 1) 
24
```
