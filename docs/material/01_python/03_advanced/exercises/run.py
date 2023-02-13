from argparse import ArgumentParser

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
        if not isinstance(value, int):
            raise ValueError("Fornire un intero per l'età.")
        self._eta = value
    
    def __str__(self):
        return f'{self.nome} {self.cognome}'


def run(args):
    """ Definiamo il metodo `run` che sarà invocato
    ad ogni esecuzione dello script.
    Il metodo accetta un parametro args che rappresenta
    gli argomenti di cui è stato effettuato il parsing.
    """
    p = Persona(args.nome, args.cognome, args.eta)
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
    parser.add_argument(
        '-e',
        '--eta',
        help='Età della persona',
        type=int
    )
    # Step 3: facciamo il parsing degli argomenti
    args = parser.parse_args()      # gli argomenti saranno salvati in args
    # Step 4: passiamo gli argomenti al metodo run
    run(args)