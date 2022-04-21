# iPython e Jupyter Lab

Fino a questo momento, ci siamo limitati ad utilizzare la riga di comando, con solo i più "audaci" che si saranno avventurati nell'esecuzione di interi script da riga di comando.

Appare però evidente come questo modo di procedere sia limitato (e limitante). Non sarebbe meglio avere un ambiente di sviluppo *interattivo*, nel quale inserire le nostre istruzioni allo scopo di visualizzare rapidamente i risultati ottenuti e, se necessario, modificarle al volo? Beh, è questo quello che devono aver pensato gli sviluppatori della libreria iPython, anch'essa facente parte del framework SciPy, quando hanno lanciato il progetto *Jupyter Lab*, precedentemente conosciuto soltanto come *Jupyter*, introducendo uno degli strumenti più usati dai data analyst al giorno d'oggi, ovvero i *notebook*.

## Cosa è un notebook?

Un notebook è, in parole povere, un ambiente interattivo che permette di scrivere e testare il nostro codice. In particolare, potremo scrivere una o più istruzioni ed eseguirle in maniera separata (ma non *indipendente*) dalle altre mediante il meccanismo delle *celle*, che altro non sono che singoli blocchi di codice. Potremo inoltre inserire commenti, descrizioni ed equazioni usando due linguaggi di markup molto noti, ovvero Markdown e Latex.

Vediamo brevemente come creare ed usare un notebook.

## Installazione e lancio di Jupyter Lab

Per prima cosa, installiamo Jupyter Lab nel nostro ambiente di sviluppo.

==="Pip" 
	```sh
	pip install jupyterlab
	```
==="Pipenv"
	```sh
	pipenv install jupyterlab
	```

A differenza delle altre librerie, non avremo bisogno di importare Jupyter; tuttavia, dovremo lanciare l'ambiente interattivo mediante il seguente comando:

==="Pip" 
	```sh
	jupyter lab
	```
==="Pipenv"
	```sh
	pipenv run jupyter lab
	```

## Il primo notebook

A questo punto saremo davanti ad una schermata molto simle a quella mostrata in figura.

![intro](../assets/images/03_libs/03_jupyter/intro.png){: .center}

Creiamo il nostro primo notebook premendo il pulsante *Python 3* nel menu *Notebook*. Una volta terminata la procedura, potremo iniziare ad interagire con l'ambiente. Prima di procedere, però, definiamo il nome del nostro notebook dal menu a sinistra.

Proviamo a fare qualcosa di semplice: importiamo NumPy e Matplotlib, creiamo un array di numeri casuali, e facciamone il plot a schermo. Per prima cosa, all'interno della prima cella, definiamo gli import:

```py
import numpy as np
import matplotlib.pyplot as plt
```

Per eseguire il codice all'interno della cella, premiamo il tasto `Play`, oppure la combinazione di tasti `Shift+Invio`. Una volta eseguita la prima cella, vedremo che nel notebook se ne sarà creata un'altra; al suo interno, scriviamo le istruzioni necessarie alla creazione di un array casuale.

```py
a = np.random.randint(0, 100, (5))
a
```

Eseguiamo l'istruzione; noteremo che al di sotto della cella è apparso a schermo l'array che abbiamo appena creato. *Se provassimo ad eseguire nuovamente il codice nella cella, vedremmo che l'array assumerebbe un nuovo valore*.

Ed è proprio questa la forza di Jupyter: la capacità di eseguire singole celle, cambiando di volta in volta valori ed algoritmi, e facilitando in questo modo le nostre prove e test.

A questo punto, possiamo creare un'ultima cella, e stampare a schermo il nostro vettore:

```py
fig, ax = plt.subplots()

ax.plot(np.arange(1, 6), a)
```

![sample](../assets/images/03_libs/03_jupyter/sample.png){: .center}

Vedremo immediatamente sotto la cella la figura rappresentativa del vettore che abbiamo creato.

### Commenti in Latex e Markdown

Accennavamo prima al fatto che fosse possibile inserire dei commenti e delle descrizioni nei linguaggi Markdown e Latex. Per farlo, ci basta selezionare il menu a tendina in alto, ed al posto di `Code` specificare un'altra opzione. Se volessimo aggiungere una descrizione al nostro notebook, ad esempio, potremmo aggiungere una cella in alto e scrivere il seguente codice:

```markdown
# Header

Una breve descrizione.
```

### Cancellare una cella

Possiamo anche decidere di cancellare una cella; per farlo, selezioniamola e premiamo due volte il tasto `D`, oppure andiamo dal menu `Cell` e selezioniamo l'apposita opzione.

### Bonus: Estensioni

E' possibile abilitare una serie di estensioni a partire dal menu indicato nella seguente immagine.

![sample](../assets/images/03_libs/03_jupyter/extensions.png){: .center}

!!!tip "Suggerimento"
	Esistono delle estensioni per la visualizzazione delle variabili in stile Matlab. Tuttavia, è plausibile che sorgano delle problematiche di compatibilità con le ultime versioni di Jupyter Lab.

## Conclusioni

In questa lezione, abbiamo brevemente visto come creare e manipolare un notebook in Jupyter. Dalla prossima, sarà questa la modalità con cui agiremo per mostrare e testare il nostro codice.
