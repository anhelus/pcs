Ecco la bozza per il file **1.3.3**, sintetizzata e adattata dai due lunghi articoli che mi hai fornito.

Ho unito i concetti di **Type Hinting avanzato** (dall'articolo su *mypy*) con la potenza di **Pydantic** (dall'articolo su *Pydantic*), creando un percorso logico che va dalla teoria alla pratica ingegneristica. Ho aggiornato la sintassi allo standard moderno (Python 3.10+, usando `|` per le Union e i generici built-in `list[]` invece di `List[]`).

---

# 1.3.3 - Type Hinting e Validazione Dati (Pydantic)

Python è un linguaggio a **tipizzazione dinamica**: non siamo obbligati a dichiarare il tipo delle variabili e questo può cambiare durante l'esecuzione. Tuttavia, in progetti complessi di Data Science e ML Engineering, questa libertà può diventare una trappola, rendendo difficile capire che forma devono avere i dati che passano attraverso le nostre pipeline.

In questa lezione vedremo come rendere il codice robusto usando il **Type Hinting Avanzato** e come validare i dati a runtime con **Pydantic**.

## Type Hinting Avanzato

Abbiamo già visto come annotare funzioni semplici (`def func(x: int) -> int`). Vediamo ora come gestire strutture dati complesse.

### Tipi Composti (List, Dict, Tuple)

Nelle versioni moderne di Python (3.9+), possiamo usare i tipi nativi per definire strutture complesse.

```python
# Lista di stringhe
nomi: list[str] = ["Mario", "Luigi"]

# Dizionario con chiavi stringa e valori interi
voti: dict[str, int] = {"Matematica": 28, "Fisica": 30}

# Tupla con struttura fissa (es. coordinate x, y)
punto: tuple[float, float] = (12.5, 45.0)
```

### Union e Optional

Spesso una variabile può assumere più tipi.
*   **Union:** Il valore può essere di tipo A *oppure* B. Dal Python 3.10 si usa l'operatore `|`.
*   **Optional:** Il valore può essere di un tipo specifico *oppure* `None`.

```python
# Vecchia sintassi (typing.Union)
from typing import Optional, Union

# Nuova sintassi (Python 3.10+)
def elabora_dato(dato: int | float) -> str | None:
    if dato < 0:
        return None
    return f"Valore: {dato}"

# Optional è equivalente a: Type | None
utente: str | None = None
```

### Il tipo `Any`

Il tipo `Any` (dal modulo `typing`) è una "via di fuga". Dice al sistema di controllo: "Fidati di me, qui può esserci qualsiasi cosa".
Va usato con estrema parsimonia, perché disabilita di fatto i controlli di tipo.

## Static Type Checking (`mypy`)

Le annotazioni di tipo in Python vengono **ignorate** dall'interprete a runtime. Se passi una stringa dove è richiesto un intero, Python proverà comunque ad eseguire il codice (e probabilmente crasherà dopo).

Per verificare la coerenza dei tipi *prima* di eseguire il codice, si usano gli **Static Type Checkers**. Il più famoso è **mypy**.

```bash
pip install mypy
```

Esempio di file `check.py` con errore:
```python
def somma(a: int, b: int) -> int:
    return a + b

print(somma(10, "20"))  # Errore di tipo!
```

Eseguendo `mypy check.py`:
```text
check.py:4: error: Argument 2 to "somma" has incompatible type "str"; expected "int"
```

## Pydantic: Validazione Dati a Runtime

Se `mypy` controlla il codice mentre lo scrivi, **Pydantic** controlla i dati mentre il programma gira. È la libreria standard *de facto* per la validazione dati in Python (usata da FastAPI, LangChain, HuggingFace).

Pydantic non si limita a controllare i tipi: fa **Data Parsing**. Se i dati in ingresso non sono nel formato corretto ma possono essere convertiti (es. la stringa "10" passata dove serve un `int`), Pydantic lo farà. Altrimenti, solleverà un errore dettagliato.

### Il `BaseModel`

Tutto ruota attorno alla classe `BaseModel`. Definiamo i nostri schemi dati come classi.

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

user = Utente.model_validate(dati_esterni)

print(user.id)        # 123 (è un intero!)
print(type(user.data_registrazione)) # <class 'datetime.datetime'>
```

### Gestione degli Errori

Se i dati non sono validi, Pydantic solleva un'eccezione `ValidationError` che spiega esattamente cosa non va.

```python
from pydantic import ValidationError

try:
    Utente(id="ciao", nome="Luigi", email="luigi@test.com")
except ValidationError as e:
    print(e)
```
Output:
```text
1 validation error for Utente
id
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, ...]
```

### Validazione Avanzata con `Field`

Possiamo aggiungere vincoli più stringenti ai dati (es. numeri positivi, lunghezza stringhe, regex) usando `Field`.

```python
from pydantic import BaseModel, Field, EmailStr

class Prodotto(BaseModel):
    nome: str = Field(min_length=3, max_length=50)
    prezzo: float = Field(gt=0, description="Il prezzo deve essere positivo")
    sku: str = Field(pattern=r"^[A-Z]{3}-\d{3}$") # Es. ABC-123
    
    # EmailStr richiede: pip install "pydantic[email]"
    email_fornitore: EmailStr 
```

### Serializzazione

Pydantic rende facilissimo convertire i modelli complessi in dizionari o JSON, pronti per essere inviati via API o salvati su file.

```python
# Convertire in dizionario
print(user.model_dump())

# Convertire in JSON string
print(user.model_dump_json())
```

## Gestione Configurazioni (`BaseSettings`)

In ambito Engineering, non si scrivono mai password o chiavi API direttamente nel codice (hardcoding). Si usano le **Variabili d'Ambiente**.
Pydantic offre un modulo separato `pydantic-settings` per gestire la configurazione dell'applicazione in modo tipizzato.

```bash
pip install pydantic-settings
```

```python
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    app_name: str = "My AI App"
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
    Usa sempre Pydantic quando devi gestire dati che provengono dall'esterno (API, file CSV, input utente) o configurazioni. Garantisce che se il programma parte, i dati sono nella forma corretta.