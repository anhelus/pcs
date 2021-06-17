# List comprehension

## Forma base

Una delle tecniche più usate per effettuare delle operazioni sugli elementi di una lista è usare la tecnica della *list comprehension*, che permette di sostituire *quasi* completamente i classici cicli.

Nella forma base, una list comprehension ha una sintassi di questo tipo:

```py
lista_output = [f(elemento) for elemento in lista_input]
```

In altre parole, otterremo in output una lista (`lista_output`) applicando ad ogni `elemento` della lista originaria (`lista_input`) la funzione `f()`.

!!!note "Nota"
	Per essere precisi, più che di lista, sarebbe opportuno parlare di iterabile di input.

## Forma estesa con if-else

La list comprehension può anche includere delle istruzioni condizionali. Un primo esempio è la seguente forma:

```py
lista_output_if = [f(elemento) for elemento in lista_input if condizione]
```

In questo caso, la funzione `f()` sarà chiamata esclusivamente sugli elementi che soddisfano la `condizione` indicata. Invece, se usassimo questa forma:

```py
lista_output_if_else = [f(elemento) if condizione else g(elemento) for elemento in lista_input]
```

la funzione `f()` sarebbe invocata su tutti gli elementi che soddisfano la `condizione`, mentre la funzione `g()` su tutti quelli che non la soddisfano.

Vediamo adesso qualche esempio di applicazione.

## Esempio 1: selezionare i nomi da una lista

Supponiamo di voler selezionare tutti i nomi che iniziano con la lettera "B". Se usassimo un classico ciclo `for`, potremmo scrivere:

```py
>>> lista_nomi = ["Jax Teller", "Walter White", "Billy Butcher", "Luke Skywalker", "Bobby Singer", "Johnny Lawrence"]
>>> output = []
>>> for nome in lista_nomi:
		if nomi[0] == "B":
			output.append(nome)
>>>	print(output)
['Billy Butcher', 'Bobby Singer']
```

Decidendo di usare invece una list comprehension:

```py
>>> output = [nome for nome in lista_nomi if nome[0] == "B"]
>>> print(output)
['Billy Butcher', 'Bobby Singer']
```

## Esempio 2: calcolo dei quadrati

Vediamo come usare una list comprehension per ottenere una nuova lista applicando a tutti gli elementi di una sequenza una certa funzione. Ad esempio, potremmo voler ottenere la lista dei quadrati di una certa sequenza:

```py
>>> def quadrato(numero):
		return numero ** 2
>>> output = []
>>> for i in range(10):
		output.append(quadrato(i))
>>> output
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Utilizzando la list comprehension:

```py
>>> output = [quadrato(i) for i in range(10)]
>>> output
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Esempio 3: lista dei numeri pari e dispari

Facciamo un ultimo esempio usando una list comprehension per "contrassegnare" tutti i numeri da 0 a 10 in base al fatto che siano pari o dispari. Al solito, vediamo come farlo usando un ciclo:

```py
>>> output = []
>>> for i in range(1, 10):
		if i % 2 == 0:
			output.append("{} è pari".format(i))
		else:
			output.append("{} è dispari".format(i))
>>> output
['1 è dispari', '2 è pari', '3 è dispari', '4 è pari', '5 è dispari', '6 è pari', '7 è dispari', '8 è pari', '9 è dispari']
```

Usando una list comprehension, invece:

```py
>>> output = ["{} è pari".format(i) if i % 2 == 0 else "{} è dispari".format(i) for i in range(1, 10)]
>>> output
['1 è dispari', '2 è pari', '3 è dispari', '4 è pari', '5 è dispari', '6 è pari', '7 è dispari', '8 è pari', '9 è dispari']
```

## In definitiva...

Le list comprehension sono utili e versatili, e permettono, in molti casi, di sostituire i classici cicli con una sintassi più snella. Tuttavia, bisogna fare attenzione a non abusare di questo strumento: infatti, facendolo si rischia di complicare inutilmente il nostro programma, rendendolo poco leggibile e manutenibile.

Come regola generale, quindi, ricordiamo il principio del rasoio di Occam: anche se è facile innamorarsi delle list comprehension, è bene ricordarsi che anche i cicli sono *leciti e funzionali*, per cui non è sempre necessario trovare a tutti i costi una soluzione usando una list comprehension.

## Post scriptum: assignment expressions

Come apparso dalla trattazione, le list comprehension sono state pensate per approcci puramente iterativi. Di conseguenza, risulta complesso implementare forme di ricorsione. Per ovviare a questo inconveniente, Python introduce, a partire dalla versione 3.8, le *assignment expression*.

Da un punto di vista "formale", un'assignment expression permette di *assegnare* e *restituire* un valore all'interno di un'unica istruzione mediante il cosiddetto *walrus operator*:

```py
>>> print(enjoy := True)
True
```

Vediamo come utilizzare questo concetto per combinare ricorsione e list comprehension. Definiamo i valori di $F_0$ ed $F_1$ per la [sequenza di Fibonacci](https://it.wikipedia.org/wiki/Successione_di_Fibonacci):

```py
>>> fib = [0, 1]
```

Vediamo cosa succede se proviamo ad usare una assignment expression in modo da restituire una lista che abbia come primo elemento il secondo della precedente (ovvero `1`), e come secondo la somma di tutti gli elementi della lista (ovvero `0 + 1`):

```py
>>> (fib := [fib[1], fib[0] + fib[1]])
>>> fib
[1, 1]
```

Notiamo che l'operazione ha modificato il valore della lista `fib`! A noi, però, interessa soltanto la somma degli elementi precedenti della lista (e quindi il secondo valore ottenuto). Per isolarlo, possiamo adoperare l'operatore booleano `and`:

```py
>>> (fib := [fib[1], fib[0] + fib[1]]) and fib[1]
1
```

Proviamo a combinare i due passaggi precedenti, ed usare una list comprehension per concatenare i risultati ottenuti per i numeri che vanno fino ad $F_9$:

```py
>>> fib = [0, 1]
>>> fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1] for i in range(10)]
>>> fib
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
