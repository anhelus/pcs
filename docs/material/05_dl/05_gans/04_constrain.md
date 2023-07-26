# 5.5.4 - Limiti delle GAN

Nel corso del tempo è emerso un certo numero di problemi comuni alle GAN, ai quali i ricercatori hanno provato a porre rimedio proponendo diverse soluzioni, più o meno efficaci.

##### Vanishing gradients

Il problema dei *vanishing gradients* affligge anche le GAN. In particolare, è stato mostrato sperimentalmente come un discriminatore eccessivamente performante comporti una riduzione di performance del generatore: ciò significa che il discriminatore non fornisce informazioni sufficienti per permettere al generatore di progredire nell'addestramento.

Per provare a porre rimedio a questo problema, sono state proposte delle modifiche alla funzione di costo, in particolare con la Wasserstein loss e con la modified minimax loss.

##### Mode collaps

### Mode collaps

Di solito vogliamo fare in modo che la GAN produca un'ampia variretà di output. Ad esempio, potremmo vllere una diversa fasccia per ogni input casuale al nostro generatore.

Tuttavia, se un genratore produce un output molto plausibile, ptorebbe aprpendere a produrre solo quell'output. Infatti, il generatore sta provando sempre a trovare l'poutpuit che sembra più plausibile alò discrimianbtore.

Se il genrator inizia a produrre lo stesso output (o un piccolo insieme di outptu) più e più volte, la strategia migliroe per il discrimiantor è apprendere a respingere sempre questo output. Ma se la successiva generazione di discrimiantore rimane ferma in unminimo locale e non tro vaquesta strtegia ottimale,. alloora è facile per l'iterazione successiva del genrator trovare l'outputm più plausibile per il discirmiantpor attuale.

Ogni iterazione del genrator sovraq-ottimizza per unc erto discrimiantor, e il discrimiantor non può mai uscire da questa "trappola". Come risultato, il genrator rtuota attraverso un piccolo sottoinsieme di outptu. Questa forma di problema è chiamata *mode collapse*.

##### Tentativi di rimedioo

I seguenti approcci provano a forzare il genratore ad ampiare il suo ampbito prevenedno che ottimizzi unsingolop dioscrimiantore fisso.

* Wasserstein loss: questa loss allevia il mdoe collapse facendoci addestrare il dicscriminator in manbeir a ottimale senz apensare ai vanisghin ggradient. Se il discriminator non si ferma in un minimo locale, apprende a respingere l'output su cui si stabilizza il generator. Di conseguenza, il generator deve provare qualcosa di nuovo.
*
 Unrolled GANs: questo tipo di gAN usa una funzione di costo per il genrator che incorpora non solo le classificazioni attuali del discrimiantor, ma anche gli otuptu di future versioni del discrimiantor. Inq eusto modo, il genrator non può sovra-ottiomizzarsi per un singolo discirminator.

 ### FAILURE TO CONVERGE

 Le GAN di solito non riescono a convergere.

 ##### Tentativi di rimedio

 I ricrcatori hanno provato diverse forme di regolarizzazione per migliorare la convergenza delle GAN, inclusi:

 * aggiungere rumoer agli input del discriminator (https://arxiv.org/pdf/1701.04862.pdf)
 * penalizzare i pesi del discriminator (https://arxiv.org/pdf/1705.09367.pdf)

## Varianti delle GAN

I ricercatori continua a trovare delle tecniche migliroate e nuovi usi per le GAN. Ecco degli esempi di variazioni sulle GAN per dare un senso delle possibilità.

### Progressive GAN

In una progressive GAN, i primi layer del generator producono immagini a risoluzione bassa, e i layer successivi vi aggiungono dettagli. Questa tecnica permette alle GAN di addestrarsi più velocemente rispetto alle GAN non-progressive equivalenti, e producono immagini a più alta risoluzione. https://arxiv.org/abs/1710.10196

### Conditional GAN

Le Conditional GAN si addestrano su un dataset labellizato e ci permettono di specificare l'etichetta per ogni istanza generata. PEr esempio, una MNIST GAN non condizionale produrrebbe cifre casuali, mentre una MNIST GAN ci permette di specificare quale cifra la GAN dovrebbe generare.

Invece di modellare la probabilità congiunta $P(X, Y)$, le conditional GAN modellano la probabilità condisionale $P(X|Y)$. (https://arxiv.org/abs/1411.1784)

### Image-to-Image translation

Le image-to-image trnalsation GAN prendoono un'mmagine in input e la mappano su un output generato con diverse proprietà. POer esempio, posisamo fare una maschera di un'auto, e la GAN la può riempire con dettagli fotorealistici.

In questo caso, la loss è una combinazione pesata della normale loss discriminator-based e di una loss pixel-wise che penalizza il genratore per distanziarsi dall'immagine sorgente. (https://arxiv.org/abs/1611.07004)

### CycleGAN

Una CycleGAN apprende a trasformare immagini da un insieme nelle immagini che possono plausibilmente appartenere ad un altro insieme. Ad esempio, una CycleGAN produce l'mmagine di destra con l'immagine di sinistra come input. Prende un'immagine di un cavallo e la trasforma in un'immagine di una zebra.

CYCLEGAN

I dati di addestramento per una CycleGan sono semplicemente due insiemi di immagini (in questo caso, un insieme di immagini di cavallo ed un insieme di immagini di zebra). Il sistema non richiede label o corrispondenze a coppie tra le immagini. (http://openaccess.thecvf.com/content_ICCV_2017/papers/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.pdf)

### Text-to-Image Synthesis

Le text-to-image GAN prendono delt esto e producono immagini che siano plausibili e descritte dal testo. Per esempio, l'immagine sottostante è stata prodotta fornendo una descrizione testaule ad una GAN.

TEXT2IMG

Notiamo che in questo sistema la GAN può produrre immagini solo da un set di classi limitato. https://arxiv.org/abs/1612.03242

### Super resolution

Le Super Resolution GAN aumentano la risoluzione dlel eimmagini, aggiungendo dettagli dove necessario per riempire le aree sfocate. Per esempio, l'immagine sfocata nel mezzo è una versione sottocampionata di quella oriignaria a sinista. Data l'immagine sfocata, unaGAN è in grado di produrre l'immagine più nitida a destra.

SUPERRES_BLURRY

L'immagine genrata dalla GAN appare molto simile a quella originaria, ma se guardiamo più vicino vedremo che la GAN non è stata in grado di riprodurre alcuni dettagli dell'originiale. Invece, ha fatto un pattern plausibile per rimpiazzare il pattern cancellato dal sottocampionamento. https://arxiv.org/pdf/1609.04802.pdf

### Face inpainting

https://arxiv.org/pdf/1607.07539.pdf

Le GAN sono state usate per il task di semantic image inpaining. IN questo task, i chunk di un'immagine vengono anneriti, e il sistema prova a ricoloralri.


https://colab.research.google.com/github/tensorflow/gan/blob/master/tensorflow_gan/examples/colab_notebooks/tfgan_tutorial.ipynb?utm_source=ss-gan&utm_campaign=colab-external&utm_medium=referral&utm_content=tfgan-intro 

INPAINTING_OUT
