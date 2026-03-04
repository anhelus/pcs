# 1.3.5 - Introduzione al Testing (`pytest`)

Scrivere codice che funziona "sul momento" è facile. Scrivere codice che **continua a funzionare** dopo mesi di modifiche e refactoring richiede i **Test Automatici**.

In Python, lo standard industriale per il testing è **`pytest`**. Rispetto al modulo nativo `unittest`, pytest richiede meno codice boilerplate, offre un output più leggibile e dispone di un ecosistema di plugin potentissimo.

## Installazione

Come sempre, installiamo la libreria nel nostro ambiente virtuale:

```bash
pip install pytest
```

## Il primo Test

In `pytest`, un test è semplicemente una funzione che inizia con il prefisso `test_` e che usa l'istruzione `assert` per verificare una condizione. Se l'asserzione è vera, il test passa. Se è falsa, il test fallisce.

Immaginiamo di avere un file `operazioni.py`:

```python
# operazioni.py
def somma(a: int, b: int) -> int:
    return a + b

def divisione(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Divisione per zero!")
    return a / b
```

Creiamo un file di test chiamato `test_operazioni.py`:

```python
# test_operazioni.py
from operazioni import somma, divisione
import pytest

def test_somma_positivi():
    assert somma(2, 3) == 5

def test_somma_negativi():
    assert somma(-1, -1) == -2

def test_divisione_errore():
    # Verifichiamo che venga lanciata l'eccezione giusta
    with pytest.raises(ValueError):
        divisione(10, 0)
```

### Eseguire i test

Da terminale, eseguiamo semplicemente:

```bash
pytest
```

L'output ci mostrerà dei punti (`.`) per i test passati e delle `F` per quelli falliti, con un report dettagliato degli errori.

## Fixtures: Gestione delle Dipendenze

Spesso i test hanno bisogno di dati iniziali o configurazioni (es. connettersi a un DB di test, caricare un dataset, creare un oggetto complesso). Invece di ripetere questo codice in ogni test, usiamo le **Fixtures**.

Una fixture è una funzione decorata con `@pytest.fixture` che restituisce un dato. I test possono richiedere questo dato passandolo come argomento.

```python
import pytest

# Definizione della Fixture
@pytest.fixture
def dati_utente():
    """Restituisce un dizionario dati simulato per i test."""
    return {
        "nome": "Mario",
        "cognome": "Rossi",
        "eta": 30,
        "is_admin": False
    }

# Utilizzo della Fixture (Dependency Injection)
def test_nome_completo(dati_utente):
    full_name = f"{dati_utente['nome']} {dati_utente['cognome']}"
    assert full_name == "Mario Rossi"

def test_maggiorenne(dati_utente):
    assert dati_utente['eta'] >= 18
```

Le fixtures sono fondamentali in Data Science per caricare, ad esempio, un modello o un DataFrame di prova una sola volta e riutilizzarlo in decine di test.

### Il file `conftest.py`

Se vogliamo condividere le fixtures tra più file di test, non serve importarle. Basta definirle in un file speciale chiamato `conftest.py` nella cartella dei test. Pytest le renderà automaticamente disponibili a tutti i test del progetto.

## Parametrizzazione

A volte vogliamo testare la stessa funzione con molti input diversi. Invece di scrivere dieci funzioni `test_...` quasi identiche, usiamo il decoratore `@pytest.mark.parametrize`.

```python
# Funzione da testare (es. controlla se una stringa è palindroma)
def is_palindroma(testo: str) -> bool:
    testo_pulito = testo.replace(" ", "").lower()
    return testo_pulito == testo_pulito[::-1]

# Test parametrizzato
@pytest.mark.parametrize("input_string, expected", [
    ("anna", True),
    ("otto", True),
    ("python", False),
    ("i topi non avevano nipoti", True), # Frase complessa
    ("", True) # Caso limite stringa vuota
])
def test_palindroma(input_string, expected):
    assert is_palindroma(input_string) == expected
```

In questo esempio, pytest eseguirà 5 test separati. Se uno fallisce, sapremo esattamente quale caso (input) ha causato il problema.

## Organizzazione del Progetto

La struttura standard per un progetto Python professionale prevede una cartella `tests/` separata dal codice sorgente:

```text
my_project/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py      <-- Fixtures condivise
│   ├── test_main.py
│   └── test_utils.py
├── .venv/
└── requirements.txt
```

!!!tip "Best Practice"
    Non aspettare di aver finito il progetto per scrivere i test. Scrivi i test per le funzioni critiche mentre le sviluppi. Questo ti salverà ore di debugging in futuro.