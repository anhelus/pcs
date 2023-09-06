# 1.1.4 - Liste

INTEGRAZIONE: # Liste

La classe `list` èp uno dei tipi built-in più utilizzati in Python. Ha un notevole set di utili feature, e ci permette di organizzare in modo efficiente e manipolare dati eterogenei. Sapere come usare le liste è una skill fondamentale come sviluppatore Python. Le liste hanno molti casi d'uso, per cui le utilizzeremo di frequente nel codice reale.

In questo articolo, vedremo le liste nel dettaglio, ed otterremo una comprensione solida delle loro feature chiave. Questa conoscenza ci permetterà di scrivere codice più efficace sfrruttandole.

Vedremo quindi come:

- **creare** nuove liste in Python;
- **accedere** agli oggetti in una lista esistente;
- **copiare, aggionrare, accrescere, ridurre, e concatenare** liste esistenti;
- **ordinare, invertire** ed **attraversare** liste esistenti;
- usare altre feature delle liste Python.

Inoltre, scriveremo il codice per alcuni esempi che mostrano degli casi d'usi comuni per le liste in Python. Ci aiuteranno ad usare al meglio le liste nel nostro codice.

Per ottenre il massimo da questo tutorial, dovbbiamo avere un buona comprensione di concetti base del linguaggio Python, inclusi variabili, funzioni, e cicli for. Sarà anche il caso di avere familiarità con altri data type buiolòt-in,m come stringhe, tuple, dizionari ed insiemi.

## Il tipo di dato list

Le liste Python sono dei tipi di dati built-in flessibili,v ersabili, potenti e molto popolari. Ci permettono di creare sequenze a lunghezza variabile e m,utabili di oggetti. In una lista, possiamo memorizzare oggeti di qualsiasi tipo. POssiamo anche mescolare tra loro oggetti di versi tipo all'interno della stessa lista, anche se gli elementi della lista spesso condividono lo stesso tipo.

Alcun e delle caratteristiche più rilevanti di una lista includono le seguenti:

- ordinamento: la lista contiene elemento o oggetti che sono disposti sequenzialmente secondo il loro specifico ordine di inserimento
- zero-based: ci permettono di accedere ai loro elementi mediante delgi indici che iniziano da zero
- mutabilità: supportano mutamenti in-place o cambi agli elementi contenuti
- eterogenee: possono memorizzare oggetti di tipio differenti
- dinamiche: possono aumentare o diminuire di dimensione in maneira dinamica, il che significa che supportano l'addizione, inserimento e rimozione di elementi
- slicing: supportano l'operaizone di slici, il che significa che possiamo estrarre una serie di elementi da qeuste
- combinabili: supportano le operazioni di concatenazione, per cui possiamo combinare du eo più piste usando gli operatori di concatenzione
- copiabili: ci permettono di fare copie dei loro contenuti meidante diverse tecniche

Le liste sono quindi sequenze di oggetti. Sono chiamate comunemente _container_ o _collezioni_ perché una singola lista può contenere un numero arbitrario di altri oggetti.

!!!note
	In Python, le liste supportano un set ricco di operazioni che sono comuni a tutte le sequenze, incluse tuyple, stringhe,m e range. Questeo operazioni sono consociute come _common sequence operations_.

In Python, le liste sono ordinete, il che signifca che mangengono gli elementi nell'ordine in cui vengono inseriti.

>>> colors = [
...     "red",
...     "orange",
...     "yellow",
...     "green",
...     "blue",
...     "indigo",
...     "violet"
... ]

>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

Gli oggetti nella lista sono stringhe che rappresentano dei colori. Se accediamo all'oggetto nella lista, allora vedremo che i colori mangengono lo stesso ordine nel quale li abbiamo inseriti nella lista. Questo ordine rimane immutando durante il tempo di vita della lista a meno che non facciamo delle modifiche sulla stessa.

Possiamo accedere ad un singolo oggetto in una lista usando la sua posizione, o indice, nelal sequenza. Gli indici in Python partono da zero:

>> colors[0]
'red'
>>> colors[1]
'orange'
>>> colors[2]
'yellow'
>>> colors[3]
'green'

Le posizioni sono quindi numerate da zero alla lunghezza della lista meno uno. L'elemento all'indiice 0 è il primo elemento nella lista, l'elemento all'indice 1 il secondo, e così via.

Le liste possono contenere oggetti di diverso tipo. Ecco perché si dice che le liste sono delle *collezioni eterogenee*.

[42, "apple", True, {"name": "John Doe"}, (1, 2, 3), [3.14, 2.78]]

Quest alista contiene ad esempio oggetti di diverso tipo, inclusi numeri,s tringhe,m valori boleani, dizionari, tuple, ed un'aòltra lista. Anche se questa feature delle lista può sembrare utile, nella pratica vedremo che spesso le liste memorizzano dati omogenei.

!!!note
	Una delle caratteristiche più rilevanti delle liste è che sono dei tipi di dati mutabili. Quyesta feature influenza pesantemente il loro comportamento ed i casi d'uso. Per esempio, la mutabilità implica che le liste non sono *hashable*é, per cui non possiamo suarle come chiavi di un dizionario.

Terminiamo questa panoramica sulle liste, e scendiamo adesso nel dettaglio delle loro feature.

## Costruire le liste in Python

Per prima cosa, se vogliamo usar euna lsita per memorizzare o collezionare dei dati nel codice, dobbiamo crearne una. Abbiamo diversi modi di creare delle liste in Python. Questa è una delle feature che le rende versatili e popolari.

Per esempio, possiamo creare delle liste usando uno dei sequenti strumenti:

* literals
* costruttore list()
* list comprehjension

##### Literals

I literals sono probabilmente il modo più popolare di creare un oggetto di tipo list in Python. Questi literal sono abbastanza semplici da utilizzare: in pratica, sono una coppia di parentesi quadre che racchiudono una serie di oggetti separati da una virgola.

Ecco la sintgasssi generale di un literal per le liste:

[item_0, item_1, ..., item_n]

Questa sintassi crea una lista di n oggetti elencando gli oggetti in una coppia chiusa di parentesi quadre. Notiamo che non dobbiamo dichiarare il tipo degli oggetti o la dimensione della lista a priori. Ricordiamo che le liste hanno una dimnensione variabile e possono memorizzare oggetti di tipo eterogeneo.

Ecco alcuni esempi di come possiamo usare la sintassi del literal per creaqre nuove liste:

>>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> fruits = ["apple", "banana", "orange", "kiwi", "grape"]
>>> cities = [
...     "New York",
...     "Los Angeles",
...     "Chicago",
...     "Houston",
...     "Philadelphia"
... ]

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]

>>> inventory = [
...     {"product": "phone", "price": 1000, "quantity": 10},
...     {"product": "laptop", "price": 1500, "quantity": 5},
...     {"product": "tablet", "price": 500, "quantity": 20}
... ]

>>> functions = [print, len, range, type, enumerate]

>>> empty = []

In questi esempi, usiamo questa sintassi per creare liste che contengono numeri, stringhe, altre liste, dizionari, o anche delel funzioni. Come già sappiamo, le liste posssono memorizzare un qualsiasi tipo di oggetto. Possono anche essere vuote, come l'ultima lista nel nostro esepio.,

Le liste vuote sono utili in mol,te situazioni. Per esempio, potremmo voler creare una slita di oggetti che risultano dai calcoli eseguiti in un loop. Il ciclo ci permette di popolare la lista vuota un elementom alla votla.

Usare un literal è probahbilmente l modo più comune di creare delle liste. Troveremo questi literal in molti esempi Python e  codebase. Sono utili qunado abbiamo uan serie di elemnti coin signfiicato strettamente correlato, e vogliamo metterli insieme in una singola struttura dati.

Notiamo che dare un nome pluarre alle liste è una pratica coimune che migliroa la leggibilità. tuttavia, non è una regola.

##### COSTRuttore list

Un altro strumetno che ci permette di creare oggetti di classe list è il costruttore list(). Possiamo chiamare questo costruttore con ogni oggetto di tipo iterablie, incluse altre liste, tuple, setr, dizionri e i loro componenti, stringhe, e molto altro. Possiamo anche chiamarlo senza alcun argomento, nel qual caso avremo una lista vuotra.

Ecco la sintassi generale:

```py
list([iterable])
```

Per creare una lista, dobbiamo chiamrae `list()` come chiameremmo un qualsiasi altro costruttore di classe. Notiamo che le parentesi quadre che circondano `iterable` indicano che l'argomento è opzionale, per cui le parentesi non sono parte della sintassi. Ecco alcuni esempi:

```py
>>> list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list({"circle", "square", "triangle", "rectangle", "pentagon"})
['square', 'rectangle', 'triangle', 'pentagon', 'circle']

>>> list({"name": "John", "age": 30, "city": "New York"}.items())
[('name', 'John'), ('age', 30), ('city', 'New York')]

>>> list("Pythonista")
['P', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a']

>>> list()
[]
```

In questi esempi, creiamo diverse liste usando il copstruttore list(), che accetta un qualsiasi tipo di oggetto iterabile, incluse tuple, dizionari, stringhe, e molte altri. Accetta anche degli insiemi, nel qual caso dobbiamo ricordare che gli insisemi sono struture dati non ordinati, per cui non saremo in grado di rpedire l'ordin e finale delgi oggetti nella lista risultante.

Chiamare list() senza un argomento crea e restituisce una nuova lista vuota. Quesot modo di carere liste vuote è meno comune di usare una coppia vuota di parentesi quadre. Tuttavia, in alcune situazioni, può rendere il codice più esplciito comunicando chiaramente il nostro itnento: creare una lista vuota.

Il costruttore list() +è utile specialmente quando dobbiamo creare una lista da un oggetto iterator. Per esempio, diciamo di avere una funzione generator che restituisce i numeri dalla sequenza di Fibonacci, e dobbiamo memorizzare i primi dieci numeri di questa in una lista.

In questo caso, possiamo usare list() come segue:

>>> def fibonacci_generator(stop):
...     current_fib, next_fib = 0, 1
...     for _ in range(0, stop):
...         fib_number = current_fib
...         current_fib, next_fib = next_fib, current_fib + next_fib
...         yield fib_number
...

>>> fibonacci_generator(10)
<generator object fibonacci_generator at 0x10692f3d0>

>>> list(fibonacci_generator(10))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Chiamare fibonacci_generator() restituisce direttamente un iteratore che ci permette di iterare sui numeri della sequenza di Fibonacci fino all'indice sceltgo. Tuttavia, non abbiamo bisogno di un iterator nel nostro codice. Abbiamo bisogno di una lista. Un modo semplice per ottenrla è uisare l'iteratore con una chiamata a list(), come fatto in precedentza.



https://realpython.com/python-list/#using-the-list-constructor 

Using the list() Constructor
Another tool that allows you to create list objects is the class constructor, list(). You can call this constructor with any iterable object, including other lists, tuples, sets, dictionaries and their components, strings, and many others. You can also call it without any arguments, in which case you’ll get an empty list back.

Here’s the general syntax:

list([iterable])
To create a list, you need to call list() as you’d call any class constructor or function. Note that the square brackets around iterable mean that the argument is optional, so the brackets aren’t part of the syntax. Here are a few examples of how to use the constructor:

>>> list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list({"circle", "square", "triangle", "rectangle", "pentagon"})
['square', 'rectangle', 'triangle', 'pentagon', 'circle']

>>> list({"name": "John", "age": 30, "city": "New York"}.items())
[('name', 'John'), ('age', 30), ('city', 'New York')]

>>> list("Pythonista")
['P', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a']

>>> list()
[]
In these examples, you create different lists using the list() constructor, which accepts any type of iterable object, including tuples, dictionaries, strings, and many more. It even accepts sets, in which case you need to remember that sets are unordered data structures, so you won’t be able to predict the final order of items in the resulting list.

Calling list() without an argument creates and returns a new empty list. This way of creating empty lists is less common than using an empty pair of square brackets. However, in some situations, it can make your code more explicit by clearly communicating your intent: creating an empty list.

The list() constructor is especially useful when you need to create a list out of an iterator object. For example, say that you have a generator function that yields numbers from the Fibonacci sequence on demand, and you need to store the first ten numbers in a list.

In this case, you can use list() as in the code below:

>>> def fibonacci_generator(stop):
...     current_fib, next_fib = 0, 1
...     for _ in range(0, stop):
...         fib_number = current_fib
...         current_fib, next_fib = next_fib, current_fib + next_fib
...         yield fib_number
...

>>> fibonacci_generator(10)
<generator object fibonacci_generator at 0x10692f3d0>

>>> list(fibonacci_generator(10))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Calling fibonacci_generator() directly returns a generator iterator object that allows you to iterate over the numbers in the Fibonacci sequence up to the index of your choice. However, you don’t need an iterator in your code. You need a list. A quick way to get that list is to wrap the iterator in a call to list(), as you did in the final example.

This technique comes in handy when you’re working with functions that return iterators, and you want to construct a list object out of the items that the iterator yields. The list() constructor will consume the iterator, build your list, and return it back to you.

Note: You can also use the literal syntax and the iterable unpacking operator (*) as an alternative to the list() constructor.

Here’s how:

>>> [*fibonacci_generator(10)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
In this example, the iterable unpacking operator consumes the iterator, and the square brackets build the final list of numbers. However, this technique is less readable and explicit than using list().

As a side note, you’ll often find that built-in and third-party functions return iterators. Functions like reversed(), enumerate(), map(), and filter() are good examples of this practice. It’s less common to find functions that directly return list objects, but the built-in sorted() function is one example. It takes an iterable as an argument and returns a list of sorted items.


Remove ads
Building Lists With List Comprehensions
List comprehensions are one of the most distinctive features of Python. They’re quite popular in the Python community, so you’ll likely find them all around. List comprehensions allow you to quickly create and transform lists using a syntax that mimics a for loop but in a single line of code.

The core syntax of list comprehensions looks something like this:

[expression(item) for item in iterable]
Every list comprehension needs at least three components:

expression() is a Python expression that returns a concrete value, and most of the time, that value depends on item. Note that it doesn’t have to be a function.
item is the current object from iterable.
iterable can be any Python iterable object, such as a list, tuple, set, string, or generator.
The for construct iterates over the items in iterable, while expression(item) provides the corresponding list item that results from running the comprehension.

To illustrate how list comprehensions allow you to create new lists out of existing iterables, say that you want to construct a list with the square values of the first ten integer numbers. In this case, you can write the following comprehension:

>>> [number ** 2 for number in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
In this example, you use range() to get the first ten integer numbers. The comprehension iterates over them while computing the square and building the new list. This example is just a quick sample of what you can do with a list comprehension.

Note: To dive deeper into list comprehensions and how to use them, check out When to Use a List Comprehension in Python.

In general, you’ll use a list comprehension when you need to create a list of transformed values out of an existing iterable. Comprehensions are a great tool that you need to master as a Python developer. They’re optimized for performance and are quick to write.

Accessing Items in a List: Indexing
You can access individual items from a list using the item’s associated index. What’s an item’s index? Each item in a list has an index that specifies its position in the list. Indices are integer numbers that start at 0 and go up to the number of items in the list minus 1.

To access a list item through its index, you use the following syntax:

list_object[index]
This construct is known as an indexing operation, and the [index] part is known as the indexing operator. It consists of a pair of square brackets enclosing the desired or target index. You can read this construct as from list_object give me the item at index.

Here’s how this syntax works in practice:

>>> languages = ["Python", "Java", "JavaScript", "C++", "Go", "Rust"]
>>> languages[0]
'Python'
>>> languages[1]
'Java'
>>> languages[2]
'JavaScript'
>>> languages[3]
'C++'
>>> languages[4]
'Go'
>>> languages[5]
'Rust'
Indexing your list with different indices gives you direct access to the underlying items. If you use the Big O notation for time complexity, then you can say that indexing is an O(1) operation. This means that lists are quite good for those situations where you need to access random items from a series of items.

Here’s a more visual representation of how indices map to items in a list:

"Python"	"Java"	"JavaScript"	"C++"	"Go"	"Rust"
0	1	2	3	4	5
In any Python list, the index of the first item is 0, the index of the second item is 1, and so on. The index of the last item is the number of items minus 1.

The number of items in a list is known as the list’s length. You can check the length of a list by using the built-in len() function:

>>> len(languages)
6
So, the index of the last item in languages is 6 - 1 = 5. That’s the index of the "Rust" item in your sample list. If you use an index greater than this number in an indexing operation, then you get an IndexError exception:

>>> languages[6]
Traceback (most recent call last):
    ...
IndexError: list index out of range
In this example, you try to retrieve the item at index 6. Because this index is greater than 5, you get an IndexError as a result. Using out-of-range indices can be an incredibly common issue when you work with lists, so keep an eye on your target indices.

Indexing operations are quite flexible in Python. For example, you can also use negative indices while indexing lists. This kind of index gives you access to the list items in backward order:

>>> languages[-1]
'Rust'
>>> languages[-2]
'Go'
>>> languages[-3]
'C++'
>>> languages[-4]
'JavaScript'
>>> languages[-5]
'Java'
>>> languages[-6]
'Python'
A negative index specifies an element’s position relative to the right end of the list, moving back to the beginning of the list. Here’s a representation of the process:

"Python"	"Java"	"JavaScript"	"C++"	"Go"	"Rust"
-6	-5	-4	-3	-2	-1
You can access the last item in a list using index -1. Similarly, index -2 specifies the next-to-last item, and so forth. It’s important to note that negative indices don’t start from 0 because 0 already points to the first item. This may be confusing when you’re first learning about negative and positive indices, but you’ll get used to it. It just takes a bit of practice.

Note that if you use negative indices, then -len(languages) will be the first item in the list. If you use an index lower than that value, then you get an IndexError:

>>> languages[-7]
Traceback (most recent call last):
    ...
IndexError: list index out of range
When you use an index lower than -len(languages), you get an error telling you that the target index is out of range.

Using negative indices can be very convenient in many situations. For example, accessing the last item in a list is a fairly common operation. In Python, you can do this by using negative indices, like in languages[-1], which is more readable and concise than doing something like languages[len(languages) - 1].

Note: Negative indices also come in handy when you need to reverse a list, as you’ll learn in the section Reversing and Sorting Lists.

As you already know, lists can contain items of any type, including other lists and sequences. When you have a list containing other sequences, you can access the items in any nested sequence by chaining indexing operations. Consider the following list of employee records:

>>> employees = [
...     ("John", 30, "Software Engineer"),
...     ("Alice", 25, "Web Developer"),
...     ("Bob", 45, "Data Analyst"),
...     ("Mark", 22, "Intern"),
...     ("Samantha", 36, "Project Manager")
... ]
How can you access the individual pieces of data from any given employee? You can use the following indexing syntax:

list_of_sequences[index_0][index_1]...[index_n]
The number at the end of each index represents the level of nesting for the list. For example, your employee list has one level of nesting. Therefore, to access Alice’s data, you can do something like this:

>>> employees[1][0]
'Alice'
>>> employees[1][1]
25
>>> employees[1][2]
'Web Developer'
In this example, when you do employees[1][0], index 1 refers to the second item in the employees list. That’s a nested list containing three items. The 0 refers to the first item in that nested list, which is "Alice". As you can see, you can access items in the nested lists by applying multiple indexing operations in a row. This technique is extensible to lists with more than one level of nesting.

If the nested items are dictionaries, then you can access their data using keys:

>>> employees = [
...     {"name": "John", "age": 30, "job": "Software Engineer"},
...     {"name": "Alice", "age": 25, "job": "Web Developer"},
...     {"name": "Bob", "age": 45, "job": "Data Analyst"},
...     {"name": "Mark", "age": 22, "job": "Intern"},
...     {"name": "Samantha", "age": 36, "job": "Project Manager"}
... ]

>>> employees[3]["name"]
'Mark'
>>> employees[3]["age"]
22
>>> employees[3]["job"]
Intern
In this example, you have a list of dictionaries. To access the data from one of the dictionaries, you need to use its index in the list, followed by the target key in square brackets.


Remove ads
Retrieving Multiple Items From a List: Slicing
Another common requirement when working with lists is to extract a portion, or slice, of a given list. You can do this with a slicing operation, which has the following syntax:

list_object[start:stop:step]
The [start:stop:step] part of this construct is known as the slicing operator. Its syntax consists of a pair of square brackets and three optional indices, start, stop, and step. The second colon is optional. You typically use it only in those cases where you need a step value different from 1.

Note: Slicing is an operation that’s common to all Python sequence data types, including lists, tuples, strings, ranges, and others.

Here’s what the indices in the slicing operator mean:

start specifies the index at which you want to start the slicing. The resulting slice includes the item at this index.
stop specifies the index at which you want the slicing to stop extracting items. The resulting slice doesn’t include the item at this index.
step provides an integer value representing how many items the slicing will skip on each step. The resulting slice won’t include the skipped items.
All the indices in the slicing operator are optional. They have the following default values:

Index	Default Value
start	0
stop	len(list_object)
step	1
The minimal working variation of the indexing operator is [:]. In this variation, you rely on the default values of all the indices and take advantage of the fact that the second colon is optional. The [::] variation of the slicing operator produces the same result as [:]. This time, you rely on the default value of the three indices.

Note: Both of the above variations of the slicing operator ([:] and [::]) allow you to create a shallow copy of your target list. You’ll learn more about this topic in the Shallow Copies of a List section.

Now it’s time for you to explore some examples of how slicing works:

>>> letters = ["A", "a", "B", "b", "C", "c", "D", "d"]

>>> upper_letters = letters[0::2] # Or [::2]
>>> upper_letters
['A', 'B', 'C', 'D']

>>> lower_letters = letters[1::2]
>>> lower_letters
['a', 'b', 'c', 'd']
In this example, you have a list of letters in uppercase and lowercase. You want to extract the uppercase letters into one list and the lowercase letters into another list. The [0::2] operator helps you with the first task, and [1::2] helps you with the second.

In both examples, you’ve set step to 2 because you want to retrieve every other letter from the original list. In the first slicing, you use a start of 0 because you want to start from the very beginning of the list. In the second slicing, you use a start of 1 because you need to jump over the first item and start extracting items from the second one.

You can use any variation of the slicing operator that fits your needs. In many situations, relying on the default indices is pretty helpful. In the examples above, you rely on the default value of stop, which is len(list_object). This practice allows you to run the slicing all the way up to the last item of the target list.

Here are a few more examples of slicing:

>>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> first_three = digits[:3]
>>> first_three
[0, 1, 2]

>>> middle_four = digits[3:7]
>>> middle_four
[3, 4, 5, 6]

>>> last_three = digits[-3:]
>>> last_three
[7, 8, 9]

>>> every_other = digits[::2]
>>> every_other
[0, 2, 4, 6, 8]

>>> every_three = digits[::3]
>>> every_three
[0, 3, 6, 9]
In these examples, the variable names reflect the portion of the list that you’re extracting in every slicing operation. As you can conclude, the slicing operator is pretty flexible and versatile. It even allows you to use negative indices.

Every slicing operation uses a slice object internally. The built-in slice() function provides an alternative way to create slice objects that you can use to extract multiple items from a list. The signature of this built-in function is the following:

slice(start, stop, step)
It takes three arguments with the same meaning as the indices in the slicing operator and returns a slice object equivalent to [start:stop:step]. To illustrate how slice() works, get back to the letters example and rewrite it using this function instead of the slicing operator. You’ll end up with something like the following:

>>> letters = ["A", "a", "B", "b", "C", "c", "D", "d"]

>>> upper_letters = letters[slice(0, None, 2)]
>>> upper_letters
['A', 'B', 'C', 'D']

>>> lower_letters = letters[slice(1, None, 2)]
>>> lower_letters
['a', 'b', 'c', 'd']
Passing None to any arguments of slice() tells the function that you want to rely on its internal default value, which is the same as the equivalent index’s default in the slicing operator. In these examples, you pass None to stop, which tells slice() that you want to use len(letters) as the value for stop.

As an exercise, you can write the digits examples using slice() instead of the slicing operator. Go ahead and give it a try! This practice will help you better understand the intricacies of slicing operations in Python.

Finally, it’s important to note that out-of-range values for start and stop don’t cause slicing expressions to raise a TypeError exception. In general, you’ll observe the following behaviors:

If start is before the beginning of the list, which can happen when you use negative indices, then Python will use 0 instead.
If start is greater than stop, then the slicing will return an empty list.
If stop is beyond the length of the list, then Python will use the length of the list instead.
Here are some examples that show these behaviors in action:

>>> colors = [
...     "red",
...     "orange",
...     "yellow",
...     "green",
...     "blue",
...     "indigo",
...     "violet"
... ]

>>> len(colors)
7

>>> colors[-8:]
['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

>>> colors[8:]
[]

>>> colors[:8]
['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
In these examples, your color list has seven items, so len(colors) returns 7. In the first example, you use a negative value for start. The first item of colors is at index -7. Because -8 < -7, Python replaces your start value with 0, which results in a slice that contains the items from 0 to the end of the list.

Note: In the examples above, you use only one colon in each slicing. In day-to-day coding, this is common practice. You’ll only use the second colon if you need to provide a step different from 1. Here’s an example where step equals 2:

>>> colors[::2]
['red', 'yellow', 'blue', 'violet']
In this example, you set step to 2 because you need a copy of colors that contains every other color. The slicing jumps over two colors in every step and gives you back a list of four colors.

In the second example, you use a start value that’s greater than the length of colors. Because there’s nothing to retrieve beyond the end of the list, Python returns an empty list. In the final example, you use a stop value that’s greater than the length of colors. In this case, Python retrieves all the items up to the end of the list.


Remove ads
Creating Copies of a List
Creating copies of an existing list is a common need in Python code. Having a copy ensures that when you change a given list, that change doesn’t affect the original data or the data in other copies.

Note: In Python, an object’s identity is a unique identifier that distinguishes it from other objects. You can use the built-in id() function to get the identity of any Python object. In Python’s CPython implementation, an object’s identity coincides with the memory address where the object is stored.

In Python, you’ll have two kinds of mechanisms to create copies of an existing list. You can create either:

A shallow copy
A deep copy
Both types of copies have specific characteristics that will directly impact their behavior. In the following sections, you’ll learn how to create shallow and deep copies of existing lists in Python. First, you’ll take a glance at aliases, a related concept that can cause some confusion and lead to issues and bugs.

Aliases of a List
In Python, you can create aliases of variables using the assignment operator (=). Assignments don’t create copies of objects in Python. Instead, they create bindings between the variable and the object involved in the assignment. Therefore, when you have several aliases of a given list, changes in an alias will affect the rest of the aliases.

To illustrate how you can create aliases and how they work, consider the following example:

>>> countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

>>> nations = countries
>>> id(countries) == id(nations)
True

>>> countries[0] = "United States of America"

>>> nations
['United States of America', 'Canada', 'Poland', 'Germany', 'Austria']
In this code snippet, the first highlighted line creates nations as an alias of countries. Note how both variables point to the same object, which you know because the object’s identity is the same. In the second highlighted line, you update the object at index 0 in countries. This change reflects in the nations alias.

Assignment statements like the one in the first highlighted line above don’t create copies of the right-hand object. They just create aliases or variables that point to the same underlying object.

In general, aliases can come in handy in situations where you need to avoid name collisions in your code or when you need to adapt the names to specific naming patterns.

To illustrate, say that you have an app that uses your list of countries as countries in one part of the code. The app requires the same list in another part of the code, but there’s already a variable called countries with other content.

If you want both pieces of code to work on the same list, then you can use nations as an alias for countries. A handy way to do this would be to use the as keyword for creating the alias through an implicit assignment, for example, when you import the list from another module.

Shallow Copies of a List
A shallow copy of an existing list is a new list containing references to the objects stored in the original list. In other words, when you create a shallow copy of a list, Python constructs a new list with a new identity. Then, it inserts references to the objects in the original list into the new list.

There are at least three different ways to create shallow copies of an existing list. You can use:

The slicing operator, [:]
The .copy() method
The copy() function from the copy module
These three tools demonstrate equivalent behavior. So, to kick things off, you’ll start exploring the slicing operator:

>>> countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

>>> nations = countries[:]
>>> nations
['United States', 'Canada', 'Poland', 'Germany', 'Austria']

>>> id(countries) == id(nations)
False
The highlighted line creates nations as a shallow copy of countries by using the slicing operator with one colon only. This operation takes a slice from the beginning to the end of countries. In this case, nations and countries have different identities. They’re completely independent list objects.

However, the elements in nations are aliases of the elements in countries:

>>> id(nations[0]) == id(countries[0])
True
>>> id(nations[1]) == id(countries[1])
True
As you can see, items under the same index in both nations and countries share the same object identity. This means that you don’t have copies of the items. You’re really sharing them. This behavior allows you to save some memory when working with lists and their copies.

Now, how would this impact the behavior of both lists? If you changed an item in nations, would the change reflect in countries? The code below will help you answer these questions:

>>> countries[0] = "United States of America"
>>> countries
['United States of America', 'Canada', 'Poland', 'Germany', 'Austria']

>>> nations
['United States', 'Canada', 'Poland', 'Germany', 'Austria']

>>> id(countries[0]) == id(nations[0])
False
>>> id(countries[1]) == id(nations[1])
True
On the first line of this piece of code, you update the item at index 0 in countries. This change doesn’t affect the item at index 0 in nations. Now the first items in the lists are completely different objects with their own identities. The rest of the items, however, continue to share the same identity. So, they’re the same object in each case.

Because making copies of a list is such a common operation, the list class has a dedicated method for it. The method is called .copy(), and it returns a shallow copy of the target list:

>>> countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

>>> nations = countries.copy()
>>> nations
['United States', 'Canada', 'Poland', 'Germany', 'Austria']

>>> id(countries) == id(nations)
False
>>> id(countries[0]) == id(nations[0])
True
>>> id(countries[1]) == id(nations[1])
True

>>> countries[0] = "United States of America"
>>> countries
['United States of America', 'Canada', 'Poland', 'Germany', 'Austria']
>>> nations
['United States', 'Canada', 'Poland', 'Germany', 'Austria']
Calling .copy() on countries gets you a shallow copy of this list. Now you have two different lists. However, their elements are common to both. Again, if you change an element in one of the lists, then the change won’t reflect in the copy.

You’ll find yet another tool for creating shallow copies of a list. The copy() function from the copy module allows you to do just that:

>>> from copy import copy

>>> countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

>>> nations = copy(countries)
>>> nations
['United States', 'Canada', 'Poland', 'Germany', 'Austria']

>>> id(countries) == id(nations)
False
>>> id(countries[0]) == id(nations[0])
True
>>> id(countries[1]) == id(nations[1])
True

>>> countries[0] = "United States of America"
>>> countries
['United States of America', 'Canada', 'Poland', 'Germany', 'Austria']
>>> nations
['United States', 'Canada', 'Poland', 'Germany', 'Austria']
When you feed copy() with a mutable container data type, such as a list, the function returns a shallow copy of the input object. This copy behaves the same as the previous shallow copies that you’ve built in this section.


Remove ads
Deep Copies of a List
Sometimes you may need to build a complete copy of an existing list. In other words, you want a copy that creates a new list object and also creates new copies of the contained elements. In these situations, you’ll have to construct what’s known as a deep copy.

When you create a deep copy of a list, Python constructs a new list object and then inserts copies of the objects from the original list recursively.

To create a deep copy of an existing list, you can use the deepcopy() function from the copy module. Here’s an example of how this function works:

>>> from copy import deepcopy

>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix_copy = deepcopy(matrix)

>>> id(matrix) == id(matrix_copy)
False
>>> id(matrix[0]) == id(matrix_copy[0])
False
>>> id(matrix[1]) == id(matrix_copy[1])
False
In this example, you create a deep copy of your matrix list. Note how both the lists and their sibling items have different identities.

Why would you need to create a deep copy of matrix, anyway? For example, if you only create a shallow copy of matrix, then you can face some issues when trying to mutate the nested lists:

>>> from copy import copy

>>> matrix_copy = copy(matrix)
>>> matrix_copy[0][0] = 100
>>> matrix_copy[0][1] = 200
>>> matrix_copy[0][2] = 300
>>> matrix_copy
[[100, 200, 300], [4, 5, 6], [7, 8, 9]]

>>> matrix
[[100, 200, 300], [4, 5, 6], [7, 8, 9]]
In this example, you create a shallow copy of matrix. If you change items in a nested list within matrix_copy, then those changes affect the original data in matrix. The way to avoid this behavior is to use a deep copy:

>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

>>> matrix_copy = deepcopy(matrix)
>>> matrix_copy[0][0] = 100
>>> matrix_copy[0][1] = 200
>>> matrix_copy[0][2] = 300
>>> matrix_copy
[[100, 200, 300], [4, 5, 6], [7, 8, 9]]

>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Now the changes in matrix_copy or any other deep copy don’t affect the content of matrix, as you can see on the highlighted lines.

Finally, it’s important to note that when you have a list containing immutable objects, such as numbers, strings, or tuples, the behavior of deepcopy() mimics what copy() does:

>>> countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
>>> nations = deepcopy(countries)

>>> id(countries) == id(nations)
False
>>> id(countries[0]) == id(nations[0])
True
>>> id(countries[1]) == id(nations[1])
True
In this example, even though you use deepcopy(), the items in nations are aliases of the items in countries. That behavior makes sense because you can’t change immutable objects in place. Again, this behavior optimizes the memory consumption of your code when you’re working with multiple copies of a list.

Updating Items in Lists: Index Assignments
Python lists are mutable data types. This means that you can change their elements without changing the identity of the underlying list. These kinds of changes are commonly known as in-place mutations. They allow you to update the value of one or more items in an existing list.

Note: To dive deeper into what mutable and immutable data types are and how they work in Python, check out Python’s Mutable vs Immutable Types: What’s the Difference?

To change the value of a given element in a list, you can use the following syntax:

list_object[index] = new_value
The indexing operator gives you access to the target item through its index, while the assignment operator allows you to change its current value.

Here’s how this assignment works:

>>> numbers = [1, 2, 3, 4]

>>> numbers[0] = "one"
>>> numbers
['one', 2, 3, 4]
>>> numbers[1] = "two"
>>> numbers
['one', 'two', 3, 4]

>>> numbers[-1] = "four"
>>> numbers
['one', 'two', 3, 'four']
>>> numbers[-2] = "three"
>>> numbers
['one', 'two', 'three', 'four']
In this example, you’ve replaced all the numeric values in numbers with strings. To do that, you’ve used their indices and the assignment operator in what you can call index assignments. Note that negative indices also work.

What if you know an item’s value but don’t know its index in the list? How can you update the item’s value? In this case, you can use the .index() method as in the code below:

>>> fruits = ["apple", "banana", "orange", "kiwi", "grape"]

>>> fruits[fruits.index("kiwi")] = "mango"
>>> fruits
['apple', 'banana', 'orange', 'mango', 'grape']
The .index() method takes a specific item as an argument and returns the index of the first occurrence of that item in the underlying list. You can take advantage of this behavior when you know the item that you want to update but not its index. However, note that if the target item isn’t present in the list, then you’ll get a ValueError.

You can also update the value of multiple list items in one go. To do that, you can access the items with the slicing operator and then use the assignment operator and an iterable of new values. This combination of operators can be called slice assignment for short.

Here’s the general syntax:

list_object[start:stop:step] = iterable
In this syntax, the values from iterable replace the portion of list_object defined by the slicing operator. If iterable has the same number of elements as the target slice, then Python updates the elements one by one without altering the length of list_object.

To understand these behaviors, consider the following examples:

>>> numbers = [1, 2, 3, 4, 5, 6, 7]

>>> numbers[1:4] = [22, 33, 44]
>>> numbers
[1, 22, 33, 44, 5, 6, 7]
In this example, you update the items located from 1 to 4, without including the last item. In this slice, you have three items, so you use a list of three new values to update them one by one.

If iterable has more or fewer elements than the target slice, then list_object will automatically grow or shrink accordingly:

>>> numbers = [1, 5, 6, 7]

>>> numbers[1:1] = [2, 3, 4]
>>> numbers
[1, 2, 3, 4, 5, 6, 7]
Now the initial list of numbers only has four values. The values 1, 2, and 3 are missing. So, you use a slice to insert them starting at index 1. In this case, the slice has a single index, while the list of values has three new values, so Python grows your list automatically to hold the new values.

You can also use a slice to shrink an existing list:

>>> numbers = [1, 2, 0, 0, 0, 0, 4, 5, 6, 7]

>>> numbers[2:6] = [3]
>>> numbers
[1, 2, 3, 4, 5, 6, 7]
Here, the initial list has a bunch of zeros where it should have a 3. Your slicing operator takes the portion filled with zeros and replaces it with a single 3.

Using the slicing operator to update the value of several items in an existing list is a pretty useful technique that may be hard to grasp at first. Go ahead and practice a bit more to get a deeper understanding of how this technique works.


Remove ads
Growing and Shrinking Lists Dynamically
In Python lists, mutability goes beyond allowing you to modify the items in place. Because lists are mutable, you can change their length on the fly by adding or removing elements. So, lists are also variable-length containers, as you already learned.

Adding new items to a list or removing unneeded ones are everyday tasks. That’s why Python provides different efficient ways to perform these actions. Using the right tool for the job is an essential skill.

In the following sections, you’ll explore the different tools that Python offers to grow and shrink a list dynamically.

Appending a Single Item at Once: .append()
The .append() method is probably the most common tool that you’ll use to add items to an existing list. As its name suggests, this method allows you to append items to a list. The method takes one item at a time and adds it to the right end of the target list.

Here’s an example of how .append() works:

>>> pets = ["cat", "dog"]

>>> pets.append("parrot")
>>> pets
['cat', 'dog', 'parrot']

>>> pets.append("gold fish")
>>> pets
['cat', 'dog', 'parrot', 'gold fish']

>>> pets.append("python")
>>> pets
['cat', 'dog', 'parrot', 'gold fish', 'python']
In these examples, every call to .append() adds a new pet at the end of your list. This behavior allows you to gradually populate an empty list or to add items to an existing list, as you did in the example.

Note: For a deep dive into how .append() works, check out Python’s .append(): Add Items to Your Lists in Place.

Using .append() is equivalent to doing the following slice assignment:

>>> pets[len(pets):] = ["hawk"]
>>> pets
['cat', 'dog', 'parrot', 'gold fish', 'python', 'hawk']
The slice assignment in this example grows your lists by appending a new item, "hawk", after the current last item in pets. This technique works the same as .append(). However, using .append() leads to a more readable and explicit solution.

An important fact to keep in mind when using .append() is that this method adds only a single item at a time. That item could be of any data type, including another list:

>>> pets.append(["hamster", "turtle"])
>>> pets
[
    'cat',
    'dog',
    'parrot',
    'gold fish',
    'python',
    'hawk',
    ['hamster', 'turtle']
]
Note how the last item in pets is a list of two pets rather than two new independent pets. This behavior may be a source of subtle errors. To avoid problems, you must remember that .append() takes and adds a single item each time.

If you need to add several items from an iterable at the end of an existing list, then you can use the .extend() method, which you’ll expore in the following section.

Extending a List With Multiple Items at Once: .extend()
When you’re working with lists, you may face the need to add multiple items to the right end of a list at once. Because this is such a common requirement, Python’s list has a dedicated method for that task.

The method is called .extend(). It takes an iterable of objects and appends them as individual items to the end of the target list:

>>> fruits = ["apple", "pear", "peach"]

>>> fruits.extend(["orange", "mango", "banana"])
>>> fruits
['apple', 'pear', 'peach', 'orange', 'mango', 'banana']
The .extend() method unpacks the items in the input iterable and adds them one by one to the right end of your target list. Now fruits has three more items on its end.

You should note that .extend() can take any iterable as an argument. So, you can use tuples, strings, dictionaries and their components, iterators, and even sets. However, remember that if you use a set as an argument to extend(), then you won’t know the final order of items beforehand.

Again, you must note that .extend() is equivalent to the following slice assignment:

>>> fruits = ["apple", "pear", "peach"]

>>> fruits[len(fruits):] = ["orange", "mango", "banana"]
>>> fruits
['apple', 'pear', 'peach', 'orange', 'mango', 'banana']
In this example, you use a slice assignment to add three items after the end of your original fruits list. Note that the result is the same as when you use .extend(). However, the .extend() variation is more readable and explicit.


Remove ads
Inserting an Item at a Given Position: .insert()
The .insert() method is another tool that you can use to add items to an existing list. This method is a bit different from .append() and .extend(). Instead of adding items at the right end of the list, .insert() allows you to decide where you want to put your item. That said, .insert() takes two arguments:

index: the index at which you want to insert the item
item: the item that you need to insert into the list
When you insert an item at a given index, Python moves all the following items one position to the right in order to make space for the new item, which will take the place of the old item at the target index:

>>> letters = ["A", "B", "F", "G"]

>>> letters.insert(2, "C")
>>> letters
['A', 'B', 'C', 'F', 'G']

>>> letters.insert(3, "D")
>>> letters
['A', 'B', 'C', 'D', 'F', 'G']

>>> letters.insert(4, "E")
>>> letters
['A', 'B', 'C', 'D', 'E', 'F', 'G']
In this example, you insert letters into specific positions in letters. You must insert one letter at a time because .insert() adds a single item in every call. To insert an item, the method shifts all the items starting from the target index to the right end of the list. This shifting makes space for the new item.

As an exercise, could you come up with a slice assignment that produces the same result as .insert()? Click the collapsible section below for the solution:


Now that you’ve learned how to add items to an existing list using different tools and techniques, it’s time to learn how to remove unneeded items from a list, which is another common task.

Deleting Items From a List
Python also allows you to remove one or more items from an existing list. Again, deleting items from lists is such a common operation that the list class already has methods to help you with that. You’ll have the following methods:

Method	Description
.remove(item)	Removes the first occurrence of item from the list. It raises a ValueError if there’s no such item.
.pop([index])	Removes the item at index and returns it back to the caller. If you don’t provide a target index, then .pop() removes and returns the last item in the list. Note that the square brackets around index mean that the argument is optional. The brackets aren’t part of the syntax.
.clear()	Removes all items from the list.
The .remove() method comes in handy when you want to remove an item from a list, but you don’t know the item’s index. If you have several items with the same value, then you can remove all of them by calling .remove() as many times as the item occurs:

>>> sample = [12, 11, 10, 42, 14, 12, 42]

>>> sample.remove(42)
>>> sample
[12, 11, 10, 14, 12, 42]

>>> sample.remove(42)
>>> sample
[12, 11, 10, 14, 12]

>>> sample.remove(42)
Traceback (most recent call last):
    ...
ValueError: list.remove(x): x not in list
The first call to .remove() deletes the first instance of the number 42. The second call removes the remaining instance of 42. If you call .remove() with an item that’s not in the target list, then you get a ValueError.

The .pop() method allows you to remove and return a specific item using its index. If you call the method with no index, then it removes and returns the last item in the underlying list:

>>> to_visit = [
...     "https://realpython.com",
...     "https://python.org",
...     "https://stackoverflow.com",
... ]

>>> visited = to_visit.pop()
>>> visited
'https://stackoverflow.com'
>>> to_visit
['https://realpython.com', 'https://python.org']

>>> visited = to_visit.pop(0)
>>> visited
'https://realpython.com'
>>> to_visit
['https://python.org']

>>> visited = to_visit.pop(-1)
>>> visited
'https://python.org'
>>> to_visit
[]
In these examples, the first call to .pop() removes and returns the last site in your list of sites to visit. The second call removes and returns the first site, which is the site at index 0.

Finally, you use .pop() with -1 as an argument to emphasize that you can also use negative indices. This call removes and returns the last item. At the end of the process, your list of sites to visit is empty, pointing out that you’ve done all your planned visits.

Removing all the items from a list in one go can be another frequent task. In this case, Python also has you covered because list has a method called .clear(), which does exactly that. Consider the following example:

>>> cache = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> cache.clear()
>>> cache
[]
If you call .clear() on a non-empty list object, then you get the list content completely removed. This method can be useful when your lists work as a cache that you want to quickly clean for a restart.

The following slice assignment produces the same result as the .clear() method:

>>> cache = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> cache[:] = []
>>> cache
[]
In this slice assignment, you assign an empty list to a slice that grabs the whole target list. Again, this syntax is less explicit and readable than using .clear().

There’s still one more Python tool that you can use to remove one or more items from an existing list. Yes, that’s the del statement. You can combine del with an indexing or slicing operation to remove an item or multiple items, respectively:

>>> colors = [
...     "red",
...     "orange",
...     "yellow",
...     "green",
...     "blue",
...     "indigo",
...     "violet"
... ]

>>> del colors[1]
>>> colors
['red', 'yellow', 'green', 'blue', 'indigo', 'violet']

>>> del colors[-1]
>>> colors
['red', 'yellow', 'green', 'blue', 'indigo']

>>> del colors[2:4]
>>> colors
['red', 'yellow', 'indigo']

>>> del colors[:]
>>> colors
[]
With the first del statement, you remove the color at index 1, which is "orange". In the second del, you use a negative index of -1 to remove the last color, "violet". Next, you use a slice to remove "green" and "blue".

Note: To dive deeper into using the del statement, check out Python’s del: Remove References From Scopes and Containers.

In the final example, you use del and a slice to remove all the items from an existing list. That construct produces a result that’s equivalent to calling .clear() on your target list.


Remove ads
Considering Performance While Growing Lists
When you create a list, Python allocates enough space to store the provided items. It also allocates extra space to host future items. When you use the extra space by adding new items to that list with .append(), .extend(), or .insert(), Python automatically creates room for additional new items.

This process is known as resizing, and while it ensures that the list can accept new items, it requires extra CPU time and additional memory. Why? Well, to grow an existing list, Python creates a new one with room for your current data and the extra items. Then it moves the current items to the new list and adds the new item or items.

Consider the following code to explore how Python grows a list dynamically:

>>> from sys import getsizeof

>>> numbers = []
>>> for value in range(100):
...     print(getsizeof(numbers))
...     numbers.append(value)
...
56
88
88
88
88
120
120
120
120
184
184
...
In this code snippet, you first import getsizeof() from the sys module. This function allows you to get the size of an object in bytes. Then you define numbers as an empty list.

Inside the for loop, you get and print your list object’s size in bytes. The first iteration shows that the size of your empty list is 56 bytes, which is the baseline size of every list in Python.

Next, the .append() method adds a new value to your list. Note how the size of numbers grows to 88 bytes. That’s the baseline size plus 32 additional bytes (56 + 4 × 8 = 88), which represent four 8-byte pointers or slots for future items. It means that Python went ahead and allocated space for four items when you added the first element.

As the loop goes, the size of numbers grows to 120 bytes, which is 88 + 4 × 8 = 120. This step allocates space for four more items. That’s why you get 120 four times on your screen.

If you follow the loop’s output, then you’ll notice that the next steps add room for eight extra items, then for twelve, then for sixteen, and so on. Every time Python resizes the list, it has to move all the items to the new space, which takes considerable time.

In practice, if you’re working with small lists, then the overall impact of this internal behavior is negligible. However, in performance-critical situations or when your lists are large, you may want to use more efficient data types, such as collections.deque, for example.

Check out the time complexity Wiki page for a detailed summary of how time-efficient list operations are. For example, the .append() method has a time complexity of O(1), which means that appending an item to a list takes constant time. However, when Python has to grow the list to make room for the new item, this performance will be a bit poorer.

Being aware of the time complexity of common list operations will significantly improve your ability to choose the right tool for the job, depending on your specific needs.

Concatenating and Repeating Lists
Another interesting and useful feature of Python’s list is that it supports the following two operations:

Concatenation, which uses the plus operator (+)
Repetition, which uses the multiplication operator (*)
In the following sections, you’ll learn how these two operations work on Python lists and how you can use them in your code.

Concatenating Lists
Concatenation consists of joining two things together. In this case, you’d like to concatenate two lists, which you can do using the plus operator (+). In this context, this operator is known as the concatenation operator.

Here’s how it works:

>>> [0, 1, 2, 3] + [4, 5, 6] + [7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
In this example, you combine three list objects using the concatenation operator. Note how the operator creates a new list containing all the individual items from the three original lists.

Whenever you use the concatenation operator, you get a new list object as a result. Consider the following example. Keep an eye on the identity of digits:

>>> digits = [0, 1, 2, 3, 4, 5]
>>> id(digits)
4558758720

>>> digits = digits + [6, 7, 8, 9]
>>> id(digits)
4470412224
In this example, you first create a list containing a few numbers. The id() function allows you to know the identity of this first list. Then you use a concatenation operation to complete your list of digits. Note how id() now returns a different value. This result confirms that the concatenation operator always creates a new list that joins its operands.

Note: You can only concatenate a list with another list. If you try to concatenate a list with something else, then you’ll get an exception:

>>> [0, 1, 2, 3, 4, 5] + (6, 7, 8, 9)
Traceback (most recent call last):
    ...
TypeError: can only concatenate list (not "tuple") to list
Python’s concatenation operator raises a TypeError exception when you try to concatenate a list with a different data type, such as a tuple.

The concatenation operator has an augmented variation, which uses the += operator. Here’s how this operator works:

>>> digits = [0, 1, 2, 3, 4, 5]
>>> digits += [6, 7, 8, 9]
>>> digits
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
The augmented concatenation operator works on an existing list. It takes a second list and adds its items, one by one, to the end of the initial list. The operation is a shortcut to something like digits = digits + [6, 7, 8, 9]. However, it works a bit differently.

Unlike the regular concatenation operator, the augmented variation mutates the target list in place rather than creating a new list:

>>> digits = [0, 1, 2, 3, 4, 5]
>>> id(digits)
4699578112

>>> digits += [6, 7, 8, 9]
>>> id(digits)
4699578112
In this example, the id() function returns the same value in both calls, meaning that you have a single list object instead of two. The augmented concatenation mutates digits in place, so the whole process is more efficient in terms of memory and execution time than a plain concatenation would be.


Remove ads
Repeating the Content of a List
Repetition consists of cloning the content of a given list a specific number of times. You can achieve this with the repetition operator (*), which takes two operands:

The list whose content you want to repeat
The number of times that you need to repeat the content
To understand how this operator works, consider the following example:

>>> ["A", "B", "C"] * 3
['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']

>>> 3 * ["A", "B", "C"]
['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
Here, you repeat the content of a list three times and get a new list as a result. In the first example, the left-hand operand is the target list, and the right-hand operand is an integer representing the number of times that you want to repeat the list’s content. In this second example, the operands are swapped, but the result is the same, as you’d expect in a multiplication operation.

The repetition operator also has an augmented variation that you’ll call the augmented repetition operator. This variation uses the *= operator. Here’s how it works:

>>> letters = ["A", "B", "C"]
>>> letters *= 3
>>> letters
['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
In the highlighted expression, the left-hand operand is the target list, while the right-hand operand is the integer value. You can’t swap them.

Again, the regular repetition operator returns a new list object containing the repeated data. However, its augmented variation mutates the target list in place, which makes it more efficient. As an exercise, go ahead and use the id() function to confirm this statement.

Reversing and Sorting Lists
Reversing and specially sorting lists of values are commonplace tasks in programming. In Python, you’ll have the built-in reversed() and sorted() functions to perform these tasks. When you’re working with lists, then you also have the .reverse() and .sort() methods, which reverse and sort the target list in place.

In the following sections, you’ll learn how to reverse and sort lists using the tools that Python provides for these tasks.

Reversing a List: reversed() and .reverse()
The built-in reversed() function takes a sequence as an argument and returns an iterator that yields the values of that sequence in reverse order:

>>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> reversed(digits)
<list_reverseiterator object at 0x10b261a50>

>>> list(reversed(digits))
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

>>> digits
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
When you call reversed() with a list as an argument, you get a reverse iterator object. This iterator yields values from the input list in reverse order. In this example, you use the list() constructor to consume the iterator and get the reversed data as a list.

Note: To dive deeper into reversing lists in Python, check out Reverse Python Lists: Beyond .reverse() and reversed().

The reversed() function doesn’t modify the input object. You’ll typically use reversed() in loops as a way to iterate over your data in reverse order. If you need to keep a reference to your data, then you can use list() and assign its return value to a new variable, which will be completely independent of your original sequence.

It’s important to note that reversed() retrieves items from the input sequence lazily. This means that if something changes in the input sequence during the reversing process, then those changes will reflect in the final result:

>>> numbers = [1, 2, 3]

>>> reversed_numbers = reversed(numbers)
>>> next(reversed_numbers)
3

>>> numbers[1] = 222
>>> next(reversed_numbers)
222

>>> next(reversed_numbers)
1
In this example, you use the built-in next() function to consume the iterator value by value. The first call to next() returns the last item from numbers. Then you update the value of the second item from 2 to 222. When you call next() again, you get 222 instead of 2. This is because reversed() doesn’t create a copy of the input iterable. Instead, it works with a reference to it.

The reversed() function is great when you want to iterate over a list in reverse order without altering the original list. What if you have a list, and for some reason, you need to reverse its content persistently? In that case, you can use the .reverse() method:

>>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> digits.reverse()
>>> digits
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
The .reverse() method reverses a list in place. This means that if you call .reverse() on an existing list, then the changes will reflect in the underlying list.

Keep in mind that while reversed() returns an iterator, the .reverse() method returns None. This behavior may be the source of subtle errors when you’re starting to use lists. Consider the following code:

>>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> reversed_digits = digits.reverse()
>>> reversed_digits is None
True
In this example, reversed_digits doesn’t get a list of reversed digits. Instead, it gets None because .reverse() mutates the underlying list in place and has no fruitful return value.

Finally, slicing is another technique that you can use to get a reversed copy of an existing list. To do this, you can use the following slicing operation:

>>> digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> digits[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
The [::-1] variation of the slicing operator does the magic in this code. With this operator, you create a reversed copy of the original list. But how does it work? The third index, step, is typically a positive number, which is why a normal slicing operation extracts the items from left to right.

By setting step to a negative number, such as -1, you tell the slicing operator to extract the items from right to left. That’s why you get a reversed copy of digits in the example above.


Remove ads
Sorting a List: sorted() and .sort()
When you need to sort a list of values without altering the original list, you can use the built-in sorted() function. This function takes an iterable of values and returns a list of sorted values:

>>> numbers = [2, 9, 5, 1, 6]

>>> sorted(numbers)
[1, 2, 5, 6, 9]

>>> numbers
[2, 9, 5, 1, 6]
When you pass a list to sorted(), you get a list of sorted values as a result. The function doesn’t alter the original data in your list.

Note: It’s important to note that sorted() returns a list rather than an iterator. This behavior differs from reversed(), which returns an iterator instead of a list.

As you can see in the above example, Python sorts numbers according to their specific values. When it comes to sorting strings, things can be a bit confusing. Consider the following example:

>>> words = ["Hello,", "World!", "I", "am", "a", "Pythonista!"]

>>> sorted(words)
['Hello,', 'I', 'Pythonista!', 'World!', 'a', 'am']
What? The sorted list isn’t in alphabetical order. Why? Python sorts strings character by character using each character’s Unicode code point. Because uppercase letters come before lowercase letters in Python’s default character set, UTF-8, you end up with "Hello" in the first position and "am" in the last.

Note: To dive deeper into sorting tools, check out How to Use sorted() and .sort() in Python.

You can use the built-in ord() function to get the Unicode code point of a character in Python:

>>> ord("H")
72
>>> ord("a")
97
As you can confirm in this code snippet, the uppercase "H" comes before the lowercase "a" in the Unicode table. That’s why you get "Hello" before "am" in the above example.

By default, the sorted() function sorts the items of a list in ascending order. If you need to sort the items in descending order, then you can use the reverse keyword-only argument. This argument defaults to False. If you set it to True, then you get the data in descending order:

>>> numbers = [2, 9, 5, 1, 6]

>>> sorted(numbers, reverse=True)
[9, 6, 5, 2, 1]
By setting the reverse argument to True, you tell sorted() to sort the input iterable in reverse order. Isn’t that neat?

Note: As you already learned, lists can store objects of different types. However, heterogeneous lists often don’t allow you to sort their content:

>>> numbers = [2, "9", 5, "1", 6]

>>> sorted(numbers)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
In practice, you won’t find heterogeneous lists in many use cases. Sequences of heterogeneous objects are like a database record with a few known and immutable fields. In those cases, using a tuple is a better way to go.

To illustrate how sorted() can help you in the real world, say that you want to calculate the median of a numeric dataset or sample. The median is the value that lies in the middle when you sort the data. In most cases, your data won’t be sorted, so sorting will be the first step. Then you just need to locate the value in the middle.

If the number of values in your dataset is even, then the median is the average of the two values in the middle. Here’s a Python function that allows you to compute the median of a sample of values:

>>> def median(samples):
...     n = len(samples)
...     middle_index = n // 2
...     sorted_samples = sorted(samples)
...     # Odd number of values
...     if n % 2:
...         return sorted_samples[middle_index]
...     # Even number of values
...     lower, upper = middle_index - 1, middle_index + 1
...     return sum(sorted_samples[lower:upper]) / 2
...

>>> median([3, 5, 1, 4, 2])
3

>>> median([3, 5, 1, 4, 2, 6])
3.5
Inside median(), you use sorted() to sort the samples in ascending order. Then you check if your list has an odd number of data points, in which case, you return the item in the middle directly. If the list has an even number of samples, then you compute the index of the two items in the middle, calculate their average, and return the resulting value.

The sorted() function also accepts another keyword-only argument called key. This argument allows you to specify a one-argument function that will extract a comparison key from each list item.

As an example of how to use key, say that you have a list of tuples where each tuple holds an employee’s data, including the employee’s name, age, position, and salary. Now imagine that you want to sort the employees by their age.

In that situation, you can do something like the following:

>>> employees = [
...     ("John", 30, "Designer", 75000),
...     ("Jane", 28, "Engineer", 60000),
...     ("Bob", 35, "Analyst", 50000),
...     ("Mary", 25, "Service", 40000),
...     ("Tom", 40, "Director", 90000)
... ]

>>> sorted(employees, key=lambda employee: employee[1])
[
    ('Mary', 25, 'Service', 40000),
    ('Jane', 28, 'Engineer', 60000),
    ('John', 30, 'Designer', 75000),
    ('Bob', 35, 'Analyst', 50000),
    ('Tom', 40, 'Director', 90000)
]
In this example, you pass a lambda function to the key argument. This lambda takes an employee tuple as an argument and returns the age value, which lives at index 1. Then sorted() uses this value to sort the tuples.

The key argument is quite useful in practice because it allows you to fine-tune the sorting process by changing the sorting criteria according to your specific needs.

If you need to sort a list in place instead of getting a new list of sorted data, then you can use the .sort() method. This method is similar to the sorted() function:

>>> numbers = [2, 9, 5, 1, 6]

>>> numbers.sort()
>>> numbers
[1, 2, 5, 6, 9]
The main difference between sorted() and .sort() is that the former returns a new list of sorted data, while the latter sorts the target list in place. Also, because .sort() is a method, you need to call it on a list object.

Like most list methods that run mutations, .sort() returns None. For example, in the code below, you run into a common mistake that can occur when working with lists:

>>> numbers = [2, 9, 5, 1, 6]

>>> sorted_numbers = numbers.sort()
>>> sorted_numbers is None
True
The .sort() method sorts the list in place and returns None to remind users that it operates by side effect. You must keep this behavior in mind because it can lead to subtle bugs.

You can also use the reverse and key keyword-only arguments with .sort(). They have the same meaning and functionality as the equivalent arguments in the sorted() function. Go ahead and give them a try!

Traversing Lists
When you’re working with lists in Python, one of the most common tasks that you’ll have to perform is to traverse the list while you run some transformation on the data or use the data for other purposes.

To traverse a list, you’ll need a loop that goes over each element from the start to the end of the list. Python provides several constructs that allow you to do this. The most popular are for loops and list comprehensions. You can also use some of Python’s functional programming tools for traversing lists.

In the following sections, you’ll learn how to traverse an existing list using these tools. To kick things off, you’ll start with for loops.

Using a for Loop to Iterate Over a List
The recommended way to iterate over a list is to use a for loop. This kind of loop is quite readable and straightforward in Python. Here’s how it goes:

>>> colors = [
...     "red",
...     "orange",
...     "yellow",
...     "green",
...     "blue",
...     "indigo",
...     "violet"
... ]

>>> for color in colors:
...     print(color)
...
red
orange
yellow
green
blue
indigo
violet
To use a for loop with a list, you place the list after the in keyword and provide a suitable loop variable. Don’t you think this loop is beautiful? Its meaning is clear, and it reads like plain English. That’s great!

Python’s for loops are intrinsically ready to operate on any iterable input directly. In this example, you’re using a list, but it’d work the same with a tuple, string, set, or any other iterable.

In the above example, the target iterable is your colors list. The loop variable, color, holds the current color in each iteration, and you can process each color in the loop’s body as needed. Note that if your list has a plural noun as its name, then the loop variable can use the same name in singular. This tiny detail will improve your loop’s readability.

A coding pattern that you’ll usually notice in code by people who come from other programming languages is that they tend to iterate over lists using a for loop that looks something like this:

>>> for i in range(len(colors)):
...     print(colors[i])
...
red
orange
yellow
green
blue
indigo
violet
This loop iterates over a range of integer numbers from 0 up to the length of the target list. In each iteration, you use the current index to access the associated item in the underlying list. Even though this loop works, it’s not Pythonic and is considered bad practice.

You don’t have to use a range of indices to iterate over a list in a for loop. Just go ahead and use your list directly in the loop definition. Python will take care of the rest.

Some people will argue that, in many situations, you’ll need to know the index of the current item to be able to perform some computations. That’s right! It’s especially true when you’re dealing with complex algorithms that operate on indices. In those cases, Python has you covered as well. It offers you the built-in enumerate() function, which you can use as in the following example:

>>> for i, color in enumerate(colors):
...     print(f"{i} is the index of '{color}'")
...
0 is the index of 'red'
1 is the index of 'orange'
2 is the index of 'yellow'
3 is the index of 'green'
4 is the index of 'blue'
5 is the index of 'indigo'
6 is the index of 'violet'
The enumerate() function takes an iterable and returns an iterator. This iterator yields two-item tuples on demand. Each tuple will contain an index and the associated item.

Note: The enumerate() function also takes a second argument called start, which is optional and defaults to 0. This argument allows you to specify a different starting point for the item count. However, if you set this argument to something different from 0, then the resulting values won’t match the items’ indices in the underlying list.

To learn more about enumerate(), check out Python enumerate(): Simplify Loops That Need Counters.

Python provides many other tools that you can use when you’re iterating through a list of values. For example, you can use reversed() to iterate over the list in reverse order:

>>> for color in reversed(colors):
...     print(color)
...
violet
indigo
blue
green
yellow
orange
red
In this loop, you take advantage of the reversed() function to traverse your list of colors in reverse order, which might be a common requirement in your code.

Another common need is to traverse the list in sorted order. In this situation, you can use your old friend sorted() as in the code below:

>>> numbers = [2, 9, 5, 1, 6]

>>> for number in sorted(numbers):
...     print(number)
...
1
2
5
6
9
The sorted() function allows you to get a new list of sorted data from your original list. Then you iterate over the new sorted list as usual.

If you continue digging into the Python tool kit, then you’ll find many other tools that will allow you to traverse your lists in different ways. For example, you’ll have the zip() function, which allows you to iterate over multiple lists in parallel:

>>> integers = [1, 2, 3]
>>> letters = ["a", "b", "c"]
>>> floats = [4.0, 5.0, 6.0]

>>> for i, l, f in zip(integers, letters, floats):
...     print(i, l, f)
...
1 a 4.0
2 b 5.0
3 c 6.0
In this example, you use zip() to iterate over three lists in parallel. The zip() function returns an iterator of tuples. The elements of each tuple come from the input iterables. In this example, the tuples combine items from integers, letters, and floats.

Note: For a deep dive into using the built-in zip() function, check out Using the Python zip() Function for Parallel Iteration.

Up to this point, all your list-traversing examples iterate over a list without performing any modification on the list itself. Modifying a list during iteration can lead to unexpected behavior and bugs, so avoid this practice. As a rule of thumb, if you need to modify the content of a list in a loop, then take a copy of that list first.

Say that you have a list of numbers, and you want to remove only odd values. In this situation, you can try something like this as your first attempt:

>>> numbers = [2, 9, 5, 1, 6]

>>> for number in numbers:
...     if number % 2:
...         numbers.remove(number)
...
>>> numbers
[2, 5, 6]
Unfortunately, only 9 and 1 were removed, while 5 remained in your list. This unexpected and incorrect behavior happened because removing items from a list shifts their indices, which interferes with the indices inside a running for loop. You can avoid this problem in a few ways.

For example, you can iterate over a copy of the original list:

>>> numbers = [2, 9, 5, 1, 6]

>>> for number in numbers[:]:
...     if number % 2:
...         numbers.remove(number)
...
>>> numbers
[2, 6]
This time, the result is correct. You use the [:] operator to create a shallow copy of your list. This copy allows you to iterate over the original data in a safe way. Once you have the copy, then you feed it into the for loop, as before.

Alternatively, you can iterate over the list in reverse order:

>>> numbers = [2, 9, 5, 1, 6]

>>> for number in reversed(numbers):
...     if number % 2:
...         numbers.remove(number)
...
>>> numbers
[2, 6]
When you remove only the last item from the right end of a list on each iteration, you change the list length, but the indexing remains unaffected. This lets you correctly map indices to the corresponding list elements.

Note that this was just an illustrative example that relied on cherry-picked data. Remember that calling .remove() deletes the first occurrence of the given value, starting from the left side of the list, instead of the last one. If you had duplicate values on the list, then list elements would be removed in a different order.

While modifying list elements during iteration is less of a problem than deleting them, it also isn’t considered a good practice. It’s usually more desirable to create a completely new list and populate it with the transformed values:

>>> numbers_as_strings = ["2", "9", "5", "1", "6"]

>>> numbers_as_integers = []
>>> for number in numbers_as_strings:
...     numbers_as_integers.append(int(number))
...

>>> numbers_as_integers
[2, 9, 5, 1, 6]
This example shows a pretty common pattern in Python. The pattern consists of creating an empty list and then populating it in a loop. You’ll find this pattern in several Python codebases all around. It provides an intuitive and readable way to populate a list from scratch. However, you’ll often find that you can replace this pattern with something even better, a list comprehension.

Building New Lists With Comprehensions
List comprehensions are another great, popular way to traverse your lists. Comprehensions are fundamentally a list transformation tool. They allow you to create lists with transformed data out of another list or iterable.

To understand how comprehensions can help you transform your lists, refer to the example where you have a list of numbers as strings and want to turn them into integers. You can solve this problem with the following comprehension:

>>> numbers = ["2", "9", "5", "1", "6"]

>>> numbers = [int(number) for number in numbers]
>>> numbers
[2, 9, 5, 1, 6]
This comprehension iterates over the values in your original list. The expression in the comprehension runs the conversion from string to integer. The final result is a new list object, which you assign back to the numbers variable.

Note that this comprehension is equivalent to a loop with the enumerate() function:

>>> numbers = ["2", "9", "5", "1", "6"]

>>> for i, number in enumerate(numbers):
...     numbers[i] = int(number)
...

>>> numbers
[2, 9, 5, 1, 6]
The loop is more verbose and complicated because you need to call enumerate() and declare an extra indexing variable, i. On the other hand, the loop modifies the original list in place, while the list comprehension creates a new list.

You can also use comprehensions to filter existing lists. For example, say that you have a list of integer values and want to create a new list containing only the even values out of your original list:

>>> integers = [20, 31, 52, 6, 17, 8, 42, 55]

>>> even_numbers = [number for number in integers if number % 2 == 0]
>>> even_numbers
[20, 52, 6, 8, 42]
The if clause in this list comprehension works as a filter that selects only the even numbers from your original data. How would you write a similar comprehension to retrieve the odd numbers?

Processing Lists With Functional Tools
You can also take advantage of some Python functional programming tools, such as map() and filter(), to traverse a list of values. These functions have an internal loop that iterates over the items of an input iterable and returns a given result.

For example, the map() function takes a transformation function and an iterable as arguments. Then it returns an iterator that yields items that result from applying the function to every item in the iterable.

Using map(), you can convert your list of numbers to integers with the following code:

>>> numbers = ["2", "9", "5", "1", "6"]

>>> numbers = list(map(int, numbers))
>>> numbers
[2, 9, 5, 1, 6]
In this example, map() applies int() to every item in numbers in a loop. Because map() returns an iterator, you’ve used the list() constructor to consume the iterator and show the result as a list.

Note: For a deeper dive into using the map() function, check out Python’s map(): Processing Iterables Without a Loop.

If you need to filter values from an existing list, then you can use the built-in filter() function. This function takes two arguments: a predicate function and an iterable of data. Then it returns an iterator that yields items that meet a given condition, which the predicate function tests for.

Here’s how filter() works in practice:

>>> integers = [20, 31, 52, 6, 17, 8, 42, 55]

>>> even_numbers = list(filter(lambda number: number % 2 == 0, integers))
>>> even_numbers
[20, 52, 6, 8, 42]
In this example, you use filter() to traverse your integers list and extract those values that satisfy the condition of being even numbers.

Note: For a deeper dive into using the filter() function, check out Python’s filter(): Extract Values From Iterables.

In Python, you’ll find a few other built-in and standard-library functions that allow you to traverse a list of values and obtain a final result either as another list, an iterator, or even a single value. Some examples include reduce(), min() and max(), sum(), all(), and any(). Note that some of these functions aren’t really functional programming tools, but they internally iterate over the input list.

Exploring Other Features of Lists
Python’s list has an impressive set of features, making it a versatile, flexible, and powerful data structure. So far, you’ve learned about most of these features. You’ve learned to create lists, add and remove items from your lists, traverse existing lists in a loop or comprehension, and much more.

In the following sections, you’ll learn about some additional features that make lists even more powerful. You’ll learn how to find items in a list, determine the minimum and maximum values, and get the list’s length. You’ll also explore the details of how Python compares lists to each other.

Finding Items in a List
Python has a few tools that allow you to search for values in an existing list. For example, if you only need to quickly determine whether a value is present in a list, but you don’t need to grab the value, then you can use the in or not in operator, which will run a membership test on your list.

Note: To learn more about the in and not in operators and how to perform membership tests, check out Python’s “in” and “not in” Operators: Check for Membership. These operators can be pretty useful when you need to check if a Python string contains a substring.

As its name suggests, a membership test is a Boolean test that allows you to find out whether an object is a member of a collection of values. The general syntax for membership tests on list objects looks something like this:

item in list_object

item not in list_object
The first expression allows you to determine if item is in list_object. It returns True if it finds item in list_object or False otherwise. The second expression works in the opposite way, allowing you to check if item is not in list_object. In this case, you get True if item doesn’t appear in list_object.

Here’s how membership tests work in practice:

>>> usernames = ["john", "jane", "bob", "david", "eve"]

>>> "linda" in usernames
False
>>> "linda" not in usernames
True

>>> "bob" in usernames
True
>>> "bob" not in usernames
False
In this example, you have a list of users and want to determine whether some specific users are registered in your system.

The first test uses in to check whether the user linda is registered. You get False because that user isn’t registered. The second test uses the not in operator, which returns True as a confirmation that linda isn’t one of your users.

The .index() method is another tool that you can use to find a given value in an existing list. This method traverses a list looking for a specified value. If the value is in the list, then the method returns its index. Otherwise, it raises a ValueError exception:

>>> usernames = ["john", "jane", "bob", "david", "eve"]

>>> usernames.index("eve")
4

>>> usernames.index("linda")
Traceback (most recent call last):
    ...
ValueError: 'linda' is not in list
In the first call to .index(), you get the index where you can find the user named "eve". You can use this index later in your code to access the actual object as needed. In the second call, because the user "linda" isn’t in the list, you get a ValueError with an explanatory message.

Note that if your search’s target value appears several times in the list, then .index() will return the index of the first occurrence:

>>> sample = [12, 11, 10, 50, 14, 12, 50]

>>> sample.index(12)
0
>>> sample.index(50)
3
The .index() method returns as soon as it finds the input value in the underlying list. So, if the value occurs many times, then .index() always returns the index of the first occurrence.

Lists provide yet another method that you can use for searching purposes. The method is called .count(), and it allows you to check how many times a given value is present in a list:

>>> sample = [12, 11, 10, 50, 14, 12, 50]

>>> sample.count(12)
2
>>> sample.count(11)
1
>>> sample.count(100)
0
The .count() method takes an item as an argument and returns the number of times the input item appears in the underlying list. If the item isn’t in the list, then you get 0.

Searching for a specific value in a Python list isn’t a cheap operation. The time complexity of .index(), .count(), and membership tests on lists is O(n). Such linear complexity may be okay if you don’t need to perform many lookups. However, it can negatively impact performance if you need to run many of these operations.

Getting the Length, Maximum, and Minimum of a List
While working with Python lists, you’ll face the need to obtain descriptive information about a given list. For example, you may want to know the number of items in the list, which is known as the list’s length. You may also want to determine the greatest and lowest values in the list. In all these cases, Python has you covered.

To determine the length of a list, you’ll use the built-in len() function. In the following example, you use this function as an intermediate step to calculate the average grade of a student:

>>> grades = [80, 97, 86, 100, 98, 82]
>>> n = len(grades)
>>> sum(grades) / n
90.5
Here, you calculate the average grade of a student. To do this, you use the sum() function to get the total sum and len() to get the number of evaluated subjects, which is the length of your grades list.

It’s important to note that because lists keep track of their length, calling len() is pretty fast, with a time complexity of O(1). So, in most cases, you don’t need to store the return value of len() in an intermediate variable as you did in the example above.

Note: To learn more about using the len() function, check out Using the len() Function in Python.

Another frequent task that you’ll perform on lists, especially on lists of numeric values, is to find the minimum and maximum values. To do this, you can take advantage of the built-in min() and max() functions:

>>> min([3, 5, 9, 1, -5])
-5

>>> max([3, 5, 9, 1, -5])
9
In these examples, you call min() and max() with a list of integer numbers. The call to min() returns the smallest number in the input list, -5. In contrast, the call to max() returns the largest number in the list, or 9.

Note: For a deeper dive into using the built-in min() and max() functions, check out Python’s min() and max(): Find Smallest and Largest Values.

Overall, Python lists support the len(), min(), and max() functions. With len(), you get the length of a list. With min() and max(), you get the smallest and largest values in a list. All these values can be fairly useful when you’re working with lists in your code.

Comparing Lists
You can also face the need to compare lists. Fortunately, list objects support the standard comparison operators. All these operators work by making item-by-item comparisons within the two involved lists:

>>> [2, 3] == [2, 3]
True
>>> [5, 6] != [5, 6]
False

>>> [5, 6, 7] < [7, 5, 6]
True
>>> [5, 6, 7] > [7, 5, 6]
False

>>> [4, 3, 2] <= [4, 3, 2]
True
>>> [4, 3, 2] >= [4, 3, 2]
True
In these examples, you compare different lists of numbers using the standard comparison operators. When comparing lists, Python runs an item-by-item comparison. So, for example, in the first expression above, Python compares 2 and 2, which are equal. Then it compares 3 and 3 to conclude that both lists are equal.

In the second expression, Python compares 5 and 5. They’re equal, so Python has to compare 6 and 6. They’re equal too, so the final result is False.

Note: In some situations, Python will run what’s known as short-circuiting evaluation. This type of evaluation occurs when Python can determine the truth value of a Boolean expression before evaluating all the parts involved:

>>> [5, 6] != [7, 6]
True
In this example, Python compares 5 and 7. They’re different, so Python returns True immediately without comparing 6 and 6 because it can already conclude that both lists are different. This behavior can make the code more efficient.

You can also compare lists of different lengths:

>>> [5, 6, 7] < [8]
True

>>> [5, 6, 7] == [5]
False
In the first expression, you get True as a result because 5 is less than 8. That fact is sufficient for Python to solve the evaluation. In the second example, you get False. This result makes sense because the lists don’t have the same length, so they can’t be equal.

As you can see, comparing lists can be tricky. It’s also an expensive operation that, in the worst case, requires traversing two entire lists. Things get more complex and expensive when you compare lists of strings. In this situation, Python will also have to compare the strings character by character, which adds cost to the operation.

Common Gotchas of Python Lists
If you’re new to Python and are starting with lists, then you’ll want to be on the lookout for a few gotchas that can cause subtle issues in your code. Up to this point, you’ve learned what you need in order to understand most of these gotchas, so here’s a summary of the most common ones:

Confusing aliases of a list with copies: This can cause issues because changes to one alias affect others. Take a look at the Aliases of a List section for practical examples of this issue.
Forgetting that most list methods mutate the list in place and return None rather than a new list: This commonly leads to issues when you assign the return value of a list method to a variable, thinking that you have a new list, but you really get None. Check out the Reversing and Sorting Lists section for practical examples of this gotcha.
Confusing .append() with .extend(): This can cause issues because .append() adds a single item to the end of the list, while the .extend() method unpacks and adds multiple items. Have a look at the Growing and Shrinking Lists Dynamically section for details on how these methods work.
Using an empty list as a default argument value in function definitions: This can lead to unexpected behaviors because default argument values get defined when Python first parses the function.
You already know the explanation of the first three bullet points in this list. So, you only have to dive deeper into the last point. Why should you avoid using an empty list—or a list in general—as a default argument value? To answer this question, consider the following toy function:

>>> def append_to(item, target=[]):
...     target.append(item)
...     return target
...
This function appends item to the end of target, which defaults to an empty list. At first glance, it may seem that consecutive calls to append_to() will return single-item lists like in the following hypothetical example:

>>> append_to(1)
[1]
>>> append_to(2)
[2]
>>> append_to(3)
[3]
But because Python defines the default argument value when it first parses the function and doesn’t overwrite it in every call, you’ll be working with the same list object in every call. Therefore, you don’t get the above behavior. Instead, you get the following:

>>> append_to(1)
[1]
>>> append_to(2)
[1, 2]
>>> append_to(3)
[1, 2, 3]
The target list remembers the data between calls. This happens because you’re using the same list object that appears as the default value in the function’s definition.

To prevent this issue, you can use None as the default value:

>>> def append_to(item, target=None):
...     if target is None:
...         target = []
...     target.append(item)
...     return target
...

>>> append_to(1)
[1]
>>> append_to(2)
[2]
>>> append_to(3)
[3]
Great! You’ve solved the issue. Now your function returns single-item lists as expected. That’s because the function doesn’t retain the state between calls.

Subclassing the Built-In list Class
Sometimes you may need to create a list-like class that either extends the features of list or customizes some of its standard behaviors. For a long time, it was impossible to inherit directly from built-in Python types implemented in C. Python 2.2 fixed this issue. Now you can subclass built-in types, including list.

To understand how to do this, say that you’re working on an application to process and report your students’ grades. You want to create a list-like object to store the grades. Your custom list should have a method that computes the average grade. In this situation, you can create a list subclass like the following:

>>> class GradeList(list):
...     def average(self):
...         return sum(self) / len(self)
...

>>> grades = GradeList([80, 97, 86, 100, 98])
>>> grades.append(82)
>>> grades.average()
90.5

>>> grades[0] = 95
>>> grades.average()
93.0
In this code snippet, you inherit from list directly. You can instantiate GradeList with an iterable of grade values. Note that the class works as a regular list. You can use list methods, such as .append() and .extend(), do indexing and slicing, and so on.

Additionally, you have a new .average() method in the class. This method isn’t part of the standard functionality of a list. So, this method extends list with new functionality.

The above example is a relatively safe way to subclass list because it doesn’t touch on any standard behavior. In contrast, things get a bit trickier when you need to customize the standard list behaviors.

For example, say that you want to continue improving your GradeList class, and you’re thinking of adding some input validation functionality. You want your class to validate any input grade to make sure it’s a number between 1 and 100.

In this situation, you need to make considerable changes to the standard functionality of list. You’ll need to modify all the methods that add new items to your lists. These methods include the following special methods:

.__init__(), which initializes all the class’s new instances.
.__setitem__(), which supports indexing operations.
You’ll also have to customize the .append(), .extend(), and .insert() methods. Furthermore, if you want your class to validate the input when you run concatenations, then you’ll have to update other special methods, including .__add__(), .__radd__(), and .__iadd__().

Here’s a possible, yet minimal, update of your GradeList class:

# grades.py

class GradeList(list):
    def __init__(self, grades):
        grades = [self._validate(grade) for grade in grades]
        super().__init__(grades)

    def __setitem__(self, index, grade):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            grades = [self._validate(grade) for grade in grade]
            return super().__setitem__(slice(start, stop, step), grades)
        super().__setitem__(index, self._validate(grade))

    def __add__(self, grades):
        grades = [self._validate(grade) for grade in grades]
        grades = super().__add__(grades)
        return self.__class__(grades)

    __radd__ = __add__

    def __iadd__(self, grades):
        grades = [self._validate(grade) for grade in grades]
        return super().__iadd__(grades)

    def append(self, grade):
        return super().append(self._validate(grade))

    def extend(self, grades):
        grades = [self._validate(grade) for grade in grades]
        return super().extend(grades)

    def average(self):
        return sum(self) / len(self)

    def _validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("grades must be numeric")
        if not (0 <= value <= 100):
            raise ValueError("grade must be between 0 and 100")
        return value
This class extends all the standard methods that add items to a regular list. All of these methods use the ._validate() helper method to guarantee that the input grades are valid. The method checks whether the values are numbers. It also checks if they’re between 0 and 100.

As you can conclude from the above code, modifying the standard behavior of a list in a subclass requires a lot of work, and it’s highly prone to errors.

Here are a few examples of how the above class works in practice:

>>> from grades import GradeList

>>> grades = GradeList([80, 97, 86, 200])
Traceback (most recent call last):
    ...
ValueError: grade must be between 0 and 100

>>> grades = GradeList([80, 97, 86, 100])
>>> grades.average()
90.75

>>> grades[0] = 955
Traceback (most recent call last):
    ...
ValueError: grade must be between 0 and 100

>>> grades[0] = 95
>>> grades
[95, 97, 86, 100]

>>> grades.append(-98)
Traceback (most recent call last):
    ...
ValueError: grade must be between 0 and 100

>>> grades.append(98)
>>> grades
[95, 97, 86, 100, 98]

>>> grades += [88, 100]
>>> grades
[95, 97, 86, 100, 98, 88, 100]

>>> grades[:3] = [100, 100, 100]
>>> grades
[100, 100, 100, 100, 98, 88, 100]

>>> grades.average()
98.0
Great! Your GradeList class works as expected. It raises an exception whenever you try to introduce an invalid grade using any of the regular operations that add items to an existing list.

Note: For a deeper dive into creating list-like classes, check out Custom Python Lists: Inheriting From list vs UserList.

Subclassing the built-in list class can be both useful and challenging. While you can extend a list with relatively little effort, customizing its standard behavior comes with important challenges, as you learned in this section. So, before making the decision to subclass list, consider whether other techniques, such as composition, might be a better solution.

Putting Lists Into Action
So far, you’ve learned a ton about Python lists, their features, and their functionalities. You’ve dived into how to create new lists, make copies of existing lists, add items to your lists, traverse existing lists in a loop or a similar tool, create custom list-like classes, and much more.

Now you have all the required knowledge about lists to effectively solve common practical Python coding problems with them. In the following sections, you’ll code a few examples to help you solidify your new knowledge and understand how to use lists in real life.

Removing Repeated Items From a List
Removing repeated items from an existing list is often a requirement in Python. You’ll probably manage to figure out several approaches to this problem. Using a set object could be one of them because sets don’t allow repeated items. So, you can do something like this:

>>> list(set([2, 4, 5, 2, 3, 5]))
[2, 3, 4, 5]
This solution works because you get a new list of unique values. However, Python sets don’t necessarily keep the contained items in order. So, you may want to use another technique that preserves the original insertion order.

Arguably, the safest way to tackle the problem of removing repeated items from a list is to create a new list with unique values out of the original list. You can do this in a function like the following:

>>> def get_unique_items(list_object):
...     result = []
...     for item in list_object:
...         if item not in result:
...             result.append(item)
...     return result
...

>>> get_unique_items([2, 4, 5, 2, 3, 5])
[2, 4, 5, 3]
In this function, you accept a list as an argument. Then you define a new empty list to store the function’s result. In the loop, you iterate over the items in the input list. The conditional checks if the current item is absent in result. If that’s the case, then you add the item using .append(). Once the loop has finished, you return the resulting list, which will contain unique values.

Note that using the not in operator on larger lists can be too slow due to its linear time complexity. If that’s the case, then you may want to introduce an additional helper variable to hold copies of the unique values in a Python set:

>>> def get_unique_items(list_object):
...     result = []
...     unique_items = set()
...     for item in list_object:
...         if item not in unique_items:
...             result.append(item)
...             unique_items.add(item)
...     return result
...

>>> len(get_unique_items(range(100_000)))
100000
You use the set to quickly determine if the given value is already present. Sets implement the in and not in operators differently, making them much faster than their list counterparts. While this functions returns instantaneously, it requires twice as much memory because you’re now storing every value in two places.

Creating Multidimensional Lists
Creating a multidimensional list, such as a matrix or a list of lists, might also be a common requirement in your code. Again, you can tackle this problem in many different ways, depending on your specific needs.

A quick and safe way to create a multidimensional list is using a for loop or a comprehension. For example, say that you want to create a five-by-five matrix of numeric values, and you want to initialize all the values to 0. You can do something like this:

>>> matrix = []
>>> for row in range(5):
...     matrix.append([])
...     for _ in range(5):
...         matrix[row].append(0)
...

>>> matrix
[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
In this example, you first create an empty list to store your matrix. Then you start a for loop that will run five times. In each iteration, you add a new empty list. So, your matrix will have five rows. Next, you start a nested loop that runs five times too.

Each time, you add a 0 to the current row using .append(). As a result, you get a five-by-five matrix with all its values initialized to 0.

Note: In Python, you commonly use an underscore (_) as a placeholder variable when the syntax requires a variable, but your code doesn’t.

You can get the same result as in the example above with a list comprehension like the following:

>>> [[0 for _ in range(5)] for _ in range(5)]
[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
In this example, you use a list comprehension whose expression is another list comprehension. The inner comprehension provides the nested lists, while the outer comprehension builds the matrix.

You can make the above comprehension even more concise and readable by taking advantage of the repetition operator (*) as in the following code:

>>> [[0] * 5 for _ in range(5)]
[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
This new version of your list comprehension is way more readable than the previous one. It takes advantage of the repetition operator to build the rows of your matrix. This example might it seem like the following would work:

>>> [[0] * 5] * 5
[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
This output looks like what you need. It’s a list containing five nested lists. However, this resulting matrix internally works pretty differently from all the previous solutions. If you change one value in a given row, then the change will reflect in all the other rows:

>>> matrix = [[0] * 5] * 5
>>> matrix
[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

>>> matrix[0][0] = 1
>>> matrix
[
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
]
In this example, you try to change the value of the first item in the first nested list or row. However, you actually changed the first value in all the rows. When you pass a list as an argument to the repetition operator, you get aliases of the list instead of copies. So, all the rows in your matrix are actually the same list.

Flattening Multidimensional Lists
Sometimes, you may need to process data that comes as a list of nested lists. Flattening this data into a one-dimensional list may be a common requirement in those scenarios. By flattening a list, you convert a multidimensional list, such as a matrix, into a one-dimensional list.

Note: To dive deeper into how to flatten a list of lists, check out How to Flatten a List of Lists in Python.

For example, suppose that you have the following list of lists:

[[0, 1, 2], [10, 11, 12], [20, 21, 22]]
Processing this list may be annoying because of its nested structure. So you need to flatten the list and get the following list instead:

[0, 1, 2, 10, 11, 12, 20, 21, 22]
How would you do this in Python? You’ll find several solutions to this problem for sure. In the code snippet below, you have one of them:

>>> matrix = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]

>>> flattened_list = []
>>> for row in matrix:
...     flattened_list.extend(row)
...

>>> flattened_list
[0, 1, 2, 10, 11, 12, 20, 21, 22]
In the for loop above, you iterate over the nested lists in matrix. Then you use the .extend() method to add the current sublist’s contents to flattened_list as independent items. This loop produces a flattened list as a result.

Splitting Lists Into Chunks
Another useful list-related skill is to split an existing list into a certain number of chunks. This skill comes in handy when you need to distribute the workload across multiple threads or processes for concurrent processing.

Note: For a complete walk-through of splitting a list or iterable into chunks, check out How to Split a Python List or Iterable Into Chunks.

Again, you’ll find multiple solutions to this problem. The code below shows just one of them. Note that you won’t be using any standard-library or third-party specialized tool. You’ll code the solution based on your knowledge about lists:

>>> def split_list(list_object, chunk_size):
...     chunks = []
...     for start in range(0, len(list_object), chunk_size):
...         stop = start + chunk_size
...         chunks.append(list_object[start:stop])
...     return chunks
...

>>> split_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
In this function, you take the list to split and the number of items in every resulting chunk. Then you define a new empty list to store the chunks. The for loop iterates over a range of indices that goes from 0 to the length of your input list. Every iteration jumps through the desired chunk size.

To extract the chunks, you use a slicing operation. The loop variable, start, defines the start index, while the stop variable provides the stop index. Then you append every chunk to your chunks list, and that’s it.

Using a List as a Stack or Queue
You can use a Python list to emulate a stack or queue data structure. The .append() and .pop() methods will help you in that task. For example, to mimic a stack, or last-in-first-out (LIFO) data structure, you can use .append() to push an item onto the top of the stack. Similarly, you can use .pop() with no arguments to pop items from the top of the stack:

>>> stack = []

>>> stack.append("Copy")
>>> stack.append("Paste")
>>> stack.append("Remove")
>>> stack
['Copy', 'Paste', 'Remove']

>>> stack.pop()
'Remove'
>>> stack.pop()
'Paste'
>>> stack.pop()
'Copy'
>>> stack
[]
In this example, you represent a stack using a list. The stack will hold actions that you can undo. You start by creating an empty list called stack. Then you push hypothetical actions onto the stack using .append(), which adds the actions to the right end of the list.

The .pop() method returns the actions so that you can redo them. This method also removes the actions from the right end of the list following the LIFO order that distinguishes a stack data structure.

Note: For a deep dive into what stacks are and how to create them in Python, check out How to Implement a Python Stack.

Alternatively, if you want to emulate a queue, or a first-in-first-out (FIFO) data structure, then you can use .append() to place items at the end of the list, which is known as an enqueue operation. Similarly, you can use .pop() with 0 as an argument to return and remove items from the left end of the queue, which is known as a dequeue:

>>> queue = []

>>> queue.append("John")
>>> queue.append("Jane")
>>> queue.append("Linda")
>>> queue
['John', 'Jane', 'Linda']
>>> queue.pop(0)
'John'
>>> queue.pop(0)
'Jane'
>>> queue.pop(0)
'Linda'
This list simulates a queue of people who may be arriving at a place to get some service. The .append() method allows you to add people to the end of the queue as they arrive. The .pop() method with 0 as an argument allows you to process people from the beginning of the queue when it’s their turn to access the service. Overall, you’re following the FIFO principle that rules queues.

Note: Check out Python Stacks, Queues, and Priority Queues in Practice for a complete walk-through of stacks and queues in Python.

By using a Python list, you can quickly take advantage of the standard list functionality to provide basic stack and queue operations, such as push, pop, enqueue, and dequeue. However, keep in mind that even though lists can help you simulate stacks and queues, they aren’t optimized for these use cases. Using a list as a queue is especially bad because it can make the queue terribly slow.

Deciding Whether to Use Lists
As you’ve learned throughout this tutorial, lists are powerful, flexible, versatile, and full-featured data structures. Because of their characteristics, people tend to use and abuse them. Yes, they’re suitable for many use cases, but sometimes they aren’t the best available option.

In general, you should use lists when you need to:

Keep your data ordered: Lists maintain the order of insertion of their items.
Store a sequence of values: Lists are a great choice when you need to store a sequence of related values.
Mutate your data: Lists are mutable data types that support multiple mutations.
Access random values by index: Lists allow quick and easy access to elements based on their index.
In contrast, avoid using lists when you need to:

Store immutable data: In this case, you should use a tuple. They’re immutable and more memory efficient.
Represent database records: In this case, consider using a tuple or a data class.
Store unique and unordered values: In this scenario, consider using a set or dictionary. Sets don’t allow duplicated values, and dictionaries can’t hold duplicated keys.
Run many membership tests where item doesn’t matter: In this case, consider using a set. Sets are optimized for this type of operation.
Run advanced array and matrix operations: In these situations, consider using NumPy’s specialized data structures.
Manipulate your data as a stack or queue: In those cases, consider using deque from the collections module or Queue, LifoQueue, or PriorityQueue. These data types are thread-safe and optimized for fast inserting and removing on both ends.
Depending on your specific scenario, lists may or may not be the right tool for the job. Therefore, you must carefully evaluate your needs and consider advanced data structures like the ones listed above.

Conclusion
Now you have a deep, solid understanding of the core features and functionalities of Python lists. Lists are everywhere. They’re an important part of the language itself and are present in the standard library, third-party packages, and in just about every piece of Python code that you’ll find out there. So, learning about them is a fundamental skill that you must have under your belt.

In this tutorial, you’ve learned how to:

Create new lists in Python using different approaches
Access one or more items in an existing list
Copy, update, grow, shrink, and concatenate existing Python lists
Sort, reverse, and traverse existing lists using built-in functions and methods
Use some other features of lists
With all this knowledge, you’re ready to write better, more effective code by taking advantage of Python lists. You’re also empowered to make informed decisions about when to use lists in your code.

