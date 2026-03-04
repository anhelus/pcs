# 1.3.1 - Gestione degli Ambienti (`venv`)

Uno dei problemi più comuni quando sviluppiamo in Python è la *gestione delle dipendenze*, ovvero delle singole librerie che utilizziamo in fase di programmazione. Di default, infatti, Python installa tutte le librerie all'interno di una cartella *globale*, valida per tutto il sistema. Questo comporta due problemi critici:

1. **Corruzione del sistema**: infatti, installare librerie in una cartella globale può creare conflitti con script di sistema che dipendono da una specifica versione di Python.
2. **Conflitti di versione:**: immaginiamo di lavorare su due progetti, di cui il primo richiede `pandas` alla versione 1.0, mentre il secondo richiede `pandas` alla versione 2.0, allo scopo di utilizzare nuove funzionalità. Se installassimo tutto *globalmente*, non sarebbe possibile lavorare contemporaneamente su entrambi i progetti, in quanto ci sarebbe un conflitto tra le versioni della libreria utilizzate.

La soluzione è, quindi, l'utilizzo dei cosiddetti *ambienti virtuali* (*virtual environments*).

## Cos'è un ambiente virtuale?

Un ambiente virtuale è una cartella autocontenuta che include tre cose:
1. Una copia (o un link simbolico) dell'interprete Python.
2. Una cartella `site-packages` isolata dove verranno installate le librerie specifiche per quel progetto.
3. Uno script per attivare e disattivare l'ambiente.

L'utilizzo di un ambiente virtuale per ciascun progetto garantisce il concetto di *isolamento*: ognuno ha le sue librerie, e non interferisce in alcun modo con gli altri.

## Creare un ambiente con `venv`

Python 3 include nativamente il modulo `venv`, che è quello base per la creazione di ambienti virtuali. Per utilizzarlo, dobbiamo aprire il terminale, spostarci nella cartella del nostro progetto, e lanciare il segeunte comando:

```powershell
python -m venv .venv
```

Così facendo andremo a creare una sottocartella chiamata `.venv` nella directory attuale.

!!!tip "Perché `.venv`?"
    Il nome `.venv` è un nome standard assegnato alla cartella dell'ambiente virtuale. Tuttavia, possiamo scegliere quello che più ci aggrada. Il consiglio è però di usare il punto davanti al nome (`.venv`) al fine di rendere la cartella nascosta nei sistemi Unix-like, mantenendola in alto nelle visualizzazioni delle cartelle, e segnalando che è una directory di configurazione non contenente codice sorgente.

## Attivazione dell'ambiente virtuale

Il passo successivo alla creazione dell'ambiente virtuale è la sua *attivazione*, il che implica modificare temporaneamente le variabili d'ambiente del terminale (ed in particolare il `PATH`) per fare in modo che i comandi `python` e `pip` puntino all'ambiente virtuale e non a quello di sistema.

=== "Windows (PowerShell)"
    ```powershell
    .venv\Scripts\activate
    ```
    *Nota: In caso di errore di sicurezza, potrebbe essere necessario eseguire l'istruzione `Set-ExecutionPolicy Unrestricted -Scope Process`.*

=== "macOS / Linux"
    ```bash
    source .venv/bin/activate
    ```

Una volta attivato l'ambiente virtuale, vedremo il nome tra parentesi nel prompt del terminale, ad esempio `(.venv) user@path:~$`.

Una volta attivato l'ambiente, possiamo installare pacchetti in isolamento usando `pip`.

### Riproducibilità: `requirements.txt`

La riproducibilità di un ambiente virtuale è fondamentale per permettere di utilizzare il programma su altre macchine. Per garantirla, è necessario "congelare" lo stato delle librerie installate all'interno di un file chiamato, per convenzione, `requirements.txt`. Per farlo, dobbiamo usare il comando `freeze`:

```bash
pip freeze > requirements.txt
```

Questo creerà un file `requirements.txt` con un elenco preciso di dipendenze. Ad esempio:

```text
numpy==1.26.4
pandas==2.2.1
requests==2.31.0
```

Potremo quindi installare queste esatte dipendenze usando il seguente comando:

```bash
pip install -r requirements.txt
```

!!!danger "Non fare la commit l'ambiente!"
    La cartella `.venv` **NON** va mai caricata su Git o condivisa. Contiene migliaia di file specifici per il nostro sistema operativo, e comporterebbe soltanto problemi di gestione. Di conseguenza, è sempre opportuno inserire la cartella relativa all'ambiente virtuale all'interno del file `.gitignore`, condividendo esclusivamente il file `requirements.txt`.

### Disattivare l'ambiente

Una volta terminato il lavoro, è opportuno uscire dall'ambiente virutale per tornare a quello globale. Per farlo, possiamo usare il comando `deactivate` da shell.

## Alternativa a `venv`: `conda`

Chiudiamo con un breve riferimetno a `conda`, un gestore di ambienti virtuali molto utilizzato in ambito data science. A differenza di `venv`, che gestisce soltanto i pacchetti Python, Conda è un gestore di pacchetti ed ambienti che può installare anche librerie esterne, come ad esempio le CUDA per il deep learning su GPU NVIDIA. La sintassi da utilizzare in questo caso è leggermente differente, e prevede comandi del tipo:

```bash
conda create --name myenv python=3.10
conda activate myenv
conda install pandas
```

Tuttavia, `venv` rimane lo standard universale per i progetti Python, ed il consiglio è sempre e comunque di partire proprio da quello prima di migrare verso sistemi più avanzati.
