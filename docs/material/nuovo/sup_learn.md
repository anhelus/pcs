Diversi modelli di NLP hanno mostrato


# Self-Supervised Representation Learning

L'apprendimento supervisionato può risolvere un task con un certo numero di label. Una buona performance richiede di solito un buon numero di label, ma etichettare manualmente un dataset può essere costoso e difficilmente scalabile. Infatti, se consideriamo che il quantiativo di dati non etichettati (ad esempio, le immagini su Internet) è enormemente maggiore a quello che un numero limitato di umani può etichettare, è limitante non sfruttarli. Tuttavia, l'apprendimento supervisionato non è semplice, e spesso è molto meno efficiente dell'apprendimento superivisionato.

E se fosse possibile ottenere le label per dati non etichettati, ed addestrare un dataset non superivsionato in maniera supervisionata? POssiamo ottenere questo ponendo un task di apprendimento supervisionato in una forma speciale, in modo da predire solo un sottoinsieme di informazioni usando le restatne. In questo modo, tutte le informazioni necessarie, sia gli input, sia le label, sono fornite. Questo processo è conosciuto come self-supervised learning.

L'idea è stata ampiamente utilizzata nel language modeling. Il task di defautl per un language model è predire la parola successiva data la sequenza del passato. BERT aggiunge due altri task ausiliari e si affidano entrambi a label auto-generate.

### Perché self-supervised learning?

Il self-supervised learning ci permette di sfruttare una varietà di label che vengono con i dati in maniera "gratuita". Il motivo è molto semplice: produrre un dataset con label "pulite" è costoso, ma dati non etichettati vengono generati in continuazione. Per far uso di questo grosso quantitativo di dati non etichettati, un modo è impostare gli obiettivi di learning in maniera appropriata, in modo da ottenere una supervisione a partire dai dati stessi.

Il task self-supervisied, anche conosciuto come *pretext task*, ci guida verso una funzione di costo supervisionata. Tuttavia, nonn ci occupiamo norlmanete delle performance finale di questo task. Piuttosto, siamo interessati nella rappresentazione intermedia appresa, con l'aspettazione che questa rappresentazione possa ottenere una buona semantica o significato strutturale, e possa beneficiare di una varietà di task pratici.

Ad esempio, potremmo ruotare arbitrariamente un'immagine,e d addestrare un modello a predire come ogni immagine di input viene ruotata. Il task di predizione di una rotazione è un task inventato, per cui l'accuracy effettiva non è importante. Ma ci aspettiamoc he il modello apprenda delle variabili latenti ad alta qualità per i task del mondo reale, come la costruzione di un classificatore per la object recognition con molto pochi campioni etichettati.

In senso ampio, tutti i modelli generativi possono essere considerati come self-supervised, ma con diversi obiettivi. I modelli generativi si focalizzno sulla creazione di immagini diverse e realistiche, mentre quelli self-supervised si occupano di produrre delle buone feature che siano generalmente utili per diverse task.

### Images-based

Molte idee sono state proposte per il sel