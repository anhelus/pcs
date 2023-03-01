# 3.1 - La libreria `argparse`

La libreria [`argparse`](https://docs.python.org/3/library/argparse.html) ci permette di passare ad uno script Python degli argomenti utilizzando la riga di comando.

Per farlo, dobbiamo seguire un processo articolato in quattro step:

1. creiamo un oggetto di classe `ArgumentParser`;
2. aggiungiamo gli argomenti di cui intendiamo fare il parsing;
3. effettuiamo il parsing di questi argomenti;
4. usiamo gli argomenti per chiamare il metodo opportuno

Vediamo un esempio.

Supponiamo di avere una classe `Persona`, e di voler scrivere uno script per creare un oggetto di questa classe mediante riga di comando. Potremo scrivere:

```py
from argparse import ArgumentParser

class Persona():

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f'{self.nome} {self.cognome}'


def run(args):
    """ Definiamo il metodo `run` che sarà invocato
    ad ogni esecuzione dello script.
    Il metodo accetta un parametro args che rappresenta
    gli argomenti di cui è stato effettuato il parsing.
    """
    p = Persona(args.nome, args.cognome)
    print(p)


if __name__ == '__main__':
    # Step 1: creiamo un oggetto di classe `ArgumentParser`
    parser = ArgumentParser()
    # Step 2: aggiungiamo due argomenti al parser
    parser.add_argument(
        '-n',                       # abbreviazione con cui invocare l'argomento
        '--nome',                   # nome completo dell'argomento
        help='Nome della persona',  # messaggio di aiuto per descrivere l'argomento
        default='Pippo',            # valore di default dell'argomento
    )
    parser.add_argument(
        '-c',
        '--cognome',
        help='Cognome della persona',
        required=True               # indica che l'argomento non può essere omesso
    )
    # Step 3: facciamo il parsing degli argomenti
    args = parser.parse_args()      # gli argomenti saranno salvati in args
    # Step 4: passiamo gli argomenti al metodo run
    run(args)
```

Proviamo a salvare questo script in un file `run.py`, ed eseguiamolo usando la notazione abbreviata:

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

```py
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

```py hl_lines="7"
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

```py hl_lines "16 17 18 19 20"
if __name__ == '__main__':
    # Step 1: creiamo un oggetto di classe `ArgumentParser`
    parser = ArgumentParser()
    # Step 2: aggiungiamo due argomenti al parser
    parser.add_argument(
        '-n',                       # abbreviazione con cui invocare l'argomento
        '--nome',                   # nome completo dell'argomento
        help='Nome della persona',  # messaggio di aiuto per descrivere l'argomento
        default='Pippo',            # valore di default dell'argomento
    )
    parser.add_argument(
        '-c',
        '--cognome',
        help='Cognome della persona',
        required=True               # indica che l'argomento non può essere omesso
    )
    parser.add_argument(
        '-e',
        '--eta',
        help='Età della persona'
    )
    # Step 3: facciamo il parsing degli argomenti
    args = parser.parse_args()      # gli argomenti saranno salvati in args
    # Step 4: passiamo gli argomenti al metodo run
    run(args)
```

Proviamo ad eseguire di nuovo lo script:

```sh
python run.py -n Nome -c Cognome -e 18
```

Vedremo che viene lanciato un errore, in quanto gli argomenti passati mediante argparse sono normalmente interpretati come delle stringhe.

Per risolvere questo problema dovremo specificare il parametro `type`, ponendolo ad `int`:

```py hl_lines "5"
parser.add_argument(
    '-e',
    '--eta',
    help='Età della persona',
    type=int
)
```

Se proviamo ad eseguire nuovamente lo script non riscontreremo alcun errore.
