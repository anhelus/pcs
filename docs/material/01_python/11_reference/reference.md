# Passaggio per reference

Dopo aver guadagnato un po' di familiarità con Python, potremmo notare dei casi nei quali le nostre funzioni non modificano degli argometni come atteso. Specialmente se veniamo d aaltri linguaggi, vedremo che alcuni di questi gestiscono gli argometni di una funzione come dei riferimenti a variabili esistenti, il che è conosciuto come *passaggio per riferimento*. Altri linguaggi, invece, trattano le due variabili come valori indipendenti, un approccio conosciuto come passaggio per valore.

In questa lezione, vedremo:

* cosa significa passare per reference, e perché dovremmo volerlo fare;
* come il passaggio per refrence differisce sia dal passaggio per valore, sia dall'approccio unico di Python;
* come si comportano i funciton arguments in Python
* come possiamo usare certi tipi mutabili per effettuare il passaggio per reference in Python
* quali sono le best practice per replicare il passaggio per reference in Python

## Cosa è il passaggio per reference?

Prima di addentrarci nei dettagli tecnici del passaggio per reference, può esserci d'aiuto dare uno sguardo ravvicinato al termine stesso "rompendolo" in più componenti:

* *passaggio* significa fornire un arogmento ad una funzione;
* *reference* indca che l'argomento che stiamo passando alla funzione è un riferimento ad una variabile che esiste già in memoria, e non una copia indipendente di quella stessa variabile.

Dal momento che stiamo dando alla funzione un riferimento ad una variabile esistente, tutte le operazioni effettuate su questo riferimento influenzeranno direttamente la variabile a cui si riferisce.

Vediamo alcuni esempi di come questo funziona nella pratica.

Vediamo come passare una variabile per reference in C#. NOtiamo l'uso della parola chiave ref nelle righe evidenziate:

```csharp
using System;

// Source:
// https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/passing-parameters
class Program
{
    static void Main(string[] args)
    {
        int arg;

        // Passing by reference.
        // The value of arg in Main is changed.
        arg = 4;
        squareRef(ref arg);
        Console.WriteLine(arg);
        // Output: 16
    }

    static void squareRef(ref int refParameter)
    {
        refParameter *= refParameter;
    }
}
```

Come possiamo vedere, il `refParameter` di `squareRef()` deve essere dichiarato usando la parola chaive `ref`, e dobbiamo anche usare la parola chiave quando chiamiamo la funzione. Quindi, l'argomento sarà passato per reference, e potrà essere modificato in place.

Python non ha una parola chiave `ref`, o un suo equivalente. SE provassimo a replicare l'esempio precedente in Python, avremmo risultati differenti:

```py
>>> def main():
...     arg = 4
...     square(arg)
...     print(arg)
...
>>> def square(n):
...     n *= n
...
>>> main()
4
```

In questo caso, la variabile `arg` non viene alterata in place. Sembra che Python tratti l'argomento passato come valore singolo piuttosto che una reference ad una variabile esistente. Questo singifica che Python passa gli argomenti per valore piuttosto che per reference?

Non proprio. Python passa gli argomenti né per reference né per valore, ma per *assegnazione* (*assignment*). Vedremo a breve rapidamente i dettalgi del passaggio per valore e per reference prima di guardare più da vicino l'approccio di Python. Dopo questo, vedremo alcune delle best practice epr ottenere l'equivalente del passaggiuo per reference in Python.

## passaggio per valore vs. passaggio per reference

Quando passiamo degli argomenti di una funzione per reference, questi argomenti sono riferiti soltanto a valori già esistenti. Di contro, quando passaimo gli argomenti per valore, questi diventano copie indipendenti dei valori originari.

Torniamo brevemente all'esempio in C#, questa volta togliendo la parola chiave `ref`. Questo farà sì che il programma usi il comportamento di default, ovvero il passaggio per valore:

```csharp
using System;

// Source:
// https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/passing-parameters
class Program
{
    static void Main(string[] args)
    {
        int arg;

        // Passing by value.
        // The value of arg in Main is not changed.
        arg = 4;
        squareVal(arg);
        Console.WriteLine(arg);
        // Output: 4
    }

    static void squareVal(int valParameter)
    {
        valParameter *= valParameter;
    }
}
```

Qui, possiamo vedere che `squareVal()` non modifica la variabile originaria. Piuttosto, `valParameter` è una copia indipendente della variabile originaria `arg`. Anche se questo combacia con il comportamento che vedremmo in Python, ricordiamo che Python non passa esattamente per valore. Proviamo ciò.

La funzione integrata `id()` di Python restituisce un intero che rappresenta l'indirizzo di memoria dell'oggetto desiderato. Usando `id()`, possiamo verificare che:

* gli argomenti della funzione si riferiscono inizialmente allo stesso indirizzo delle loro variabili originarie
* riassegnare l'argomento nella funzione gli dà un nuovo indirizzo, mentre la variabile originaria rimane immutata

Nell'esempio successivo, notiamo che l'idnirizzo di `x` combacia inizialmente con quello di `n`, ma cambia dopo la riassegnazione, mentre l'indirizzo di `n` non cambia:

```py
>>> def main():
...     n = 9001
...     print(f"Initial address of n: {id(n)}")
...     increment(n)
...     print(f"  Final address of n: {id(n)}")
...
>>> def increment(x):
...     print(f"Initial address of x: {id(x)}")
...     x += 1
...     print(f"  Final address of x: {id(x)}")
...
>>> main()
Initial address of n: 140562586057840
Initial address of x: 140562586057840
  Final address of x: 140562586057968
  Final address of n: 140562586057840
```

Il fatto che l'indirizzo iniziale di `n` ed `x` siano gli stessi quando invochiamo `increment()` prova che l'argomento `x` non sta venendo passato per valore. Altrimetni, `n` ed `x` avrebbero avuto indirizzi di memoria distinti.

Prima di apprendere i dettagli di come Python gestisce gli argomenti, vediamo alcuni casi d'uso pratici del passaggio per reference.

## Utilizzare dei costrutti di passaggio per referecne

Passare variabili per reference è una delle tante strategie che possiamo usare per implementare determianti pattern di programmazione. Anche se non è sempre necessario, il passaggio per reference può comunque essere utile.

In questa sezione, vedremo tre dei pattern più comuni per i quali il passaggio per reference è un approccio pratico. Vedremo quindi come implementare ciascuno di questi pattern in Python.

## Evitare oggetti duplicati

Come abbiamo visto, passare una variabile per valore casuerà la creazione e memorizzazione di una copia di quel valore, Nei linguaggi in cui il comportamento di default è il passaggio per valore, potremmo avere dei benefici in termini di performance nel passaggio per reference, specialmente qunado la variabile ha molti dati. Questo sarà abbastanza evidente quando il codice gira su macchine con risorse limitate.

In Python, tuttavia, questo non è mai un problema. Veddemo il perché nella sezione successiva.

## Restiture valori multipli

Una delle applicazioni più comuni del passaggio per reference è creare auna funzione che alteri il valore dei parametri di riferimento restituendo un valore distinto. Possiamo modificare l'esempio del passaggio per reference in C# per illustrare questa tecnica:

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        int counter = 0;

        // Passing by reference.
        // The value of counter in Main is changed.
        Console.WriteLine(greet("Alice", ref counter));
        Console.WriteLine("Counter is {0}", counter);
        Console.WriteLine(greet("Bob", ref counter));
        Console.WriteLine("Counter is {0}", counter);
        // Output:
        // Hi, Alice!
        // Counter is 1
        // Hi, Bob!
        // Counter is 2
    }

    static string greet(string name, ref int counter)
    {
        string greeting = "Hi, " + name + "!";
        counter++;
        return greeting;
    }
}
```

Nell'esempio precedente, `greet()` restituisce una stringa di benvenuto e modifica contestualmente il valore del contatore. Ora, proviamo a riprodurre questo quanto più possibile in Python:

```py
>>> def main():
...     counter = 0
...     print(greet("Alice", counter))
...     print(f"Counter is {counter}")
...     print(greet("Bob", counter))
...     print(f"Counter is {counter}")
...
>>> def greet(name, counter):
...     counter += 1
...     return f"Hi, {name}!"
...
>>> main()
Hi, Alice!
Counter is 0
Hi, Bob!
Counter is 0
```

Counter non viene incrementato nell'esempio precedente perché, come abbiamo appreso in precedenza, Python non ha modo di passare i valori per reference. Quindi, come possiamo ottenere lo stesso risultato ottenuto in C#?

In pratica, i parametri passati per riferimento in C# permettono alla funzione non solo di restituire un valore, ma anche di operare su parametri aggiuntivi. QUesto equivale a restituire valori multipli.

Fortunatamente, Python supporta già la restituzione di valori multipli. In senso stretto, una funzione Python che restituisce valori multipli restituisce in effetti una tupla che contiene ogni valore.

```py
>>> def multiple_return():
...     return 1, 2
...
>>> t = multiple_return()
>>> t  # A tuple
(1, 2)

>>> # You can unpack the tuple into two variables:
>>> x, y = multiple_return()
>>> x
1
>>> y
2
```

Come possiamo vedere, per restiturie valori multipli, possiamo semplicemente usare la parola chiave `return`seguita da valori separati da virgole, o variabili.

Grazie a questa tecnica, posisamo modificare l'istruzione di ritorno in `greet()` dal codice Python precedente per restituire sia un messaggio di benvenuto sia un contatore:

```py
>>> def main():
...     counter = 0
...     print(greet("Alice", counter))
...     print(f"Counter is {counter}")
...     print(greet("Bob", counter))
...     print(f"Counter is {counter}")
...
>>> def greet(name, counter):
...     return f"Hi, {name}!", counter + 1
...
>>> main()
('Hi, Alice!', 1)
Counter is 0
('Hi, Bob!', 1)
Counter is 0
```

Tuttavia, questo ancora non sembra giusto. Anche se adesso `greet()` restituisce più valori, questi stanno venendo stampati come una tupla, il che non è nostra intenzione. Inoltre, la variabile contatore originaria rimane a 0.

Per pulire il nostro output ed ottenere i risutlati desiderati, dobbiamo reassegnare la variabile `counter` con ogni chiamata a `greet()`.

```py
>>> def main():
...     counter = 0
...     greeting, counter = greet("Alice", counter)
...     print(f"{greeting}\nCounter is {counter}")
...     greeting, counter = greet("Bob", counter)
...     print(f"{greeting}\nCounter is {counter}")
...
>>> def greet(name, counter):
...     return f"Hi, {name}!", counter + 1
...
>>> main()
Hi, Alice!
Counter is 1
Hi, Bob!
Counter is 2
```

Ora, dopo aver riassegnato ogni variabile con una chiamata a `greet()`, potremo vedere i risultati desiderati.

Assegnare i valori di ritorno alle variabili è il miglior modo di ottenere gli stessi risultati del passaggio per reference in Python. Vedremo il perché, tra le altre cose, nella sezione sulle best pracitce.

## Creazione di funzioni condizionali con più valori di ritorno

Questo è un caso d'uso specifico di restituire più valori nel quale la funzione può essere usata in un'istruzione condizionale ed ha dei side effect aggiuntivi, come modificare una variabile esterna passata come argomento.

Consideriamo la funzione standard `Int32.TryParse` in C#, che restituisce un valore booleano edmopera su una reference ad un argomento intero allo stesso tempo:

```csharp
public static bool TryParse (string s, out int result);
```

Questa funzione prova a convertire una stringa in un intero a 32 bit cons egno usando la parola chiave `out`. Ci sono due possibili risultati:

* se il parsing ha successo, il parametro di output sarà impostato all'intero risultatnte, e la funzione restituirà `true`
* se il parsing fallisce, allora il parmaetro di output sarà impostato a `0`, e la funzione restituirà falso

Possiamo vedere questo nella pratica nel seguente esempio, che prova a convertire un certo numero di stringhe differenti:

```csharp
using System;

// Source:
// https://docs.microsoft.com/en-us/dotnet/api/system.int32.tryparse?view=netcore-3.1#System_Int32_TryParse_System_String_System_Int32__
public class Example {
    public static void Main() {
        String[] values = { null, "160519", "9432.0", "16,667",
                            "   -322   ", "+4302", "(100);", "01FA" };
        foreach (var value in values) {
            int number;

            if (Int32.TryParse(value, out number)) {
                Console.WriteLine("Converted '{0}' to {1}.", value, number);
            }
            else {
                Console.WriteLine("Attempted conversion of '{0}' failed.",
                                   value ?? "<null>");
            }
        }
    }
}
```

Il codice precedente, che prova a convertrire delle stringhe formattate differentemente in interi mediante `TryParse()`, manda in output il seguente:

```sh
Attempted conversion of '<null>' failed.
Converted '160519' to 160519.
Attempted conversion of '9432.0' failed.
Attempted conversion of '16,667' failed.
Converted '   -322   ' to -322.
Converted '+4302' to 4302.
Attempted conversion of '(100);' failed.
Attempted conversion of '01FA' failed.
```

Per implementare una funzione simile in Python, possiamo usare molteplici valori di ritorno come visto in precedenza:

```py
def tryparse(string, base=10):
    try:
        return True, int(string, base=base)
    except ValueError:
        return False, None
```

Questa funzione `tryparse()` restituisce due valori. Il primo valore indica se la conversione ha avuto successo, ed il secondo contiene il risultato (o `None`, in caso di fallimento).

Tuttavia, l'uso di questa funzione è un po' CLUNKY, perché dobbiamo spacchettare il valore di ritorno ad ogni chiamata. Questo significa che non possiamo usare la funzione all'interno di un'istruzione if:

```py
>>> success, result = tryparse("123")
>>> success
True
>>> result
123

>>> # We can make the check work
>>> # by accessing the first element of the returned tuple,
>>> # but there's no way to reassign the second element to `result`:
>>> if tryparse("456")[0]:
...     print(result)
...
123
```

Anche se in linea generale questo funziona restituendo più valori, `tryparse()` non può essere usato in un check condizionale. Questo significa che abbiamo dell'ulteriore lavoro da fare.

Possiamo sfruttare la flessibilità di Python e semplificare la funzione per restituire un singolo valore di diversi tipi a seconda del fatto che la conversione abbia successo:

```py
def tryparse(string, base=10):
    try:
        return int(string, base=base)
    except ValueError:
        return None
```

Grazie al fatto che le funzioni Python possono restituire diversi tipi di dato, possiamo usare questa funzione all'interno di un'istruzione condizionale. Ma come? Non dovremmo chiamare per prima la funzione, assegnare il suo valore di ritorno, e quindi controllare il valore stesso?

Sfruttando la flessibilità di Python sui tipi degli oggetti, così come le nuove espressioni di assegnazione in Python 3.8, possiamo chiamare questa funzione semplificata all'interno di un'istruzione if ed ottenere il valore di ritorno se il controllo passa:

```py
>>> if (n := tryparse("123")) is not None:
...     print(n)
...
123
>>> if (n := tryparse("abc")) is None:
...     print(n)
...
None

>>> # You can even do arithmetic!
>>> 10 * tryparse("10")
100

>>> # All the functionality of int() is available:
>>> 10 * tryparse("0a", base=16)
100

>>> # You can also embed the check within the arithmetic expression!
>>> 10 * (n if (n := tryparse("123")) is not None else 1)
1230
>>> 10 * (n if (n := tryparse("abc")) is not None else 1)
10
```

Notiamo che questa versione di `tryparse()` risulta essere anche più potente della versione C#, permettendoci di suarla all'interno di istruzioni condizionali ed in espressioni aritmetiche.

Con un po' di ingenuità, abbiamo replicato un pattern specifico ed utile di passaggio per reference senza passare gli argomenti per reference. Infatti, dobbiamo di nuovo assegnare i valori di ritorno quando usiamo l'operatore di assegnazione (:=) ed usando il valore di ritorno direttamente nelle espressioni Python.

Finora, abbiamo appreso quello che significa passaggio per reference, come differisce dal passaggio per valore, e come l'approccio di Python differisca da entrambi. Ora siamo pronti a dare un'occhiata ravvicinata a come Python gestisce gli argomenti di una funzione.

## Passare gli argomenti in Python

Python passa gli argomenti per assegnazione. Ciò significa che quando chiamiamo una funzione Python, ogni argomento diventa una variabile alla quale viene assegnato il valore passato.

Quindi, possiamo apprendere dettagli importanti su come Python gestisce gli argomenti della funzione comprendendo come il meccanismo di assegnazione stesso funziona, anche al di fuori delle funzioni.

## Comprendere l'assegnazione in Python

La documentazione di Python per le istruzioni di assegnazione fornisce i seguenti dettagli:

* se l'obiettivo dell'assegnazione è un identificatore, o il nome di una variabile, questo nome è collegato all'oggetto. Per esempio, in `x = 2`, `x` è il nome e `2` è l'oggetto.
* se il nome è già collegato ad un oggetto separato, viene quindi ri-collegato al nuovo oggetto. Ad esempio, se `x` è già `2` ed abbiamo scritto `x = 3`, allora il nome della variabile `x` viene ri-assegnato a `3`.

Tutti gli oggetti Python sono implementati secondo una certa struttura. UNa delle proprietà di qeusta struttura è un contatore che tiene traccia di qunati nomi sono stati collegati a questo oggetto.

!!!note "Nota"
    Questo contatore è chiamato *reference counter* perché tiene traccia di quante reference, o nomi, puntano allo stesso oggetto. Non confondiamo il reference counter con il concetto di passaggio per reference, in quanto i due sono incorrelati.

La documentazione Python fornisce ulteriori dettagli sui reference counts.

Rimaniamo all'esempio `x = 2` ed esaminiamo quello che accade quando assegnamo un valore ad una nuova varibile:

* se un oggetto rappresentativo del valore `2` esiste già, viene recuperato. Altrimenti, è creato.
* il reference counter di questo oggetto viene incrementato
* un'entrata è aggiunta nell'attuale namespace per collegare l'identificatore `x` all'oggetto che rappresenta `2`. Questa entrata è nei fatti una coppia chiave-valore memorizzata in un dizionario. Una rappresentazione di questo dizionario è restituita da `locals()` o `globals()`.

Ecco quello chea ccade se riassegnamo `x` ad un diverso valore:

* il reference counter dell'oggetto rappresentante `2` viene decrementato
* il reference counter dell'oggetto che rappresenta il nuovo valore è incrementato
* il dizionario per l'attuale namespace è aggiornato per correlare `x` all'oggetto rappresentante il nuovo valore

Python ci permette di ottenre il reference counter per valori arbitrari con la funzione `sys.getrefcount()`. Possiamo usarla per illustrare come l'assegnazione incemenrta e decrementa questi reference counter. Notiamo che l'interprete interattivo sfrutta il comportamento che darà risultati differenti, per cui dovremo eseguire il seguente codice da un file:

```py
from sys import getrefcount

print("--- Before  assignment ---")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")
x = "value_1"
print("--- After   assignment ---")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")
x = "value_2"
print("--- After reassignment ---")
print(f"References to value_1: {getrefcount('value_1')}")
print(f"References to value_2: {getrefcount('value_2')}")
```

Questo script mostrerà il conteggio delle reference per ogni valore prima dell'assegnazione, dopo l'assegnazione, e dopo la riassegnazione:

```sh
--- Before  assignment ---
References to value_1: 3
References to value_2: 3
--- After   assignment ---
References to value_1: 4
References to value_2: 3
--- After reassignment ---
References to value_1: 3
References to value_2: 4
```

Questi risultai illustrano la relazione tra gli identificatori (nomi delle variabili) e gli oggetti Python che rapprentano valori distinti. Quando assegnamo più variabili allo stesso valore, Python aumenta il reference counter per l'oggetto esistente ed aggiorna il namespace attuale piuttosto che creare oggetti duplicati in memroia.

Vediamo adesso di esplorare come Python gestisce gli argomenti di una funzione.

## Esplorazione degli argomenti di una funzione

Gli argomenti di una funzione in Python sono variabili locali. Cosa significa? Quello locale è uno degli ambiti definiti in Python (ed in ogni linguaggio di programmazione). Questi ambiti sono rappresentati dai namespace dictionary menizioanti nella sezione precedente. Possiamo usare `locals()` e `globals()` per recuperare i namespace dictionary locali e globali, rispettivamnete.

All'esecuzione, ogni funzione ha il suo proprio namespace locale:

```py
>>> def show_locals():
...     my_local = True
...     print(locals())
...
>>> show_locals()
{'my_local': True}
```

Usando `locals()`, possiamo dimostrare che gli argomenti della funzione diventano variabili regolai nel namespace locale della funzione. Aggiungiamo un argomento, `my_arg`, alla funzione:

```py
>>> def show_locals(my_arg):
...     my_local = True
...     print(locals())
...
>>> show_locals("arg_value")
{'my_arg': 'arg_value', 'my_local': True}
```

Possiamo anche usare `sys.getrefcount()` per mostrare come gli argomenti di funzioni aumentano il conteggio delle reference per un oggetto:

```py
>>> from sys import getrefcount

>>> def show_refcount(my_arg):
...     return getrefcount(my_arg)
...
>>> getrefcount("my_value")
3
>>> show_refcount("my_value")
5
```

Lo script precedente scrive il conteggio delle reference per `my_value` per prima cosa all'esterno, poi all'interno di `show_refcount()`, mostrando un aumento del reference count non di uno, ma di due!

Questo perché, oltre a `show_refcount()` stesso, la chiamata a `sys.getrefcount()` all'interno di `show_refcount()` riceve anche `my_arg` come argomento. Questo piazza `my_arg` nel namespace locale per `sys.getrefcount()`, aggiungendo una reference extra a `my_value`.



By examining namespaces and reference counts inside functions, you can see that function arguments work exactly like assignments: Python creates bindings in the function’s local namespace between identifiers and Python objects that represent argument values. Each of these bindings increments the object’s reference counter.

Now you can see how Python passes arguments by assignment!


Remove ads
Replicating Pass by Reference With Python
Having examined namespaces in the previous section, you may be asking why global hasn’t been mentioned as one way to modify variables as if they were passed by reference:

>>> def square():
...     # Not recommended!
...     global n
...     n *= n
...
>>> n = 4
>>> square()
>>> n
16
Using the global statement generally takes away from the clarity of your code. It can create a number of issues, including the following:

Free variables, seemingly unrelated to anything
Functions without explicit arguments for said variables
Functions that can’t be used generically with other variables or arguments since they rely on a single global variable
Lack of thread safety when using global variables
Contrast the previous example with the following, which explicitly returns a value:

>>> def square(n):
...     return n * n
...
>>> square(4)
16
Much better! You avoid all potential issues with global variables, and by requiring an argument, you make your function clearer.

Despite being neither a pass-by-reference language nor a pass-by-value language, Python suffers no shortcomings in that regard. Its flexibility more than meets the challenge.

Best Practice: Return and Reassign
You’ve already touched on returning values from the function and reassigning them to a variable. For functions that operate on a single value, returning the value is much clearer than using a reference. Furthermore, since Python already uses pointers behind the scenes, there would be no additional performance benefits even if it were able to pass arguments by reference.

Aim to write single-purpose functions that return one value, then (re)assign that value to variables, as in the following example:

def square(n):
    # Accept an argument, return a value.
    return n * n

x = 4
...
# Later, reassign the return value:
x = square(x)
Returning and assigning values also makes your intention explicit and your code easier to understand and test.

For functions that operate on multiple values, you’ve already seen that Python is capable of returning a tuple of values. You even surpassed the elegance of Int32.TryParse() in C# thanks to Python’s flexibility!

If you need to operate on multiple values, then you can write single-purpose functions that return multiple values, then (re)assign those values to variables. Here’s an example:

def greet(name, counter):
    # Return multiple values
    return f"Hi, {name}!", counter + 1

counter = 0
...
# Later, reassign each return value by unpacking.
greeting, counter = greet("Alice", counter)
When calling a function that returns multiple values, you can assign multiple variables at the same time.

Best Practice: Use Object Attributes
Object attributes have their own place in Python’s assignment strategy. Python’s language reference for assignment statements states that if the target is an object’s attribute that supports assignment, then the object will be asked to perform the assignment on that attribute. If you pass the object as an argument to a function, then its attributes can be modified in place.

Write functions that accept objects with attributes, then operate directly on those attributes, as in the following example:

>>> # For the purpose of this example, let's use SimpleNamespace.
>>> from types import SimpleNamespace

>>> # SimpleNamespace allows us to set arbitrary attributes.
>>> # It is an explicit, handy replacement for "class X: pass".
>>> ns = SimpleNamespace()

>>> # Define a function to operate on an object's attribute.
>>> def square(instance):
...     instance.n *= instance.n
...
>>> ns.n = 4
>>> square(ns)
>>> ns.n
16
Note that square() needs to be written to operate directly on an attribute, which will be modified without the need to reassign a return value.

It’s worth repeating that you should make sure the attribute supports assignment! Here’s the same example with namedtuple, whose attributes are read-only:

>>> from collections import namedtuple
>>> NS = namedtuple("NS", "n")
>>> def square(instance):
...     instance.n *= instance.n
...
>>> ns = NS(4)
>>> ns.n
4
>>> square(ns)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in square
AttributeError: can't set attribute
Attempts to modify attributes that don’t allow modification result in an AttributeError.

Additionally, you should be mindful of class attributes. They will remain unchanged, and an instance attribute will be created and modified:

>>> class NS:
...     n = 4
...
>>> ns = NS()
>>> def square(instance):
...     instance.n *= instance.n
...
>>> ns.n
4
>>> square(ns)
>>> # Instance attribute is modified.
>>> ns.n
16
>>> # Class attribute remains unchanged.
>>> NS.n
4
Since class attributes remain unchanged when modified through a class instance, you’ll need to remember to reference the instance attribute.


Remove ads
Best Practice: Use Dictionaries and Lists
Dictionaries in Python are a different object type than all other built-in types. They’re referred to as mapping types. Python’s documentation on mapping types provides some insight into the term:

A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary. (Source)

This tutorial doesn’t cover how to implement a custom mapping type, but you can replicate pass by reference using the humble dictionary. Here’s an example using a function that operates directly on dictionary elements:

>>> # Dictionaries are mapping types.
>>> mt = {"n": 4}
>>> # Define a function to operate on a key:
>>> def square(num_dict):
...     num_dict["n"] *= num_dict["n"]
...
>>> square(mt)
>>> mt
{'n': 16}
Since you’re reassigning a value to a dictionary key, operating on dictionary elements is still a form of assignment. With dictionaries, you get the added practicality of accessing the modified value through the same dictionary object.

While lists aren’t mapping types, you can use them in a similar way to dictionaries because of two important characteristics: subscriptability and mutability. These characteristics are worthy of a little more explanation, but let’s first take a look at best practices for mimicking pass by reference using Python lists.

To replicate pass by reference using lists, write a function that operates directly on list elements:

>>> # Lists are both subscriptable and mutable.
>>> sm = [4]
>>> # Define a function to operate on an index:
>>> def square(num_list):
...     num_list[0] *= num_list[0]
...
>>> square(sm)
>>> sm
[16]
Since you’re reassigning a value to an element within the list, operating on list elements is still a form of assignment. Similar to dictionaries, lists allow you to access the modified value through the same list object.

Now let’s explore subscriptability. An object is subscriptable when a subset of its structure can be accessed by index positions:

>>> subscriptable = [0, 1, 2]  # A list
>>> subscriptable[0]
0
>>> subscriptable = (0, 1, 2)  # A tuple
>>> subscriptable[0]
0
>>> subscriptable = "012"  # A string
>>> subscriptable[0]
'0'
>>> not_subscriptable = {0, 1, 2}  # A set
>>> not_subscriptable[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
Lists, tuples, and strings are subscriptable, but sets are not. Attempting to access an element of an object that isn’t subscriptable will raise a TypeError.

Mutability is a broader topic requiring additional exploration and documentation reference. To keep things short, an object is mutable if its structure can be changed in place rather than requiring reassignment:

>>> mutable = [0, 1, 2]  # A list
>>> mutable[0] = "x"
>>> mutable
['x', 1, 2]

>>> not_mutable = (0, 1, 2)  # A tuple
>>> not_mutable[0] = "x"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> not_mutable = "012"  # A string
>>> not_mutable[0] = "x"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> mutable = {0, 1, 2}  # A set
>>> mutable.remove(0)
>>> mutable.add("x")
>>> mutable
{1, 2, 'x'}
Lists and sets are mutable, as are dictionaries and other mapping types. Strings and tuples are not mutable. Attempting to modify an element of an immutable object will raise a TypeError.

Conclusion
Python works differently from languages that support passing arguments by reference or by value. Function arguments become local variables assigned to each value that was passed to the function. But this doesn’t prevent you from achieving the same results you’d expect when passing arguments by reference in other languages.

In this tutorial, you learned:

How Python handles assigning values to variables
How function arguments are passed by assignment in Python
Why returning values is a best practice for replicating pass by reference
How to use attributes, dictionaries, and lists as alternative best practices
You also learned some additional best practices for replicating pass-by-reference constructs in Python. You can use this knowledge to implement patterns that have traditionally required support for passing by reference.

To continue your Python journey, I encourage you to dive deeper into some of the related topics that you’ve encountered here, such as mutability, assignment expressions, and Python namespaces and scope.

Stay curious, and see you next time!