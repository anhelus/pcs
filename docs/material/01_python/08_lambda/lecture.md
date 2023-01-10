# 1.8 - Calcolo lambda in Python

Python ed altri linguaggi come Java, C#, ed anche C++, hanno avuto avuto delle funzioni lambda aggiunte alla loro sintassi, mentre linguaggi come LISP o F# usano le lambda come concetto core.

Le lambda in Python sono delle piccole funzioni anonime, soggette ad una sintassi più restrittiva, ma concisa, rispetto alle funzioni regolari Python.

!!!note "Nota"
    Alcuni degli esempi di codice che utilizzano le lambda function potrebbe sembrare ignorino le best practice in temrini di stile di Python. Tuttavia, in questo caso, servono ad illustrare i concetti alla base delle funzioni lambda in Python, e saranno comujnque messi a confronto con alternative migliori nel codice.

## Calcolo lambda

Le espressioni lambda in Python ed in altri linguaggi di programmazione affondano le loro radici nel calcolo lambda, un modello computazionale inventato da Alonzo Church.

Alonzo Church formalizzò il calcolo lambda, un linguaggio basato puramente sull'astrazione, negli anni '30. Le funzioni lambda sono anche riferite originariamente come *astrazioni lambda*, un riferimento diretto al modello astratto creato originariamente da Church.

Il calcolo lambda può codificare una qualsiasi elaborazione. E' Turing-completo ma, contrariamente al concetto di macchina di Turing, è puro e non mantiene alcuno stato.

I linguaggi funzionali affondano le loro origini nella logica matematica e nel calcolo lambda, mentre i linguaggi di programmazione imperativi abbracciano il modello computazionale basato sullo stato ed inventato da ALan Turing. I due modelli di calcolo, il calcolo lambda e le macchine di Turing, possono essere tradotto l'uno nell'altro. Questa equivalenza è consocitua come *ipotesi di Church-Turing*.

I linguaggi funzionali ereditano direttamente la filosofia del calcolo lambda, adottando un approccio di programmazione dichiarativo che enfasizza l'astrazione, la trasformazione dei dati, la composizione, e la purezza (nessuno stato o side effect). Esempi di linguaggi funzionali sono Lisp o Erlang.

In contrasto, la macchian di Turing ha condotto alla programmazione imperativa che è possibile osservare in linguaggi come Fortran, C, o Python.

Lo stile imperativo consiste nella programmazione con istruzioni, conducendo il flusso del programma passo dopo passo con istruzioni dettagliate. QUesto approccio promuove il mutamento, e richiede la gestione dello stato.

La separazione tra le famiglie in realtà presenta alcuni punti in comune: alcuni linguaggi incorporano feature imperative, mentre ci sono delle feature funzionali che permeano la famiglia dei linguaggi imperativi, in particoalre con l'introduzione delle funzioni lambda in linguaggi come Java o Python.

Python non è intrinsecamente un linguaggio funzionale, ma ha adottato alcuni concetti funzionali abbastanza presto: infatti, gli operatori map(), filter() e reduce() vennero aggiunti al linguaggio già nel gennaio del 1994.

## Primo esempio

Ecco alcuni esempi per darci un'idea per qualche codice Python in puro stile funzionale.

La funzione identità, una funzione che restituisce il suo argomento, è espresso con una funzione standard Python definita come segue:

```py
def identity(x):
    return x
```

`identity()` prende come argomento `x`, e lo restituisce quando invocato.

In contrasto, se usiamo la costruzione lambda Python, otteniamo il seguente:

```py
lambda x: x
```

Nell'esempio precedente, l'espressione è composta di:

* la parola chiave `lambda`
* una variable `x`, che rappresenta l'argomento per la funzione lambda
* un corpo, anche in questo caso `x`, che segue l'operatore `:`

La variabile `x` è defintia come dipendente, a differenza di una variabile indpendente la quale non è vincolata e può essere referenziata nel corpo dell'espressione. UNa variabile libera può essere una costante o una variabile definita nell'ambito della funzione. 

Possiamo scrivere un esempio leggermente più elabroato, una funzione che aggiunge `1` ad un argomento, come segue:

```py
lambda x: x + 1
```

Possiamo applicare la funzione precedente ad un argomento circondando la funzione ed il suo argomento con delle parentesi:

```sh
>>> (lambda x: x + 1)(2)
3
```

Quello della *riduzione* è un approccio del calcolo lambda per calcolare il valore di un'espressione. Nell'esempio attuale, consiste nel rimpiazzare la variabile dipendente `x` con l'argomento `2`:

```
(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3
```

Dato che una funzione lambda è un'espressione, può avere un nome. QUindi possiamo scrivere il codice precedente come segue:

```sh
>>> add_one = lambda x: x + 1
>>> add_one(2)
3
```

La precedente funzione lambda è equivalente a scrivere questo:

```py
def add_one(x):
    return x + 1
```

Queste funzioni prendono un singolo argomento. Potremmo aver notato che, nella definizione delle lambda, gli argomenti non soino circondatri da parentesi. Le funzioni multi-argomento (funzioni che accettano più di un argomento) sono espresse nelle lambda Python elencando gli argomenti e separandoli con una virgola (,) ma senza circondarli da delle parentesi:

```py
>>> scrivi_nome_cognome = lambda nome, cognome: f'{nome.title()} {cognome.title()}'
>>> scrivi_nome_cognome('guido', 'van rossum')
Guido Van Rossum
```

La funzione almbda assegnata a `scrivi_nome_cognome` prende due argomenti e restituisce una stringa che interpola i due parametri `nome` e `cognome`. Come atteso, la definizione della lambda elenca gli argomenti senza parentesi, laddove la chiamata alla funzione è fatta esattamente come una funzione Python normale, con parentesi che circondano gli argomenti.

### Funzioni anonime

I seguenti termini possono essere usati in maniera intercambiabile a seconda del tipo di linguaggio di programmazione: *funzioni anonime*, *funzioni lambda*, *espressioni lambda*, *astrazioni lambda*, e via dicendo.

Prese letteralmente, una funzione anonima è una funzione senza un nome. In Python, una funzione anonima viene creata mediante la parola chiave `lambda`. Blandamente, può o meno avere un nome. Considerando una funzione anonima a due argomenti definita con la lambda ma non vincolata ad una variabile. La lambda non ha un nome:

```py
>>> lambda x, y: x + y
```

La funzione precedente definisce un'espressione lambda che rpende due argomenti e restituisce la loro somma.

Oltre chje fornirci il feedback che Python è perfettamente ok con questa forma, non ha alcun uso pratico. Possiamo invocare la funzione nell'interprete Python:

```sh
>>> _(1, 2)
3
```

L'esempio precedente sfrutta la feature interattiva dell'interprete mediante l'underscore. Tuttavia, non possiamo scrivere del codice simile in un modulo Python: qui, dovremmo assegnare un nome alla lambda, o passare la lambda ad una funzione. Vedremo in seguito come fare.

!!!note "Nota"
    In una sessione interattiva con l'interprete Python, il singolo underscore è collegato all'ultima espressione valutata. Nell'esempio precedente, quindi, il `_` putna alla funzione lambda.

Un altro pattern usato in altri linguaggi come JavaScript è quello di usare immediatamente una funzione lambda Python. Questo è conosciuto come *Immediately Invoked Function Expression* (*IIFE*). Ecco un esempio

```py
>>> (lambda x, y: x + y)(2, 3)
5
```

La funzione lambda precedente è definita e quindi chiuamata immediatamente con due argomenti, ovvero 2 e 3. Restituisce il valore 5, che è la somma degli argomenti.

# lambda e higher order functions

Le funzioni lambda sono di frequente usate con le higher-order functions, che prendono una o più funzioni come argomenti e restituiscono una o più funzioni.

Una funzione lambda può essere una higher-order function prendendo una funzione (normale o lambda) come argomento, come nell'esempio successivo.

```py
>>> high_ord_func = lambda x, func: x + func(x)
>>> high_ord_func(2, lambda x: x * x)
6
>>> high_ord_func(2, lambda x: x + 3)
7
```

Python espone le higher-order function come funzioni built-in, o nella libreria standard. Esempi includono map(), filter(), reduce(), così come funzioni chiave come sort(), sorted(), min(), e max(). 

## Lambda e funzioni regolari

A differenza delle forme lambda in altri linguaggi, dove aggiungono nuove funzionalità, le lambda Python sono solo una notazione abbrievata se siamo troppo pigri per definire una funzione.

Nonostante questo, non dobbiamo fare in modo che questa definizione ci faccia desistere dall'usare le lambda function in Python. Di primo acchitto, potremmo accettare che una funzione lambda sia una funzione che ci permetta semplicemente di ridurre il codice necessario a definire o invocare una funzione. Vedremo però a breve che ci sono delle sottili differenze tra le normali funzioni Python e le funzioni lambda.

### Funzioni

A questo punto, potremmo chiederci cosa distingue fondamentalmente una funzione lambda vincolata ad una variabile da una regolare funzione con una singola riga di ritorno: sotto il cofano, praticamente niente. Verifichaimo èperò come Python vede una funzione costruita con una singola istruzione di ritorno rispettoa d una funzione costrrita come un'espressione lambda.

Il modulo dis espone delle funzioni per analizzare il bytecode Python generato dal compilatore.

```py
>>> import dis
>>> add = lambda x, y: x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function <lambda> at 0x7f30c6ce9ea0>
```

Possiamo vedere che `dis()` mostra una versione leggibile del bytecode Python, permettendo l'ispezione delle istruzioni a basso livello che l'interprete Pythjon usa mentre esegue il programma.

Ora vediamo una funzione classica:

```py
>>> import dis
>>> def add(x, y): return x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function add at 0x7f30c6ce9f28>
```

Il bytecode interpretato da Python è lo stesso per entrambe le funzioni. Tuttavia, possiamo notare che il nome è differente: il nome della funzione è add per la funzione definita mediante def, mentre la funzione lambda Python è vista come lambda.

### traceback

ABbiamo visto che, nel contesto della funzione lambda, Python non ha fornito il nome della funzione, ma solo <lambda>. Questa può essere una limitazione da considerare quando vi è un'eccezione, ed un traceback mostra soltanto <lambda>: 

```py
>>> div_zero = lambda x: x / 0
>>> div_zero(2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <lambda>
ZeroDivisionError: division by zero
```

Ecco la stessa eccezione lanciata da una funzione normale:

```py
>>> def div_zero(x): return x / 0
>>> div_zero(2)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in div_zero
ZeroDivisionError: division by zero
```

La funzione normale causa un errore simile, ma risulta in un traceback più preceiso, perché dà il nome della funzione (`div_zero`).

### Sintassi

Come abbiamo visto nelle sezioni precedente, una funzione lambda presenta delle distinzioni sintattiche da una funzione normale. In particolare, una funzione lambda ha le seguenti caratteristiche:

* può contenre soltanto espressioni e non include istruzioni nel suo corpo;
* è scritta come una singola riga di esecuzione;
* non supporta il type hinting;
* può essere invocata immedaitamente.

#### Nessuna istruzione

Una funzione lambda non può contenere alcuna istruzione. In una funzione lambda, le istruizoni come return, pass, assert o raise lanceranno un'eccezione SyntaxError. Ecco un esempio dell'aggiunta di assert al corpo di una lambda:

```py
>>> (lambda x: assert x == 2)(2)
  File "<input>", line 1
    (lambda x: assert x == 2)(2)
                    ^
SyntaxError: invalid syntax
```

Questo conciso esempio intendeva asserire che il parametro `x` ha un valore pari a 2. Tuttavia, l'interprete identifica un SyntaxError mentre effettua il parsing del codice che coinvolge l'assert nel corpo della lambda.

#### Singola espressione

Invece di una funzione normale, una funzione lambda Python è una singola espressione. Tuttavia, nel corpo di una lambda, possiamo suddividere l'espressione in varie righe usando parentesi o stringhe multilinea; ciònonostante, rimane una singola espressione:

```py
>>> (lambda x:
... (x % 2 and 'odd' or 'even'))(3)
'odd'
```

L'esempio precedente restituisce la stringa `odd` quando l'argomento della lambda è dispari, e pari quando l'argomento è pari. E' suddivisa tra due linee perché è contenuta in un insieme di parentesi, ma rimane una singola espressione.

#### Type hinting

Se abbiamo iniziato ad adottare il type hiunting, abbiamo un'altra ragione per preferire le funzioni normali alle lambda function Python. In una funzione lambda, infatti, questa espressione non ha equivalenti:

```py
def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'
```

Un qualsiasi errore di tipo può essere catturato da strumetni come mypy o pyre, ed un SyntaxError con l'equivalente funzione lamb da viuene lanciato a runtime:

```py
>>> lambda first: str, last: str: first.title() + " " + last.title() -> str
  File "<stdin>", line 1
    lambda first: str, last: str: first.title() + " " + last.title() -> str

SyntaxError: invalid syntax
```

In pratica, provare ad inserire del type hinting risulta immedaitamente in un SyntaxError a runtime.

### IIFE

Abbiamo già visto degli esempi di IIFE:

```py
>>> (lambda x: x * x)(3)
9
```

Al di furoi dell'interprete Pyuthon, questa feature non viene praticamente usata in pratica. E' infatti una conseguenza diretta del fatto che la funzione lambda è chiamabile come viene definita. Per esempio, questo ci permette di apssare la definizione di una funzione lambda Python ad una higher-order function come map(), filter o reduec().

## Argomenti

Come una normale funzione definita mediante def, le espressioni lambda in Python supportano tutti i diversi modi per passare degli argomenti, come argomenti posizionali, args e kwargs.

Vediamo un esempio:

```py
>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
6
```

### Decorators

In Python, un decorator è l'implemnentazione di un pattern che permette di aggiungere un dato comportamento ad una funzione o classe. Viene normalmente anteponendo una sintassi del tipo @nome_decorator alla funzione. Ecco un esempio:

```py
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")
```

Nell'esempio precedente, some_decorator() è una funzione che aggiunge un dato comporrtamento alla funzione decorated_fucntion(), in modo che chiamare decorated_fucntion('Python') restituisce il seguente output:

```py
Calling function 'decorated_function'
With argument 'Python'
```

In pratica, decorated_function() manda a schermo soltanto "With argument 'Python'", ma il decorator aggiunge un ulteriorie comportamento che permette anche di mostrare a schermo "Calling function 'decorated_function'".

Un decorator può essere applicato ad una funzione lambda. Anche se non è possibile decorare una funzione lambda con la sintassi @decorator, dato che il decorator è semplicemente una funzione, questo può chiamare  una funzione lambda:

```py
# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
```

La funzione `add_two()`, decorata con `@trace` alla riga 11, viene invocata con l'argomento 3 alla riga 15. Di contro, alla riga 18, una funzione lambda viene immediatamente integrata in una chiamata a trace(), il decorator. Eseguendo il codice precedente, otteniamo il seguente output:

```sh
[TRACE] func: add_two, args: (3,), kwargs: {}
[TRACE] func: <lambda>, args: (3,), kwargs: {}
9
```

Vediamo che il nome della funzione lambda appare come `<lambda>`, mentre `add_two` viene chiaramente identificato come una funzione normale.

Decorare la funzione lambda in questo modo può essere utile a scopo di debugging, specialmente per analizzare il comportamento di una funzione almbda usata nel contesto di una higher-order function. Vediamo un esempio con `map()`:

```py
list(map(trace(lambda x: x*2), range(3)))
```

The first argument of map() is a lambda that multiplies its argument by 2. This lambda is decorated with trace(). When executed, the example above outputs the following:

[TRACE] Calling <lambda> with args (0,) and kwargs {}
[TRACE] Calling <lambda> with args (1,) and kwargs {}
[TRACE] Calling <lambda> with args (2,) and kwargs {}
[0, 2, 4]
The result [0, 2, 4] is a list obtained from multiplying each element of range(3). For now, consider range(3) equivalent to the list [0, 1, 2].

You will be exposed to map() in more details in Map.

A lambda can also be a decorator, but it’s not recommended. If you find yourself needing to do this, consult PEP 8, Programming Recommendations.

For more on Python decorators, check out Primer on Python Decorators.


Remove ads
Closure
A closure is a function where every free variable, everything except parameters, used in that function is bound to a specific value defined in the enclosing scope of that function. In effect, closures define the environment in which they run, and so can be called from anywhere.

The concepts of lambdas and closures are not necessarily related, although lambda functions can be closures in the same way that normal functions can also be closures. Some languages have special constructs for closure or lambda (for example, Groovy with an anonymous block of code as Closure object), or a lambda expression (for example, Java Lambda expression with a limited option for closure).

Here’s a closure constructed with a normal Python function:

def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
outer_func() returns inner_func(), a nested function that computes the sum of three arguments:

x is passed as an argument to outer_func().
y is a variable local to outer_func().
z is an argument passed to inner_func().
To test the behavior of outer_func() and inner_func(), outer_func() is invoked three times in a for loop that prints the following:

x = 0, y = 4, z = 5
closure(5) = 9
x = 1, y = 4, z = 6
closure(6) = 11
x = 2, y = 4, z = 7
closure(7) = 13
On line 9 of the code, inner_func() returned by the invocation of outer_func() is bound to the name closure. On line 5, inner_func() captures x and y because it has access to its embedding environment, such that upon invocation of the closure, it is able to operate on the two free variables x and y.

Similarly, a lambda can also be a closure. Here’s the same example with a Python lambda function:

def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
When you execute the code above, you obtain the following output:

closure(5) = 9
closure(6) = 11
closure(7) = 13
On line 6, outer_func() returns a lambda and assigns it to to the variable closure. On line 3, the body of the lambda function references x and y. The variable y is available at definition time, whereas x is defined at runtime when outer_func() is invoked.

In this situation, both the normal function and the lambda behave similarly. In the next section, you’ll see a situation where the behavior of a lambda can be deceptive due to its evaluation time (definition time vs runtime).

Evaluation Time
In some situations involving loops, the behavior of a Python lambda function as a closure may be counterintuitive. It requires understanding when free variables are bound in the context of a lambda. The following examples demonstrate the difference when using a regular function vs using a Python lambda.

Test the scenario first using a regular function:

>>> def wrap(n):
...     def f():
...         print(n)
...     return f
...
>>> numbers = 'one', 'two', 'three'
>>> funcs = []
>>> for n in numbers:
...     funcs.append(wrap(n))
...
>>> for f in funcs:
...     f()
...
one
two
three
In a normal function, n is evaluated at definition time, on line 9, when the function is added to the list: funcs.append(wrap(n)).

Now, with the implementation of the same logic with a lambda function, observe the unexpected behavior:

>>> numbers = 'one', 'two', 'three'
>>> funcs = []
>>> for n in numbers:
...     funcs.append(lambda: print(n))
...
>>> for f in funcs:
...     f()
...
three
three
three
The unexpected result occurs because the free variable n, as implemented, is bound at the execution time of the lambda expression. The Python lambda function on line 4 is a closure that captures n, a free variable bound at runtime. At runtime, while invoking the function f on line 7, the value of n is three.

To overcome this issue, you can assign the free variable at definition time as follows:

>>> numbers = 'one', 'two', 'three'
>>> funcs = []
>>> for n in numbers:
...     funcs.append(lambda n=n: print(n))
...
>>> for f in funcs:
...     f()
...
one
two
three
A Python lambda function behaves like a normal function in regard to arguments. Therefore, a lambda parameter can be initialized with a default value: the parameter n takes the outer n as a default value. The Python lambda function could have been written as lambda x=n: print(x) and have the same result.

The Python lambda function is invoked without any argument on line 7, and it uses the default value n set at definition time.


Remove ads
Testing Lambdas
Python lambdas can be tested similarly to regular functions. It’s possible to use both unittest and doctest.

unittest

The unittest module handles Python lambda functions similarly to regular functions:

import unittest

addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # Should fail
        self.assertEqual(addtwo(3), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
LambdaTest defines a test case with three test methods, each of them exercising a test scenario for addtwo() implemented as a lambda function. The execution of the Python file lambda_unittest.py that contains LambdaTest produces the following:

$ python lambda_unittest.py
test_add_three (__main__.LambdaTest) ... FAIL
test_add_two (__main__.LambdaTest) ... ok
test_add_two_point_two (__main__.LambdaTest) ... ok

======================================================================
FAIL: test_add_three (__main__.LambdaTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "lambda_unittest.py", line 18, in test_add_three
    self.assertEqual(addtwo(3), 6)
AssertionError: 5 != 6

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
As expected, we have two successful test cases and one failure for test_add_three: the result is 5, but the expected result was 6. This failure is due to an intentional mistake in the test case. Changing the expected result from 6 to 5 will satisfy all the tests for LambdaTest.

doctest

The doctest module extracts interactive Python code from docstring to execute tests. Although the syntax of Python lambda functions does not support a typical docstring, it is possible to assign a string to the __doc__ element of a named lambda:

addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3) # Should fail
    6
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
The doctest in the doc comment of lambda addtwo() describes the same test cases as in the previous section.

When you execute the tests via doctest.testmod(), you get the following:

$ python lambda_doctest.py
Trying:
    addtwo(2)
Expecting:
    4
ok
Trying:
    addtwo(2.2)
Expecting:
    4.2
ok
Trying:
    addtwo(3) # Should fail
Expecting:
    6
**********************************************************************
File "lambda_doctest.py", line 16, in __main__.addtwo
Failed example:
    addtwo(3) # Should fail
Expected:
    6
Got:
    5
1 items had no tests:
    __main__
**********************************************************************
1 items had failures:
   1 of   3 in __main__.addtwo
3 tests in 2 items.
2 passed and 1 failed.
***Test Failed*** 1 failures.
The failed test results from the same failure explained in the execution of the unit tests in the previous section.

You can add a docstring to a Python lambda via an assignment to __doc__ to document a lambda function. Although possible, the Python syntax better accommodates docstring for normal functions than lambda functions.

For a comprehensive overview of unit testing in Python, you may want to refer to Getting Started With Testing in Python.

Lambda Expression Abuses
Several examples in this article, if written in the context of professional Python code, would qualify as abuses.

If you find yourself trying to overcome something that a lambda expression does not support, this is probably a sign that a normal function would be better suited. The docstring for a lambda expression in the previous section is a good example. Attempting to overcome the fact that a Python lambda function does not support statements is another red flag.

The next sections illustrate a few examples of lambda usages that should be avoided. Those examples might be situations where, in the context of Python lambda, the code exhibits the following pattern:

It doesn’t follow the Python style guide (PEP 8)
It’s cumbersome and difficult to read.
It’s unnecessarily clever at the cost of difficult readability.

Remove ads
Raising an Exception
Trying to raise an exception in a Python lambda should make you think twice. There are some clever ways to do so, but even something like the following is better to avoid:

>>> def throw(ex): raise ex
>>> (lambda: throw(Exception('Something bad happened')))()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 1, in <lambda>
    File "<stdin>", line 1, in throw
Exception: Something bad happened
Because a statement is not syntactically correct in a Python lambda body, the workaround in the example above consists of abstracting the statement call with a dedicated function throw(). Using this type of workaround should be avoided. If you encounter this type of code, you should consider refactoring the code to use a regular function.

Cryptic Style
As in any programming languages, you will find Python code that can be difficult to read because of the style used. Lambda functions, due to their conciseness, can be conducive to writing code that is difficult to read.

The following lambda example contains several bad style choices:

>>> (lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
The underscore (_) refers to a variable that you don’t need to refer to explicitly. But in this example, three _ refer to different variables. An initial upgrade to this lambda code could be to name the variables:

>>> (lambda some_list: list(map(lambda n: n // 2,
                                some_list)))([1,2,3,4,5,6,7,8,9,10])
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
Admittedly, it’s still difficult to read. By still taking advantage of a lambda, a regular function would go a long way to render this code more readable, spreading the logic over a few lines and function calls:

>>> def div_items(some_list):
      div_by_two = lambda n: n // 2
      return map(div_by_two, some_list)
>>> list(div_items([1,2,3,4,5,6,7,8,9,10])))
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
This is still not optimal but shows you a possible path to make code, and Python lambda functions in particular, more readable. In Alternatives to Lambdas, you’ll learn to replace map() and lambda with list comprehensions or generator expressions. This will drastically improve the readability of the code.

Python Classes
You can but should not write class methods as Python lambda functions. The following example is perfectly legal Python code but exhibits unconventional Python code relying on lambda. For example, instead of implementing __str__ as a regular function, it uses a lambda. Similarly, brand and year are properties also implemented with lambda functions, instead of regular functions or decorators:

class Car:
    """Car with methods as lambda functions."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))

    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value))

    __str__ = lambda self: f'{self.brand} {self.year}'  # 1: error E731

    honk = lambda self: print('Honk!')     # 2: error E731
Running a tool like flake8, a style guide enforcement tool, will display the following errors for __str__ and honk:

E731 do not assign a lambda expression, use a def
Although flake8 doesn’t point out an issue for the usage of the Python lambda functions in the properties, they are difficult to read and prone to error because of the usage of multiple strings like '_brand' and '_year'.

Proper implementation of __str__ would be expected to be as follows:

def __str__(self):
    return f'{self.brand} {self.year}'
brand would be written as follows:

@property
def brand(self):
    return self._brand

@brand.setter
def brand(self, value):
    self._brand = value
As a general rule, in the context of code written in Python, prefer regular functions over lambda expressions. Nonetheless, there are cases that benefit from lambda syntax, as you will see in the next section.


Remove ads
Appropriate Uses of Lambda Expressions
Lambdas in Python tend to be the subject of controversies. Some of the arguments against lambdas in Python are:

Issues with readability
The imposition of a functional way of thinking
Heavy syntax with the lambda keyword
Despite the heated debates questioning the mere existence of this feature in Python, lambda functions have properties that sometimes provide value to the Python language and to developers.

The following examples illustrate scenarios where the use of lambda functions is not only suitable but encouraged in Python code.

Classic Functional Constructs
Lambda functions are regularly used with the built-in functions map() and filter(), as well as functools.reduce(), exposed in the module functools. The following three examples are respective illustrations of using those functions with lambda expressions as companions:

>>> list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
['CAT', 'DOG', 'COW']
>>> list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
['dog', 'cow']
>>> from functools import reduce
>>> reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
'cat | dog | cow'
You may have to read code resembling the examples above, albeit with more relevant data. For that reason, it’s important to recognize those constructs. Nevertheless, those constructs have equivalent alternatives that are considered more Pythonic. In Alternatives to Lambdas, you’ll learn how to convert higher-order functions and their accompanying lambdas into other more idiomatic forms.

Key Functions
Key functions in Python are higher-order functions that take a parameter key as a named argument. key receives a function that can be a lambda. This function directly influences the algorithm driven by the key function itself. Here are some key functions:

sort(): list method
sorted(), min(), max(): built-in functions
nlargest() and nsmallest(): in the Heap queue algorithm module heapq
Imagine that you want to sort a list of IDs represented as strings. Each ID is the concatenation of the string id and a number. Sorting this list with the built-in function sorted(), by default, uses a lexicographic order as the elements in the list are strings.

To influence the sorting execution, you can assign a lambda to the named argument key, such that the sorting will use the number associated with the ID:

>>> ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
>>> print(sorted(ids)) # Lexicographic sort
['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
>>> sorted_ids = sorted(ids, key=lambda x: int(x[2:])) # Integer sort
>>> print(sorted_ids)
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']
UI Frameworks
UI frameworks like Tkinter, wxPython, or .NET Windows Forms with IronPython take advantage of lambda functions for mapping actions in response to UI events.

The naive Tkinter program below demonstrates the usage of a lambda assigned to the command of the Reverse button:

import tkinter as tk
import sys

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300x100")
label = tk.Label(window, text="Lambda Calculus")
label.grid(column=0, row=0)
button = tk.Button(
    window,
    text="Reverse",
    command=lambda: label.configure(text=label.cget("text")[::-1]),
)
button.grid(column=0, row=1)
window.mainloop()
Clicking the button Reverse fires an event that triggers the lambda function, changing the label from Lambda Calculus to suluclaC adbmaL*:

Animated TkInter Windows demonstrating the action of the button to the text
Both wxPython and IronPython on the .NET platform share a similar approach for handling events. Note that lambda is one way to handle firing events, but a function may be used for the same purpose. It ends up being self-contained and less verbose to use a lambda when the amount of code needed is very short.

To explore wxPython, check out How to Build a Python GUI Application With wxPython.


Remove ads
Python Interpreter
When you’re playing with Python code in the interactive interpreter, Python lambda functions are often a blessing. It’s easy to craft a quick one-liner function to explore some snippets of code that will never see the light of day outside of the interpreter. The lambdas written in the interpreter, for the sake of speedy discovery, are like scrap paper that you can throw away after use.

timeit
In the same spirit as the experimentation in the Python interpreter, the module timeit provides functions to time small code fragments. timeit.timeit() in particular can be called directly, passing some Python code in a string. Here’s an example:

>>> from timeit import timeit
>>> timeit("factorial(999)", "from math import factorial", number=10)
0.0013087529951008037
When the statement is passed as a string, timeit() needs the full context. In the example above, this is provided by the second argument that sets up the environment needed by the main function to be timed. Not doing so would raise a NameError exception.

Another approach is to use a lambda:

>>> from math import factorial
>>> timeit(lambda: factorial(999), number=10)
0.0012704220062005334
This solution is cleaner, more readable, and quicker to type in the interpreter. Although the execution time was slightly less for the lambda version, executing the functions again may show a slight advantage for the string version. The execution time of the setup is excluded from the overall execution time and shouldn’t have any impact on the result.

Monkey Patching
For testing, it’s sometimes necessary to rely on repeatable results, even if during the normal execution of a given software, the corresponding results are expected to differ, or even be totally random.

Let’s say you want to test a function that, at runtime, handles random values. But, during the testing execution, you need to assert against predictable values in a repeatable manner. The following example shows how, with a lambda function, monkey patching can help you:

from contextlib import contextmanager
import secrets

def gen_token():
    """Generate a random token."""
    return f'TOKEN_{secrets.token_hex(8)}'

@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex
    function during testing.
    """
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex

def test_gen_key():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

test_gen_key()
A context manager helps with insulating the operation of monkey patching a function from the standard library (secrets, in this example). The lambda function assigned to secrets.token_hex() substitutes the default behavior by returning a static value.

This allows testing any function depending on token_hex() in a predictable fashion. Prior to exiting from the context manager, the default behavior of token_hex() is reestablished to eliminate any unexpected side effects that would affect other areas of the testing that may depend on the default behavior of token_hex().

Unit test frameworks like unittest and pytest take this concept to a higher level of sophistication.

With pytest, still using a lambda function, the same example becomes more elegant and concise :

import secrets

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_key(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"
With the pytest monkeypatch fixture, secrets.token_hex() is overwritten with a lambda that will return a deterministic value, feedfacecafebeef, allowing to validate the test. The pytest monkeypatch fixture allows you to control the scope of the override. In the example above, invoking secrets.token_hex() in subsequent tests, without using monkey patching, would execute the normal implementation of this function.

Executing the pytest test gives the following result:

$ pytest test_token.py -v
============================= test session starts ==============================
platform linux -- Python 3.7.2, pytest-4.3.0, py-1.8.0, pluggy-0.9.0
cachedir: .pytest_cache
rootdir: /home/andre/AB/tools/bpython, inifile:
collected 1 item

test_token.py::test_gen_key PASSED                                       [100%]

=========================== 1 passed in 0.01 seconds ===========================
The test passes as we validated that the gen_token() was exercised, and the results were the expected ones in the context of the test.


Remove ads
Alternatives to Lambdas
While there are great reasons to use lambda, there are instances where its use is frowned upon. So what are the alternatives?

Higher-order functions like map(), filter(), and functools.reduce() can be converted to more elegant forms with slight twists of creativity, in particular with list comprehensions or generator expressions.

To learn more about list comprehensions, check out When to Use a List Comprehension in Python. To learn more about generator expressions, check out How to Use Generators and yield in Python.

Map
The built-in function map() takes a function as a first argument and applies it to each of the elements of its second argument, an iterable. Examples of iterables are strings, lists, and tuples. For more information on iterables and iterators, check out Iterables and Iterators.

map() returns an iterator corresponding to the transformed collection. As an example, if you wanted to transform a list of strings to a new list with each string capitalized, you could use map(), as follows:

>>> list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
['Cat', 'Dog', 'Cow']
You need to invoke list() to convert the iterator returned by map() into an expanded list that can be displayed in the Python shell interpreter.

Using a list comprehension eliminates the need for defining and invoking the lambda function:

>>> [x.capitalize() for x in ['cat', 'dog', 'cow']]
['Cat', 'Dog', 'Cow']
Filter
The built-in function filter(), another classic functional construct, can be converted into a list comprehension. It takes a predicate as a first argument and an iterable as a second argument. It builds an iterator containing all the elements of the initial collection that satisfies the predicate function. Here’s an example that filters all the even numbers in a given list of integers:

>>> even = lambda x: x%2 == 0
>>> list(filter(even, range(11)))
[0, 2, 4, 6, 8, 10]
Note that filter() returns an iterator, hence the need to invoke the built-in type list that constructs a list given an iterator.

The implementation leveraging the list comprehension construct gives the following:

>>> [x for x in range(11) if x%2 == 0]
[0, 2, 4, 6, 8, 10]
Reduce
Since Python 3, reduce() has gone from a built-in function to a functools module function. As map() and filter(), its first two arguments are respectively a function and an iterable. It may also take an initializer as a third argument that is used as the initial value of the resulting accumulator. For each element of the iterable, reduce() applies the function and accumulates the result that is returned when the iterable is exhausted.

To apply reduce() to a list of pairs and calculate the sum of the first item of each pair, you could write this:

>>> import functools
>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
6
A more idiomatic approach using a generator expression, as an argument to sum() in the example, is the following:

>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> sum(x[0] for x in pairs)
6
A slightly different and possibly cleaner solution removes the need to explicitly access the first element of the pair and instead use unpacking:

>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
>>> sum(x for x, _ in pairs)
6
The use of underscore (_) is a Python convention indicating that you can ignore the second value of the pair.

sum() takes a unique argument, so the generator expression does not need to be in parentheses.

Are Lambdas Pythonic or Not?
PEP 8, which is the style guide for Python code, reads:

Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier. (Source)

This strongly discourages using lambda bound to an identifier, mainly where functions should be used and have more benefits. PEP 8 does not mention other usages of lambda. As you have seen in the previous sections, lambda functions may certainly have good uses, although they are limited.

A possible way to answer the question is that lambda functions are perfectly Pythonic if there is nothing more Pythonic available. I’m staying away from defining what “Pythonic” means, leaving you with the definition that best suits your mindset, as well as your personal or your team’s coding style.

Beyond the narrow scope of Python lambda, How to Write Beautiful Python Code With PEP 8 is a great resource that you may want to check out regarding code style in Python.

Conclusion
You now know how to use Python lambda functions and can:

Write Python lambdas and use anonymous functions
Choose wisely between lambdas or normal Python functions
Avoid excessive use of lambdas
Use lambdas with higher-order functions or Python key functions
If you have a penchant for mathematics, you may have some fun exploring the fascinating world of lambda calculus.

Python lambdas are like salt. A pinch in your spam, ham, and eggs will enhance the flavors, but too much will spoil the dish.