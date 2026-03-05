# 1.3.2 - Interfacce a riga di comando (`argparse`)

Il corretto sviluppo di uno script Python implica la necessità di evitare modifiche al codice sorgente ogni volta che dobbiamo cambiare un parametro (ad esempio, il numero di epoche di addestramento, il percorso del dataset, o il learning rate del modello). In tal senso, il modulo [`argparse`](https://docs.python.org/3/library/argparse.html) della libreria standard ci permette di passare questi parametri direttamente da riga di comando (CLI).

## Uno script con `argparse`

L'uso di `argparse` prevede quattro step fondamentali:

1. Per prima cosa, dovremo creare un oggetto di classe [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser).
2. A questo punto, dovremo aggiungere gli argomenti attesi dello script (`add_argument`).
3. Chiameremo quindi il metodo `parse_args` per effettuare il parsing degli argomenti attesi al punto 2.
4. Utilizzeremo infine i valori di cui è stato fatto il parsing all'interno dello script.

Proviamo a fare un esempio. Immaginiamo di voler popolare una semplice struttura dati che rappresenta una persona. Per farlo, utilizzeremo una [dataclass](../02_syntax/05_classes.md).

```py
from dataclasses import dataclass

@dataclass
class Persona:
    nome: str
    cognome: str
    eta: int
    studente: bool
```

A questo punto, possiamo creare un nuovo script, che chiameremo `run.py`, e definire una funzione `main` che accetta gli argomenti di cui è stato fatto il parsing, creando contestualmente l'oggetto.

```py
import argparse

# ...

def run(args: argparse.Namespace):
    """
    Logica principale dello script.
    Riceve i parametri parsati e istanzia la classe.
    """
    p = Persona(
        nome=args.nome,
        cognome=args.cognome,
        eta=args.eta,
        studente=args.studente
    )
    print(f"Creato oggetto: {p}")

if __name__ == '__main__':
    # 1. Creazione del parser
    parser = argparse.ArgumentParser(description="Script demo per gestire persone.")

    # 2. Aggiunta argomenti
    
    # Argomento con valore di default (Opzionale)
    parser.add_argument(
        '-n', '--nome',
        help='Nome della persona',
        default='Mario'
    )
    
    # Argomento obbligatorio (required=True)
    parser.add_argument(
        '-c', '--cognome',
        help='Cognome della persona',
        required=True
    )

    # 3. Parsing
    args = parser.parse_args()
    
    # 4. Esecuzione
    run(args)
```

A questo punto possiamo eseguire lo script da terminale:

```sh
python run.py 
# Errore!: manca il cognome (obbligatorio)
# Output: error: the following arguments are required: -c/--cognome

python run.py -c Rossi
# Funzionamento corretto
# Output: Creato oggetto: Persona(nome='Mario', cognome='Rossi', ...)
```

!!!tip "Help automatico"
    Il modulo `argparse` genera automaticamente un messaggio di aiuto. Per vederlo, proviamo a lanciare lo script usando la dicitura `python run.py --help`

## Gestione del tipo degli argomenti con `type`

Di default, `argparse` tratta tutti gli argomenti passati come delle stringhe. Qualora vogliamo passare un numero (ad esempio, l'età), dovremo specificarne il tipo mediante l'argomento `type`:

```py
    parser.add_argument(
        '-a', '--age',
        help='Età della persona',
        type=int,           # Conversione automatica in intero
        default=18
    )
```

Se provassimo a passare un valore non numerico, lo script si fermerà mostrando a schermo un errore esplicativo.

## Flag Booleani con `store_true`

Spesso abbiamo bisogno di alcuni "flag comportamentali" che fungano da interruttori *on/off*, come ad esempio `--use-gpu`, `--verbose`, o `--dry-run`. In questi casi non è necessario passare un valore, ma soltanto sapere se il flag è presente o meno: per farlo, potremo usare l'argomento `action='store_true'`. Ad esempio:

```py
    parser.add_argument(
        '-s', '--student',
        help='Indica se la persona è uno studente',
        action='store_true' # Se presente diventa True, altrimenti False
    )
```

Utilizzo:
```sh
# Senza flag -> studente=False
python run.py -c Rossi 

# Con flag -> studente=True
python run.py -c Rossi --studente
```

## Scelte vincolate con `choices`

Immaginiamo di avere un parametro che può assumere soltanto un insieme limitato di valori. In questo caso, possiamo usare il parametro `choices`:

```py
    parser.add_argument(
        '--role',
        choices=['admin', 'user', 'guest'],
        default='user',
        help='Ruolo nel sistema'
    )
```

Se passiamo, ad esempio, `--role superadmin`, `argparse` bloccherà l'esecuzione segnalando che il valore non è tra quelli ammessi.

## Esempio Completo

Chiudiamo con uno esempio di codice "pronto all'uso" ed in grado di coprire molti dei casi d'uso che possiamo trovare in un progetto di machine learning.

```py
import argparse

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Iperparametri (Numeri)
    parser.add_argument(
        '--epochs',
        type=int,
        default=10,
        help='Numero di epoche')
    parser.add_argument(
        '--lr',
        type=float,
        default=0.001,
        help='Learning rate')
    
    # Percorsi (Stringhe)
    parser.add_argument(
        '--data',
        type=str,
        required=True,
        help='Path del dataset')
    
    # Configurazioni (Scelte e Flag)
    parser.add_argument(
        '--model',
        choices=['resnet', 'vgg'],
        ùdefault='resnet')
    parser.add_argument(
        '--gpu',
        action='store_true',
        help='Abilita training su GPU')

    args = parser.parse_args()
    
    print(f"Training {args.model} on {args.data} for {args.epochs} epochs...")
    if args.gpu:
        print("GPU Enabled!")

if __name__ == '__main__':
    main()
```

Con questo esempio abbiamo quindi un vero e proprio *template* che possiamo seguire per i nostri esperimenti.
