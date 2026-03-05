# 1.3.3 - Type Hinting e Validazione Dati con Pydantic

Abbiamo già introdotto il concetto di [tipizzazione dinamica](../01_intro/01_intro.md): in pratica, Python non ci obbliga a dichiarare il tipo di variabili, e questo può cambiare in maniera abbastanza "semplice" a runtime. Tuttavia, nei progetti complessi, questa libertà può diventare una trappola, rendendo difficile capire la forma che devono avere i dati che passano attraverso i nostri script e le nostre pipeline di elaborazione.

Per rendere il codice più robusto, quindi, ci viene in aiuto il concetto di *type hinting avanzato*, che possiamo gestire a runtime mediante l'utilizzo della libreria [**Pydantic**](https://docs.pydantic.dev/latest/).

## Type hinting...avanzato?

[Abbiamo già visto](../01_intro/01_intro.md) come sia possibile annotare funzioni semplici. Tuttavia, è necessario imparare anche a gestire delle strutture dati più complesse. Per definirle, le ultime versioni di Python ci mettono a disposizione i tipi nativi. Ad esempio:

```python
# Lista di stringhe
nomi: list[str] = ["Mario", "Luigi"]

# Dizionario con chiavi stringa e valori interi
voti: dict[str, int] = {"Matematica": 28, "Fisica": 30}

# Tupla con struttura fissa (es. coordinate x, y)
punto: tuple[float, float] = (12.5, 45.0)
```

##### Union e Optional

Spesso una variabile può assumere più tipi. In questo caso, potremmo utilizzare due soluzioni:

* le *union* prevedono che il valore possa essere di tipo A *oppure* di tipo B. In Python, dalla versione 3.10, è possibile usare l'operatore `|`;
* gli *optional* prevedono che il valore sia di un tipo specifico, *oppure* `None`.

Questa sintassi va a sostituire quella tenuta fino a Python 3.9, che prevedeva l'uso delle classi `Union` ed `Optional` importate dal package `typing`

```python
# Nuova sintassi per le Union (Python 3.10+)
def elabora_dato(dato: int | float) -> str | None:
    if dato < 0:
        return None
    return f"Valore: {dato}"

# Optional è equivalente a: Type | None
utente: str | None = None
```

##### Il tipo `Any`

Il tipo `Any`, presente anch'esso nel modulo `typing`, permette di specificare all'interprete Python che quel dato può essere di qualsiasi tipo. Il consiglio è di usarlo con estrema cautela, visto che, di fatto, disabilita il type hinting.

## Static Type Checking con `mypy`

E' importante sottolineare come le annotazioni di tipo vengano, nei fatti, *ignorate* a runtime dall'interprete. In altre parole, se passiamo una stringa dove è richiesto un intero, l'interprete proverà comunque ad eseguire il codice, lanciando molto probabilmente un errore immeditamente dopo. Di conseguenza, per verificare la coerenza dei tipi *prima* di eseguire il codice, si utilizzano i cosiddetti *static type checkers*, il più famoso tra i quali è `mypy`. Per usarlo, dobbiamo per prima cosa installarlo:

```bash
pip install mypy
```

A questo punto, proviamo a creare un file `check.py` che contiene un errore di tipo:
```python
def somma(a: int, b: int) -> int:
    return a + b

print(somma(10, "20"))  # Errore di tipo!
```

Eseguendo l'istruzione `mypy check.py` avremo il seguente risultato:

```text
check.py:4: error: Argument 2 to "somma" has incompatible type "str"; expected "int"
```

## Validazione a runtime con Pydantic

Se `mypy` ci permette di controllare il codice durante la fase di scrittura, **Pydantic** è la libreria standard *de facto* per la validazione dei dati in Python, e che permette quindi di controllare i dati mentre il programma è in esecuzione.

Pydantic non si limita al type checking, ma fa anche *data parsing*. In pratica, se i dati in ingresso non sono nel formato corretto, ma possono essere convertiti (ad esempio, una stringa "10" passata dove serve un `int`), Pydantic gestirà la conversione. Altrimenti, solleverà un errore dettagliato.

### La classe `BaseModel`

Il funzionamento di Pydantic ruota attorno alla classe `BaseModel`, che ci permette di definire i nostri schemi dati come classi. Immaginiamo ad esempio di voler implementare una classe `Utente`:

```python
from pydantic import BaseModel
from datetime import datetime

class Utente(BaseModel):
    id: int
    nome: str
    email: str
    is_attivo: bool = True  # Valore di default
    data_registrazione: datetime | None = None

# Creazione di un oggetto (Parsing e Validazione)
dati_esterni = {
    "id": "123",              # Stringa -> convertita in int
    "nome": "Mario Rossi",
    "email": "mario@example.com",
    "data_registrazione": "2024-01-01T12:00:00" # ISO format -> datetime object
}
```

A questo punto, potremo utilizzare il metodo `model_validate` per validare i dati utilizzati.

```py
user = Utente.model_validate(dati_esterni)

print(user.id)        # 123 (è un intero!)
print(type(user.data_registrazione)) # <class 'datetime.datetime'>
```

Qualora i dati non siano validi, Pydantic solleverà un'eccezione di tipo `ValidationError`, la quale spiegherà in maniera precisa l'errore intercorso. Ad esempio:

```python
from pydantic import ValidationError

try:
    Utente(id="ciao", nome="Luigi", email="luigi@test.com")
except ValidationError as e:
    print(e)
```

Questo manderà in output il seguente testo:

```sh
1 validation error for Utente
id
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, ...]
```

### Validazione Avanzata con `Field`

Qualora volessimo aggiungere dei vincoli più stringenti sui dati, come ad esempio numeri positivi o lunghezza delle stringhe, potremo usare la classe `Field`. Ad esempio:

```python
from pydantic import BaseModel, Field, EmailStr

class Prodotto(BaseModel):
    nome: str = Field(min_length=3, max_length=50)
    prezzo: float = Field(gt=0, description="Il prezzo deve essere positivo")
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{3}$") # Es. ABC-123
    
    # EmailStr richiede: pip install "pydantic[email]"
    email_fornitore: EmailStr 
```

### Serializzazione in file JSON

Pydantic rende facile anche convertire gli oggetti complessi in dizionari o serializzarli in JSON pronti per essere inviati, ad esempio, mediante API RESTful. Per farlo, potremo usare i due metodi seguenti:

```python
# Conversione in dizionario
print(user.model_dump())

# Conversione in stringa JSON
print(user.model_dump_json())
```

## Gestione Configurazioni con `BaseSettings`

Pydantic ci mette anche a disposizione un modulo separato, chiamato `pydantic-settings`, che ci permette di gestire le *variabili d'ambiente* e, conseguentemente, la configurazione dell'applicazione in modo tipizzato. Per prima cosa, dobbiamo installare il modulo via pip:

```bash
pip install pydantic-settings
```

A quel punto, potremo creare una nuova configurazione, ad esempio facendo come segue:

```python
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    app_name: str = "Applicazione AI"
    api_key: str
    db_port: int = 5432

    # Opzionale: legge automaticamente da un file .env
    class Config:
        env_file = ".env"

# Pydantic cercherà le variabili d'ambiente APP_NAME, API_KEY, DB_PORT
# Se API_KEY manca, solleverà un errore all'avvio dell'app!
config = Config() 

print(f"Connecting to DB on port {config.db_port} using key {config.api_key}")
```

!!!tip "Best Practice"
    L'utilizzo di Pydantic è estremamente consigliato quando dobbiamo gestire dati che provengono dall'esterno, ovvero mediante API, file CSV, o input dell'utente, oppure configurazioni. Questo garantisce che, se il programma parte, i tipi siano nel formato corretto.