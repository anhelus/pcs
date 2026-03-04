# 1.3.2 - Interfacce a riga di comando (`argparse`)

Sviluppare uno script Python in maniera corretta implica la necessità di evitare la modifica del codice sorgente ogni volta che vogliamo cambiare un parametro come, ad esempio, il numero di epoche di training, il percorso del dataset da analizzare, o il learning rate del nostro modello. Il modulo [`argparse`](https://docs.python.org/3/library/argparse.html) della libreria standard ci permette di passare questi parametri direttamente da riga di comando (CLI).

## Struttura base

L'uso di `argparse` prevede quattro step fondamentali:

1. Per prima cosa, dovremo creare un oggetto di classe [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser).
2. A questo punto, dovremo aggiungere gli argomenti attesi dallo script (`add_argument`).
3.  Effettuare il parsing (`parse_args`);
4.  Usare i valori all'interno dello script.

Usiamo un approccio pratico. Immaginiamo di voler popolare una semplice struttura dati che rappresenta una persona. Per farlo in modo moderno, useremo una [Dataclass](../02_syntax/05_classes.md).

```py
from dataclasses import dataclass

@dataclass
class Persona:
    nome: str
    cognome: str
    eta: int
    studente: bool
```

### Creazione dello script

Creiamo un file `cli_demo.py`. Definiremo una funzione `main` che accetta gli argomenti parsati e crea l'oggetto.

```py
import argparse
from dataclasses import dataclass

# ... (inserire qui la definizione della dataclass Persona) ...

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

Eseguiamo lo script da terminale:

```sh
# Errore: manca il cognome (obbligatorio)
python cli_demo.py 
# Output: error: the following arguments are required: -c/--cognome

# Funzionamento corretto
python cli_demo.py -c Rossi
# Output: Creato oggetto: Persona(nome='Mario', cognome='Rossi', ...)
```

!!!tip "Help automatico"
    `argparse` genera automaticamente un messaggio di aiuto. Provate a lanciare:
    `python cli_demo.py --help`

## Gestione dei Tipi (`type`)

Di default, `argparse` tratta tutto come stringhe. Se vogliamo passare un numero (es. l'età), dobbiamo specificare il tipo.

Aggiungiamo l'argomento età al parser:

```py
    parser.add_argument(
        '-e', '--eta',
        help='Età della persona',
        type=int,           # Conversione automatica in intero
        default=18
    )
```

Se l'utente prova a passare una stringa non numerica, il programma si fermerà prima di eseguire `run()`, mostrando un errore chiaro.

## Flag Booleani (`store_true`)

Spesso in AI abbiamo bisogno di "interruttori" on/off (es. `--use-gpu`, `--verbose`, `--dry-run`). In questi casi non vogliamo passare un valore, ma solo sapere se il flag è presente o meno. Si usa `action='store_true'`.

```py
    parser.add_argument(
        '-s', '--studente',
        help='Indica se la persona è uno studente',
        action='store_true' # Se presente diventa True, altrimenti False
    )
```

Utilizzo:
```sh
# Senza flag -> studente=False
python cli_demo.py -c Rossi 

# Con flag -> studente=True
python cli_demo.py -c Rossi --studente
```

## Vincolare le scelte (`choices`)

Se un parametro può assumere solo un set limitato di valori (es. il modello da usare per il training), possiamo usare `choices`.

```py
    parser.add_argument(
        '--ruolo',
        choices=['admin', 'user', 'guest'],
        default='user',
        help='Ruolo nel sistema'
    )
```

Se l'utente passa `--ruolo superadmin`, `argparse` bloccherà l'esecuzione segnalando che il valore non è tra quelli ammessi.

## Esempio Completo (Template per ML)

Ecco uno snippet "pronto all'uso" che copre il 90% dei casi d'uso in un progetto di Machine Learning:

```py
import argparse

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Iperparametri (Numeri)
    parser.add_argument('--epochs', type=int, default=10, help='Numero di epoche')
    parser.add_argument('--lr', type=float, default=0.001, help='Learning rate')
    
    # Percorsi (Stringhe)
    parser.add_argument('--data', type=str, required=True, help='Path del dataset')
    
    # Configurazioni (Scelte e Flag)
    parser.add_argument('--model', choices=['resnet', 'vgg'], default='resnet')
    parser.add_argument('--gpu', action='store_true', help='Abilita training su GPU')

    args = parser.parse_args()
    
    print(f"Training {args.model} on {args.data} for {args.epochs} epochs...")
    if args.gpu:
        print("GPU Enabled!")

if __name__ == '__main__':
    main()
```