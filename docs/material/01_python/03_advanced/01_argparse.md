# 1.3.1 - Il modulo `argparse`

Il modulo [`argparse`](https://docs.python.org/3/library/argparse.html) ci permette di passare ad uno script Python degli argomenti utilizzando la riga di comando.

Per farlo, dobbiamo seguire un processo articolato in quattro step:

1. creiamo un oggetto di classe [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser);
2. aggiungiamo gli argomenti di cui intendiamo fare il parsing;
3. effettuiamo il parsing di questi argomenti;
4. usiamo gli argomenti passati.

Come molte cose in Python, è più complesso descrivere questa serie di passaggi che implementarla. Di conseguenza, usiamo il solito approccio *learn by doing*, usando un semplice esempio.

Supponiamo di avere una classe `Persona`, definita come segue:

```py linenums="1"
class Persona():

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f'{self.nome} {self.cognome}'
```

Scriviamo adesso uno script per creare un oggetto di questa classe, specificandone i parametri mediante riga di comando. Per prima cosa, importiamo la libreria `argparse`:

```py
import argparse
```

Definiamo quindi un metodo che accetti come parametro un generico insieme di argomenti (che chiameremo `args`), e che crei al suo interno un'istanza di `Persona` a partire da questi argomenti.

```py linenums="1"
def run(args):
    """ Definiamo il metodo `run` che sarà invocato
    ad ogni esecuzione dello script.
    Il metodo accetta un parametro args che rappresenta
    gli argomenti di cui è stato effettuato il parsing.
    """
    p = Persona(args.nome, args.cognome)
    print(p)
```

Possiamo adesso definire il punto di accesso al nostro script come segue:

```py linenums="1"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
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
    args = parser.parse_args()
    run(args)
```

In particolare:

* alla riga 2, creeremo un oggetto di tipo `ArgumentParser`, che chiameremo `parser`;
* alla riga 3, aggiungeremo un primo argomento (il nome) al `parser` mediante il metodo [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument);
* alla riga 4, aggiungeremo un *flag* che contrassegnerà l'argomento;
* alla riga 5, aggiungeremo un *nome* per indicare l'argomento;
* alla riga 6, andremo a definire un messaggio di aiuto mediante il parametro `help` che descriverà a cosa serve l'argomento;
* alla riga 7, assegneremo un valore di default all'argomento relativo al nome della persona;
* alla riga 8, creeremo un secondo argomento, ovvero il cognome, aggiungendolo al parser;
* alla riga 12, specificheremo che l'argomento `cognome` è richiesto settando il parametro `required` a `True`;
* alla riga 13, andremo ad effettuare il parsing degli argomenti passati, salvandoli in una variabile chiamata `args`;
* infine, alla riga 14, passeremo la variabile `args` al metodo `run()` definito in precedenza.

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
