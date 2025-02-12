Generator in Python
Cosa sono i Generator?
I generator in Python sono una semplice e potente implementazione del pattern "iteratore". Una funzione generator consente di iterare su un set di dati senza doverli prima memorizzare completamente in memoria. Questa funzionalità è utile per lavorare con dataset di grandi dimensioni.

Creazione di un Generator
Un generator si crea utilizzando una funzione con l'istruzione yield:

python
def mio_generator():
    yield 1
    yield 2
    yield 3

gen = mio_generator()
for val in gen:
    print(val)
Funzionamento del yield
L'istruzione yield è simile a return, ma invece di terminare la funzione e restituire un valore, salva lo stato della funzione e lo riprende al punto successivo alla yield alla chiamata successiva.

Esempi Pratici
1. Generatore di Numeri Fattoriali
python
def fattoriale():
    n = 1
    result = 1
    while True:
        yield result
        n += 1
        result *= n

gen = fattoriale()
for _ in range(5):
    print(next(gen))
2. Generatore di Numeri di Fibonacci
python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(5):
    print(next(gen))
Generator Expressions
Oltre alle funzioni generator, è possibile creare generator in modo simile alle comprehension list, usando le parentesi tonde:

python
gen_expr = (x * x for x in range(10))
for val in gen_expr:
    print(val)
Vantaggi dei Generator
Efficienza della Memoria: Ideali per lavorare con grandi dataset, poiché non memorizzano tutti i dati in memoria.

Lazy Evaluation: Calcolano i valori al bisogno, migliorando le performance.