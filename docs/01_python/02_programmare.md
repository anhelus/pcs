# Programmare in Python

## Note fondamentali sulla sintassi

Oltre al duck typing, esistono altri concetti che caratterizzano la sintassi di Python. Vediamoli brevemente.

1. Le **parentesi**:
	* **tonde** sono usate soltanto nel caso di chiamata a funzione, oltre che per esprimere la precedenza nelle operazioni. In tutti gli altri casi, sono opzionali e possono essere omesse;
	* **quadre** sono usate per la creazione e l'accesso agli elementi di una lista;
	* **graffe** sono usate per la creazione di un dizionario.
2. **Il termine di un'istruzione viene indicato andando a capo**.
3. **L'ambito del codice è definito mediante il numero di tabulazioni**. Come regola generale, il codice indentato ad un certo livello di tabulazione appartiene al medesimo ambito.

## Programmazione strutturata

Il linguaggio Python utilizza una sintassi per le strutture di controllo differente da quella usata nei tipici linguaggi C-like.

### Istruzioni condizionali (`if`)

Partiamo dall'istruzione condizionale `if`, mostrando la differenza tra l'implementazione in C/C++ e quella Python.

=== "Python"
	```py
	a = 5
	if a < 5:
	    print('a è minore di 5')
	elif a == 5:
	    print('a è uguale a 5')
	else:
	    print('a è maggiore di 5')
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

In entrambi i casi l'output a schermo sarà:

```bash
a è uguale a 5
```

La sintassi è, in realtà, abbastanza simile, anche se si tiene conto delle regole sintattiche indicate in precedenza.

### Pattern matching

Fino alla versione 3.10, Python non offriva il costrutto `switch/case`. A partire da quest'ultima, però, il *pattern matching* è stato implementato usando questa sintassi:

```py
match command:
	case "case 1":
		case_1()
	case "case 2":
		case()
	case unknown_command:
		print("Comando sconosciuto")
```

!!!warning "Attenzione"
	La versione 3.10 di Python è, al momento, ancora sperimentale. Non sarà quindi possibile nell'arco del corso ricorrere al pattern matching!

### Cicli

#### Ciclo `for`

Un ciclo `for` in Python differisce leggermente da quelli classici presenti in C/C++; infatti, laddove questi ultimi sono delle una vera e propria progressioni aritmetiche, contraddistinte da un valore iniziale, un incremento ed un valore terminale, in Python un ciclo `for` itera su una sequenza, come una lista o una stringa. Per fare un esempio, nel seguente blocco di codice vediamo come mostrare a schermo in maniera iterativa i numeri che vanno da 0 a 5:

=== "Python"
	```py
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

In entrambi i casi, il risultato che sarà stampato a schermo è:

```bash
0
1
2
3
4
```

Rispetto ai linguaggi "classici", quindi, occorre modificare tutti i "range di iterazione" in liste o, più genericamente, *iterabili*. Questo sforzo però è ampiamente ripagato dalla maggiore semplicità del codice; per fare un esempio, mostriamo come sia più semplice iterare su una stringa:

=== "Python"
	```py
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

A schermo vedremo in entrambi i casi il seguente risultato:

```bash
	P
	y
	t
	h
	o
	n
```

!!!warning "Attenzione"
	La maggiore semplicità sintattica offerta da Python non è indolore, ma ha un costo. Uno script Python, infatti, per quanto ottimizzato, non potrà quasi mai offrire performance paragonabili ad un codice ottimizzato in C o C++, a meno di non usare particolari (ed avanzati) accorgimenti. Tuttavia, il compromesso costi/benefici propende, per i nostri scopi, nettamente a favore di Python.

#### Ciclo `while`

A differenza del ciclo `for`, il funzionamento del `while` è analogo a quello della controparte C/C++. Anche in questo caso, ciò che cambia è la sintassi:

=== "Python"
	```py
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

A schermo vedremo:

```bash
Continuo!
Continuo!
Esco!
```

!!!note "I valori booleani in Python"
	I più attenti avranno notato come i valori booleani in Python siano stati scritti come `True` e `False`. Questo non è un refuso: la prima lettera è proprio una maiuscola.

#### La funzione `range()`

Torniamo adesso al precedente ciclo `for` per Python, che riportiamo di seguito.

```py
>>> vals = [0,1,2,3,4]
>>> for i in vals:
...     print(i)
```

Nonostante il codice sia già compatto, scrivere manualmente la sequenza da iterare può facilmente diventare un'operazione abbastanza complessa. Python ci viene quindi in aiuto tramite la funzione `range(i, j, s)`, che genera una sequenza avente tutti i numeri compresi tra `i` (incluso) e `j` (escluso) a passo `s`. Ad esempio, per generare i numeri compresi tra 0 e 4 scriveremo:

```py
>>> r = range(0, 5, 1)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

!!!note "Nota"
	Notiamo che per mandare in output i valori di `r` dovremo convertirlo in lista (`list(r)`).

Qualora omessi, `i` ed `s` assumono valori di default rispettivamente 0 ed 1:

```py
>>> r = range(5)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

E' anche possibile specificare una sequenza *decrementale* ponendo `i > j` ed `s < 0`:

```py
>>> r = range(5, 1, -1)
>>> print(list(r))
[5, 4, 3, 2]
```

##### Iterare su tutti gli elementi di una lista

Usando la funzione `range()` assieme alla funzione `len()` è possibile iterare sui singoli elementi di una lista:

```py
>>> l = ['Pippo', 'Pluto', 5, 'Paperino']
>>> for i in range(len(l)):
...     print(l[i])
Pippo
Pluto
5
Paperino
```

#### Istruzioni `break` e `continue`

Le istruzioni `break` e `continue` permettono rispettivamente di *uscire dal ciclo* o di *saltare all'iterazione successiva*. Ad esempio:

```py
>>> while (True):
...     if randint(-5, 5) > 0:
...         print("Continuo!")
...			continue
...     else:
...         print("Esco!")
...         break
```

## Definire una funzione

In Python è possibile definire una funzione in questo modo:

```py
def nome_funzione(parametri):
	# istruzioni
	return valore_ritorno
```

E' importante notare che:

* non è necessario definire un tipo, ma soltanto un *valore* di ritorno. Qualora la funzione non restituisca alcun valore, potrà essere omessa l'istruzione `return`;
* non è (strettamente) necessario definire il tipo di ciascuno dei parametri passati;
* è consentito inserire dei parametri di default.

### Esempio di funzioni

La seguente funzione concatena ad una lista il doppio dei singoli valori nella lista stessa:

```py
>>> def raddoppia_lista(lista):
...     for i in range(len(lista)):
...             lista.append(l[i] * 2)
...
>>> l = [1,2]
>>> raddoppia_lista(l)
>>> l
[1, 2, 2, 4]
```

In questa funzione, invece, usiamo un parametro opzionale per specificare la lunghezza della lista generata in output:

```py
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
	Il duck typing fa sì che non venga effettuato alcun controllo sui parametri in ingresso. Ciò però non significa che non si possa provare a chiamare (ad esempio) la funzione `genera_lista_casuale()` passando come parametro una stringa; ciò tuttavia causerà un (prevedibile) errore.

### Passaggio di parametri a funzione

Python prevede che i parametri siano passati ad una funzione *esclusivamente per valore*. Ad esempio:

```py
>>> def raddoppia(valore):
...     valore = valore * 2
...
>>> val = 1
>>> raddoppia(val)
>>> val
1
```

Come evidente, la funzione `raddoppia()` non ha avuto alcun effetto sulla variabile `val`; ciò avviene proprio perché il passaggio è stato effettuato proprio per valore. Questo è il motivo per cui, qualora non si voglia avere un valore di ritorno in una ben determinata funzione, è necessario usare dei tipi mutabili (come nel caso della funzione `raddoppia_lista`, che accetta una lista, ovvero un tipo mutabile), oppure utilizzare le funzioni nell'ambito di una classe (torneremo su questo in avanti).

### L'istruzione `pass`

Chiudiamo accennando all'istruzione `pass`. Questa non fa assolutamente nulla; è utile, ad esempio, quando vogliamo inserire una funzione (o una classe) vuota, che definiremo per qualche motivo in seguito:

```py
>>> def funzione_vuota():
...     pass
...
>>> funzione_vuota()
```

!!!note "Nota"
	Anche se di primo acchitto potrebbe non essere evidente, l'istruzione `pass` è *estremamente* utile.

## Conclusioni

In questa lezione, abbiamo visto alcune delle tecniche fondamentali da padroneggiare per quello che riguarda la programmazione strutturata in Python. Nella prossima lezione, ci focalizzeremo su alcune possibili applicazioni delle liste.
