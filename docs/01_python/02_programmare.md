# Programmare in Python

## Note fondamentali sulla sintassi

Abbiamo già accennato al fatto che il linguaggio Python sfrutta ampiamente il concetto di duck typing. Ecco alcuni altri concetti da tenere in considerazione dal punto di vista sintattico.

### Uso delle parentesi

In Python:

* le **parentesi tonde** sono usate soltanto nel caso di chiamata a funzione, oltre che per esprimere la precedenza nelle operazioni. In tutti gli altri casi, sono opzionali e possono essere omesse;
* le **parentesi quadre** sono usate per la creazione e l'accesso agli elementi di una lista;
* le **parentesi graffe** sono usate per la creazione dei dizionari.

### Termine delle istruzioni

In C e C++, il termine di un'istruzione è contrassegnato dal carattere `;` (il punto e virgola); in Python, invece, è necessario andare a capo.

### Ambito del codice e tabulazione

In C e C++, l'ambito era definito mediante le parentesi graffe. In Python, invece, è definito mediante le tabulazioni; come regola generale, il codice indentato allo stesso livello di tabulazione appartiene allo stesso ambito.

## Programmazione strutturata

Abbiamo visto che in C ed in C++ la sintassi per l'utilizzo delle strutture di controllo è comune; questo ricordiamo essere un effetto legato al fatto che il C++ altro non è se non un "superset" di istruzioni del C.

Il linguaggio Python, invece, pur condividendo l'insieme fondamentale di istruzioni utilizzate dal C e dal C++, utilizza una sintassi differente.

### Strutture di controllo

Partiamo dalla struttura di controllo `if`; nel seguente blocco di codice, vediamo la differenza tra un'implementazione in C/C++ ed una in Python della stessa istruzione condizionale.

=== "Python"
	```python
	>>> a = 5
	>>> if a < 5:
	...     print('a è minore di 5')
	... elif a == 5:
	...     print('a è uguale a 5')
	... else:
	...     print('a è maggiore di 5')
	...
	```

=== "C/C++"
	```cpp
	#include <iostream>

	using namespace std;

	int main ()
	{
		int a = 5;
		if (a < 5) {
			std::cout << "a è minore di 5" << std::endl;
		}
		else if (a == 5) {
			std::cout << "a è uguale a 5" << std::endl;
		}
		else {
			std::cout << "a è maggiore a 5" << std::endl;
		}
	}
	```

L'output che riceveremo in entrambi i casi è il seguente:

```bash
a è uguale a 5
```

Notiamo come la sintassi sia molto simile, anche se vi è un ovvio adattamento alle regole sintattiche già esplicitate in precedenza.

!!!note "Il costrutto switch"
	Python non implementa il costrutto `switch`. Qualora questo si reputi necessario, deve essere implementato mediante una serie di `if` ed `elif`, o anche mediante un apposito dizionario; in quest'ultimo caso, però, le applicazioni sono decisamente più limitate, e l'implementazione più complessa, anche se vi è un vantaggio in termini di performance.

### Cicli

#### Ciclo `for`

Un ciclo `for` in Python differisce leggermente da quelli visti in C/C++; infatti, laddove questi ultimi sono delle una vera e propria progressioni aritmetiche, contraddistinte da un valore iniziale, un incremento ed un valore terminale, in Python un ciclo `for` itera su una sequenza, come una lista o una stringa. Ad esempio, nel seguente blocco di codice vediamo come mostrare a schermo in maniera iterativa i numeri che vanno da 0 a 5:

=== "Python"
	```python
	>>> vals = [0,1,2,3,4]
	>>> for i in vals:
	...     print(i)
	```

=== "C/C++"
	```cpp
	#include <iostream>

	using namespace std;

	int main ()
	{
		for (int i = 0; i < 5; i++) {
			cout << i << endl;
		}
		return 0;
	}
	```

In entrambi i casi, il risultato che vedremo a schermo è il seguente:

```bash
0
1
2
3
4
```

E' quindi necessario un "cambio" di mentalità: infatti, per passare dal nostro codice C/C++ ad un equivalente Python, dovremo modificare tutti i nostri "range di iterazione" in liste o, in maniera più generica, *sequenze*. Il costo di questo "sforzo concettuale" è però ampiamente ripagato: infatti, nel seguente blocco di codice vediamo come è possibile iterare su una stringa:

=== "Python"
	```python
	>>> string = "Python"
	>>> for char in string:
	...     print(char)
	```

=== "C/C++"
	```cpp
	#include <iostream>
	#include <string>

	using namespace std;

	int main ()
	{
		string str ("C/C++");
		for (int i = 0; i < str.size(); i++) {
			cout << str[i] << endl;
		}
		return 0;
	}
	```

Il risultato è il seguente:

```bash
	P
	y
	t
	h
	o
	n
```

E' quindi evidente come sia l'interprete Python a farsi carico dell'astrazione di molte delle complessità di implementazione che si riscontrano nel linguaggio C/C++.

!!!note "Nota"
	Ovviamente, questa operazione *non è indolore*. Infatti, un codice Python, per quanto ottimizzato, *raramente* sarà in grado di offrire le stesse performance di un analogo codice (ottimizzato) C/C++. Tuttavia, nella maggior parte delle situazioni l'impatto in termini di performance è, ai nostri scopi, insignificante.

#### Ciclo `while`

Dal punto di vista semantico, il ciclo `while` è, a differenza del `for`, analogo alla controparte C/C++. Anche in questo caso, quello che cambia è la sintassi, come mostrato nel seguente blocco di codice:

=== "Python"
	```python
	>>> i = True
	>>> while (i):
	...     if randint(-5, 5) > 0:
	...         print("Continuo!")
	...     else:
	...         print("Esco!")
	...             i = False
	```

=== "C/C++"

	```cpp
	#include <iostream>
	#include <cstdlib>

	using namespace std;

	int main ()
	{
		bool i = true;
		while (i) {
			int randn = -5 + (rand() % (5 + 5 + 1));
			if (randn > 0) {
				cout << "Continuo!" << endl;
			} else {
				cout << "Esco!" << endl;
				i = false;
			}
		}
	}
	```

Il risultato che avremo è (pressappoco) il seguente:

```bash
Continuo!
Continuo!
Esco!
```

!!!note "I valori booleani in Python"
	I più attenti avranno notato come i valori booleani in Python siano stati scritti come `True` e `False`. Questo non è un refuso: la prima lettera è proprio una maiuscola.

#### La funzione `range()`

Ritorniamo per un attimo all'esempio che abbiamo fatto sul ciclo `for` in Python, che riportiamo di seguito per comodità.

```python
>>> vals = [0,1,2,3,4]
>>> for i in vals:
...     print(i)
```

Già in questa versione, il codice è molto più compatto della controparte C/C++; tuttavia, scrivere manualmente la sequenza per l'iterazione può essere un'operazione tediosa (e facilmente suscettibile all'errore). Python ci viene in aiuto mediante la funzione `range()`, che ha la seguente sintassi:

```python
range(i, j, s)
```

e genera la sequenza di tutti i numeri compresi tra `i` (incluso) e `j` (escluso) a passo `s`. Ad esempio, per generare i numeri compresi tra 0 e 4, possiamo scrivere:

```python
>>> r = range(0, 5, 1)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

!!!note "Nota"
	Per mandare a schermo la lista dei valori assunti dalla sequenza `r`, dovremo farne il cast in lista mediante l'operazione `list(r)`.

Qualora omessi, `i` e di `s` assumono i valori di default, ovvero 0 ed 1:

```python
>>> r = range(5)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

E' anche possibile specificare una sequenza decrementale facendo in modo che `i > j` ed `s < 0`:

```python
>>> r = range(5, 1, -1)
>>> print(list(r))
[5, 4, 3, 2]
```

##### Iterare su tutti gli elementi di una lista

Possiamo usare la funzione `range()` in accoppiata alla funzione `len()` per iterare sugli elementi di una lista:

```python
>>> l = ['Pippo', 'Pluto', 5, 'Paperino']
>>> for i in range(len(l)):
...     print(l[i])

Pippo
Pluto
5
Paperino
```

#### Istruzioni `break` e `continue`

Le istruzioni `break` e `continue` sono analoghe a quelle implementate in linguaggio C/C++, e permettono, rispettivamente, di uscire dal ciclo o di saltare all'iterazione successiva. Ad esempio:

=== "Python"
	```python
	>>> while (True):
	...     if randint(-5, 5) > 0:
	...         print("Continuo!")
	...			continue
	...     else:
	...         print("Esco!")
	...         break
	```

=== "C/C++"

	```cpp
	#include <iostream>
	#include <cstdlib>

	using namespace std;

	int main ()
	{
		while (true) {
			int randn = -5 + (rand() % (5 + 5 + 1));
			if (randn > 0) {
				cout << "Continuo!" << endl;
				continue;
			} else {
				cout << "Esco!" << endl;
				break;
			}
		}
	}
	```

##### Istruzione `else`

Python permette di usare un `else` in uscita da un ciclo in accoppiata con la funzione `break`. Ad esempio:

```python
>>> for i in range(2, 10):
...     for j in range(2, 5):
...             if i % j == 0:
...                 break
...     else:
...         print('{} non è divisibile per {}'.format(i, j))
...
5 non è divisibile per 4
7 non è divisibile per 4
```

Come evidente dal codice precedente, ogni volta che il ciclo interno termina con un `break`, il controllo ritorna al ciclo esterno, ma l'`else` non viene chiamato; quest'ultimo sarà chiamato soltanto quando il ciclo interno *non* viene interrotto.

!!!note "Nota"
	L'utilizzo di questa particolare forma dell'`else` è abbastanza poco comune, almeno nei casi standard, e può comunque essere sempre riformulata in maniera più semplice. Ai fini del corso, si consiglia l'adozione di un controllo di flusso e di una sintassi il più semplificati possibile.

## Definizione di funzioni

La sintassi usata per definire una funzione in Python è la seguente:

```python
def nome_funzione(parametri):
	# istruzioni
	return valore_ritorno
```

E' importante notare che:

* non è necessario definire un tipo di ritorno, ma soltanto un valore di ritorno. Qualora la funzione non restituisca alcun valore, semplicemente si ometterà l'istruzione `return`;
* non è (strettamente) necessario definire il tipo di ciascuno dei parametri passati;
* è consentito inserire dei parametri di default.

Ad esempio, la seguente funzione calcola il quadrato:

```python
>>> def calcola_area_quadrato(lato):
...     return lato * lato
...
>>> calcola_area_quadrato(5)
25
```

La seguente funzione concatena ad una lista il doppio dei singoli valori nella lista stessa:

```python
>>> l = [1,2]
>>> def raddoppia_lista(valore):
...     for i in range(len(valore)):
...             l.append(l[i] * 2)
...
>>> raddoppia_lista(l)
>>> l
[1, 2, 2, 4]
```

In questa funzione, invece, usiamo un parametro opzionale per specificare la lunghezza della lista generata in output:

```python
>>> def genera_lista_casuale(lunghezza=5):
...     l = []
...     for i in range(lunghezza):
...             l.append(randint(0, 10))
...     return l
...
>>> genera_lista_casuale()
[3, 1, 2, 0, 6]
>>> genera_lista_casuale(10)
[7, 9, 1, 10, 2, 4, 9, 1, 4, 8]
```

!!!warning "Tipo dei parametri di ingresso"
	Il duck typing fa sì che non sia posto alcun controllo sui parametri di ingresso. Ciò però non significa che l'interprete Python ci impedisca di chiamare (ad esempio) la funzione `genera_lista_casuale()` passando come parametro una stringa; tuttavia, ciò comporterà, come prevedibile, un errore a runtime.

### Passaggio di parametri a funzione

E' importante sottolineare come in Python i parametri siano passati ad una funzione **esclusivamente per valore**. Ad esempio:

```python
>>> def raddoppia(valore):
...     valore = valore * 2
...
>>> val = 1
>>> raddoppia(val)
>>> val
1
```

Notiamo come la funzione `raddoppia()` non abbia quindi avuto alcun effetto sulla variabile esterna! Ciò avviene proprio perché questa non è passata per reference, ma per valore.

Questo è il motivo per cui, qualora non si voglia avere un valore di ritorno in una ben determinata funzione, è necessario usare dei tipi mutabili (come nel caso della funzione `raddoppia_lista`, che accetta una lista, ovvero un tipo mutabile), oppure utilizzare le funzioni nell'ambito di una classe (torneremo su questo in avanti).

### L'istruzione `pass`

Chiudiamo accennando all'istruzione `pass`. Questa non fa assolutamente nulla; è utile, ad esempio, quando vogliamo inserire una funzione (o una classe) vuota, che definiremo per qualche motivo in seguito:

```python
>>> def passa():
...     pass
...
>>> passa()
```

!!!note "Nota"
	Anche se non scenderemo nei dettagli, l'istruzione `pass` è utile nella definizione delle classi astratte.
