# Visualizzare i dati con Matplotlib (e Seaborn)

Finora ci siamo limitati a visualizzare dati e risultati usando esclusivamente la riga di comando. Evidentemente, però, questo non è il modo ottimale di procedere: cosa ne è, infatti, di tutti quei coloratissimi grafici che si vedono in giro? In realtà, visualizzarli è abbastanza semplice: abbiamo bisogno, infatti, di integrare il nostro ambiente con delle altre librerie, ovvero *Matplotlib* e, opzionalmente, *Seaborn*.

## Matplotlib

### Installazione

Partiamo proprio da *Matplotlib*, che è probabilmente la più usata tra le librerie disponibili per la visualizzazione dati. Iniziamo installandola all'interno del nostro ambiente di lavoro:

==="Pip" 
	```sh
	pip install matplotlib
	```
==="Pipenv"
	```sh
	pipenv install matplotlib
	```

Nel prosieguo, presupporremo che siano stati effettuati gli import necessari, riassumibili nelle seguenti istruzioni:

```py
import numpy as np
import matplotlib.pylot as plt
```

### Il primo plot

Una volta installata Matplotlib, proviamo a creare il nostro primo plot. Per farlo, apriamo il nostro solito terminale Python, ed inseriamo le seguenti istruzioni:

```py
rng = np.random.default_rng(42)
x = np.arange(1, 6)
y = rng.integers(low=0, high=10, size=5)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

Se tutto è andato per il verso giusto, dovremmo vedere a schermo un'immagine simile a questa (data la natura casuale di `y`):

![first_plot](../assets/images/03_libs/01_matplotlib/first_plot.png){: .center}

A questo punto, è arrivato il momento di descrivere maggiormente nel dettaglio ciò che abbiamo fatto.

### Figure, assi ed artisti

Alla base del funzionamento di Matplotlib abbiamo quattro classi fondamentali.

Per prima cosa, ci sono le `Figure`, che rappresentano l'intera *figura* mostrata da Matplotlib. Questa, ovviamente, terrà traccia di tutto ciò che vi è al suo interno, e potrà contenere un numero arbitrario degli elementi che vedremo a breve.

Abbiamo poi gli `Axes`, oggetti che rappresentano il plot vero e proprio, ovvero la regione dell'immagine all'interno del quale vengono "disegnati" i dati. La relazione tra `Figure` ed `Axes` è strettamente gerarchica: una `Figure` può avere diversi `Axes`, ma ogni `Axes` appartiene esclusivamente ad una `Figure`.

All'interno di un oggetto `Axes` troviamo poi due o tre oggetti di tipo `Axis`, ognuno dei quali rappresenta l'asse vero e proprio (in altri termini, $x$, $y$ e, per le figure tridimensionali, $z$). Gli oggetti `Axis` ci permettono quindi di definire gli intervalli dati, l'eventuale griglia, e via discorrendo.

!!!warning "Attenzione"
	Fate attenzione a non confondere gli `Axes` con gli `Axis`, nonostante l'infelice scelta dei nomi!

In ultimo, abbiamo gli *artist*, che rappresentano *tutto* quello che è possibile visualizzare su una figura, incluso testo, label, plot, numeri, e via discorrendo.

Torniamo brevemente al precedente snippet. Dopo aver importato i package necessari, ed aver creato un vettore di numeri interi casuali, abbiamo creato una `Figure` ed un `Axes` usando la funzione `subplots()`:

```py
fig, ax = plt.subplots()
```

A quel punto, abbiamo effettuato il plot dei valori di `x` ed `y` su nostro oggetto `Axes`:

```py
ax.plot(x, y)
```

In ultimo, abbiamo mostrato a schermo la figura usando la funzione `plt.show()`.

Vediamo qualche esempio più "corposo".

### Esempio 1: Plot di più funzioni

In questo esempio, vogliamo mostrare sullo stesso `Axes` il plot di due diverse funzioni, in particolare una retta ed un seno. Ricordiamo che questo è possibile grazie al fatto che i plot vengono considerati degli artist, e quindi è possibile inserirne un numero arbitrario.

Vediamo come fare. Per prima cosa, definiamo i nostri dati:

```py
x = np.arange(0., 10., 0.01)
y_1 = 1 + 2 * x
y_2 = np.sin(x)
```

Notiamo che stiamo usando un unico vettore per le ascisse, di modo da fornire una base comune al nostro plot. Adesso, creiamo la nostra `Figure` con relativo `Axes`, ed effettuiamo il plot di entrambe le funzioni.

```py
fig, ax = plt.subplots()
ax.plot(x, y_1)
ax.plot(x, y_2)
```

Possiamo impostare il titolo e le label sugli assi $x$ ed $y$ usando rispettivamente le funzioni `set_title`, `set_xlabel` e `set_ylabel`:

```py
ax.set_title('Plot di due funzioni matematiche')
ax.set_xlabel('Asse x')
ax.set_ylabel('Asse y')
ax.grid()
```

Abbiamo anche usato la funzione `grid()` per far apparire una griglia sulla figura. In ultimo, possiamo plottare a schermo la figura con la funzione `show()`:

```py
plt.show()
```

Il risultato ottenuto è mostrato in figura.

![simple_plot](../assets/images/03_libs/01_matplotlib/simple_plot.png){: .center}

### Esempio 2: Subplot

Abbiamo detto che possiamo definire più `Axes` per un'unica `Figure`; per farlo, possiamo parametrizzare la funzione `subplots(i, j)`, in maniera tale che vengano creati $i \times j$ plot all'interno della stessa figura.

Per creare 2 subplot in "riga", ad esempio, usiamo questa istruzione:

```py
fig, (ax_1, ax_2) = plt.subplots(2, 1)
```

Possiamo poi usare la funzione `suptitle()` per dare un titolo all'intera figura:

```py
fig.suptitle('Due subplot di più funzioni matematiche')
```

A questo punto, procediamo ad effettuare i plot sui relativi assi nella solita maniera:

```py
# Primo subplot
ax_1.plot(x, y_1)
ax_1.set_ylabel('Asse y')
ax_1.grid()
# Secondo subplot
ax_2.plot(x, y_2)
ax_2.set_xlabel('Asse x')
ax_2.set_ylabel('Asse y')
ax_2.grid()
# Mostro la figura
plt.show()
```

Il risultato sarà simile a quello mostrato in figura:

![multi_subplot](../assets/images/03_libs/01_matplotlib/multi_subplots.png){: .center}

### Esempio 3: Rappresentazione di un istogramma

Abbiamo già parlato degli istogrammi in precedenza. Tuttavia, la loro vera potenza sta nella rappresentazione visiva che offrono, ed in tal senso Matplotlib ci viene in soccorso offrendoci la funzione `hist`.

Per prima cosa, creiamo un vettore di interi.

```py
x = rng.integers(low=0, high=100, size=1000)
```

Al solito, creiamo la nostra figura, ed usiamo la funzione `hist` passandogli il vettore `x` creato in precedenza ed il parametro `density`, che ci permetterà di normalizzare l'istogramma (ovvero, fare in modo tale che la sommatoria dei singoli bin sia esattamente pari ad 1).

```py
fig, ax = plt.subplots()
ax.hist(x, density=True)
```

Al solito, usiamo i metodi opportuni per impostare titolo e label degli assi, e mostriamo la figura.

```py
ax.set_xlabel('Bin')
ax.set_ylabel('Conteggio dei singoli elementi')
ax.set_title('Esempio di istogramma')

plt.show()
```

Il risultato sarà simile a quello mostrato nella figura successiva.

![hist](../assets/images/03_libs/01_matplotlib/hist.png){: .center}

### Esempio 4: Plot tridimensionale

Concludiamo questa breve carrellata mostrando un esempio di plot a tre dimensioni. Questa volta, dovremo passare alla funzione `subplots` l'argomento `'projection': '3d'`, per indicargli che il plot ha tre assi al posto dei soliti due.

```py
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
```

Creiamo i nostri dati, avendo cura di usare la funzione `meshgrid()` per creare una griglia rettangolare a partire dai valori iniziali degli array `x` ed `y`, grazie a cui potremo poi creare la figura tridimensionale vera e propria.

```py
x = np.arange(-10, 10, 0.25)
y = np.arange(-5, 15, 0.25)
x, y = np.meshgrid(z, y)
z = np.cos(np.sqrt(x**2 + y**2))
```

A questo punto, usiamo la funzione `plot_surface()` per plottare i tre assi, impostiamone il titolo e mostriamo l'immagine a schermo.

```py
ax.plot_surface(x, y, z)
ax.set_title('Un esempio di plot tridimensionale')
plt.show()
```

Il risultato che otterremo sarà simile a questo.

![3d](../assets/images/03_libs/){: .center}

## Seaborn

Seaborn è una libreria che *estende* Matplotlib, integrando diverse opzioni e funzionalità a quelle già esistenti. Vediamo rapidamente un esempio.

### Installazione

Per prima cosa, installiamo la libreria nel modo usuale:

==="Pip" 
	```sh
	pip install seaborn
	```
==="Pipenv"
	```sh
	pipenv install seaborn
	```

Importiamo poi Seaborn nel nostro script:

```py
import seaborn as sns
```

### Esempio: Heatmap

La sintassi usata da Seaborn è molto simile a quella usata da Matplotlib, con qualche piccola ed ovvia differenza. 

Una funzione molto utile è quella che ci permette di visualizzare le *heatmap*, che ci permettono di visualizzare rapidamente i valori in diversi tipi di matrici, come ad esempio quelle di correlazione (o, come vedremo più avanti, quelle di confusione). Questa funzione, quasi "banalmente", è chiamata `heatmap()`, e richiede almeno un parametro in ingresso, rappresentativo della matrice da cui sarà estratta la figura:

```py
a = rng.integers(low=0, high=100, size=(20, 20))
coeff = np.corrcoef(a)
fig, ax = plt.subplots()
sns.heatmap(corr)
plt.show()
```

Il risultato che otterremo sarà simile a questo:

![heatmap](../assets/images/03_libs/01_matplotlib/heatmap.png){: .center}

## Conclusioni

In questa lezione, abbiamo dato una panoramica su due delle librerie più usate per la visualizzazione dei dati in Python. Nella prossima lezione, toccheremo brevemente un'altra libreria, molto usata soprattutto in ambito scientifico, ovvero [SciPy](./02_scipy.md).
