# 1.3.1 - Il modulo `argparse`

Il modulo [`argparse`](https://docs.python.org/3/library/argparse.html) è una libreria di Python che ci consente di passare argomenti a uno script utilizzando la riga di comando.

Per utilizzare `argparse`, dobbiamo seguire quattro semplici passaggi:

1. Creare un oggetto [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser), che ci permetterà di gestire gli argomenti.
2. Aggiungere gli argomenti che desideriamo gestire.
3. Effettuare il parsing degli argomenti passati.
4. Utilizzare gli argomenti passati per eseguire le operazioni desiderate.

Per aiutarci a comprendere questo processo, useremo un esempio semplice. Supponiamo di avere una classe chiamata `Persona` definita nel seguente modo:

```python
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f'{self.nome} {self.cognome}'
```

Creiamo ora uno script per creare un'istanza di questa classe, specificando i parametri tramite la riga di comando. Iniziamo importando la libreria `argparse`:

```python
import argparse
```

Definiamo quindi il metodo `run` che accetta come parametro un oggetto `args`, rappresentante gli argomenti passati tramite la riga di comando:

```python
def run(args):
    """
    Definiamo il metodo `run` che viene eseguito ogni volta che lo script viene avviato.
    Il metodo accetta un parametro chiamato `args` che contiene gli argomenti del parsing.
    """
    p = Persona(args.nome, args.cognome)
    print(p)
```

Ora possiamo definire il punto di ingresso dello script nel blocco `if __name__ == '__main__':`. Iniziamo creando un oggetto `ArgumentParser` chiamato `parser`:

```python
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
```

Aggiungiamo quindi il primo argomento, il nome, al nostro `parser` utilizzando il metodo `add_argument()`:

```python
parser.add_argument(
    '-n',
    '--nome',
    help='Nome della persona',
    default='Pippo')
```

Specifichiamo un *flag* per identificare l'argomento e un *nome* per riferirci ad esso. Utilizziamo il parametro `help` per fornire una descrizione dell'argomento e impostiamo un valore di default per il nome.

Aggiungiamo quindi il secondo argomento, il cognome:

```python
parser.add_argument(
    '-c',
    '--cognome',
    help='Cognome della persona',
    required=True)
```

Indichiamo che il cognome è un argomento obbligatorio, utilizzando il parametro `required=True`.

Successivamente, effettuiamo il parsing degli argomenti passati e li salviamo nella variabile `args`:

```python
args = parser.parse_args()
```

Infine, chiamiamo il metodo `run` passando l'oggetto `args`:

```python
run(args)
```

Ecco un riassunto dei passaggi effettuati:

1. Creiamo un oggetto `ArgumentParser`.
2. Aggiungiamo i nostri argomenti utilizzando il metodo `add_argument()`.
3. Effettuiamo il

 parsing degli argomenti passati utilizzando il metodo `parse_args()`.
4. Utilizziamo gli argomenti passati per eseguire le operazioni desiderate.

Ora siamo pronti per eseguire il nostro script e gestire gli argomenti dalla riga di comando.

!!!tip "La variabile `args`"
    La variabile `args` definisce un oggetto di tipo [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace) all'interno del quale sono salvati tutti gli argomenti passati allo script, ciascuno dei quali invocabile con la notazione `args.nome_argomento`.

!!!tip "Utilizzare l'`help`"
    Definire il parametro `help` ci permette di usare il comando `python nome_script -h`, che ci restituisce le righe di aiuto specificate durante il parsing. Di conseguenza, è opportuno evitare di inserire dei flag del tipo `-h`, onde evitare collisioni ed errori del parser.

Salviamo il nostro codice in uno script chiamato `run.py`. Per eseguirlo, sfrutteremo i flag `-n` e `-c` per specificare rispettivamente nome e cognome:

```sh
python run.py -n Nome -c Cognome
```

A schermo vedremo:

```sh
Nome Cognome
```

Possiamo anche omettere il nome, ma non il cognome, in quanto è un parametro richiesto:

```sh
python run.py -c Cognome
Pippo Cognome
```

Possiamo poi invocare l'help scrivendo:

```sh
python run.py -h
```

Proviamo infine ad utilizzare la notazione completa:

```sh
python run.py --nome Nome --cognome Cognome
Nome Cognome
```

Proviamo adesso a modificare la classe `Persona` inserendovi l'età. In tal senso, specifichiamo che l'età deve essere un valore intero; qualora questo non avvenga, sarà lanciata un'eccezione.

```py linenums="1"
class Persona():

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    @property
    def eta(self):
        return self._eta
    
    @eta.setter
    def eta(self, value):
        if not isinstance(eta, int):
            raise ValueError("Fornire un intero per l'età.")
        self._eta = value
    
    def __str__(self):
        return f'{self.nome} {self.cognome}'
```

Modifichiamo il resto dello script per adattarci alle nuove esigenze. Partiamo dal metodo `run`:

```py linenums="1" hl_lines="7"
def run(args):
    """ Definiamo il metodo `run` che sarà invocato
    ad ogni esecuzione dello script.
    Il metodo accetta un parametro args che rappresenta
    gli argomenti di cui è stato effettuato il parsing.
    """
    p = Persona(args.nome, args.cognome, args.eta)
    print(p)
```

Aggiungiamo poi un altro argomento al `parser`:

```py linenums="1" hl_lines="13 14 15 16"
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-n',                       
        '--nome',                   
        help='Nome della persona',  
        default='Pippo')            
    parser.add_argument(
        '-c',
        '--cognome',
        help='Cognome della persona',
        required=True)              
    parser.add_argument(
        '-e',
        '--eta',
        help='Età della persona')
    args = parser.parse_args()
    run(args)
```

Proviamo ad eseguire di nuovo lo script:

```sh
python run.py -n Nome -c Cognome -e 18
```

Vedremo che viene lanciato un errore, in quanto gli argomenti passati mediante argparse sono normalmente interpretati come delle stringhe.

Per risolvere questo problema dovremo specificare il parametro `type`, ponendolo ad `int`:

```py linenums="1" hl_lines="5"
parser.add_argument(
    '-e',
    '--eta',
    help='Età della persona',
    type=int)
```

Se proviamo ad eseguire nuovamente lo script non riscontreremo alcun errore.
