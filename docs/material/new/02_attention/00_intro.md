# Attention

L'attetnion è un concetto ampiamente investigato che è stato spesso usato assieme ad *aropusal*, alertness, ed engagement con l'ambiente circostante.

> In its most generic form, attention coudl be descriebd as merely an overal level of alertness or ability to engage with surroundings.

La *visual* attention è una derelle aree spesso più staudiate sia dalla prospettiva neuroscientifica, sia da quella psicologica.

Quando ad un soggetto viene presentate diverse imagini, i movimenti dell'occhio che il soggetWto effettua possono rilevare le parti *salienti* dell'immagine che attraggono soprattutto la attenzione del soggetto. In questa review dei modelli computazionali per la visual attention, Itti e Koch menzioano che queste parti salienti dell'immagini sono spesso caratterizzate dagli attributi visivi, includendo il contrasto in termini di intensità, gli edge orientati, gli angoli e le giunzioni, ed il movimento. Il cervello umano ATTENDS a queste feature visive salienti a diversi livelli neuronali.

> I neuroni nei primi stage sono adatti a distinguere attributi visuali semplici come contrasto di intensitàò, colori opposti, orientamento, direzione e velcocità del moto, o disparità stereo a diverse scale spaziali. Il tuning dei neuroni diventa sempre più specializzato conla progressione da aree visive a basso livello verso quelle ad alto livello, in modo che le aree visive ad alto livello includono neurono che rispondono solo ad angoli o giunzioni, indizi di forma a partire dall'ombreggiatura, o vie di specifici oggetti nel modndo reale.

E' interessante osservare come diversi soggetti tendono ad esesre attratti alle stesse indizi visivi.

I ricercatori hanno anche scroperto diverse forme di interazione tra la memoria e l'attention. Dal modmento che il cervello umano ha una capacità di memoria limitata, scegliere quali informazioni memorizzare diventa cruciale nell'utilizzo ottimizzato di queste risorse limitate. Il cervello umano lo fa affidandosi all'attention, in modo da memorizzare dinamicamente in memoria l'informazione a cui il soggeetto umano fa più attenzione.

## Attention nel machine learning

Implementare il meccanismo di attention nelle ANN non segue necessariamente i meccanismi biologici e psicologici del cervello umano. INvece, è l'abilità di evidenziare dinameicamente ed usare le parti *salienti* dell'informazione a disposziione - in modo simile a quello del cervello umano - che rende l'attention un concetto così attraente nel machien learning.

Possiamo pensare ai sistemi attention-based come composti di tre componenti (da Deep Learning https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618/ref=sr_1_1?dchild=1&keywords=deep+learning&qid=1622968138&sr=8-1)

* un processo che *legge* i dati raw (come le parole in una frase) e lei converte in rappresentazioni distrib uite, con un vettore delle feature assocaito alla posizione di ognio parola
* una lista di vettori delle feature che contienen l'output del lettore. questo può essere visto come una "memoria" che contiene una sequenza di fatti, che posssoono essere recuperati succeeeviamente, non necessariamente nello stgesso ordine, senza doverli visitare tutti nuovamente
* un processo che sfrutta il contenuto di memoriz per effettuare un task in maniera sequenziale, facendo in modo che ad ogni step temporale ci sia la possibilitàdi inserire l'attention sul contenuitop di un elem,ento di memoria (o di alcuni, con pesi diffeernti)

Vediamo uil framewokr dell'encoder-decoder come esempio, perchè è in questo framework semplcie che venne per la prima volta introdotto il concetto di attention.

Se stiamo elabroando una sequenzza di parole in input, allora questa sarà per prima cosa passata ad un encoder, che darà in output un vettore per ogni elemento nella sequenza., Questo corriosponde al primo compoenmtne del nostro sistema attention-based, come spiegato in precedenza.

Una lista di questi vettori (il secondo compoennte del sistema attention-based dim prima), assieme agli strati nascosti rpecedenti del decoder, sarà sfruttata dal meccanismo di attention per evidenziare in maneira dinamica quale dell'i formazione di input sarà usata per generare l'output.

Ad ogni step temporale, il meccanismo di attention prende quindi lìo stato nascosto precedente del decoder e la slista di vettori codificati, usandoli per generare valori di punteggio non normalizzati che indicano quanto "bene" gli elemenit della sequnza di input si alleneano all'output attuaylele. Dal momento che i valori di punteggio generati devono avere senso (relativamente) in termini di importanza, sono normalizzati passandoli attraverso una funzione softmax per generare i *pesi*. Seguendo la nromalizzazione mediante softmax, tutti i valori di pesi saranno nell'intervallo [0,1] e si sommeranno ad 1, cil che significa che possono essere interpretrati come probabilità. Infine, i vettori codificati sono scalati dai pesi clcolati epr generare un contextg vector. Questo processo di attenzione forma il terzo componente del sikstema attention-based descritto rpecedente,ente,. E' questro context vector che viene quindi mandato nel decoder per genrare un output tradotto: (https://www.frontiersin.org/articles/10.3389/fncom.2020.00029/full)

> Questo tipo di attenzione artriificale è una forma di re-weighting iterativo. Nello specifico, evidenzia dinamneicamente diverse compoennti di un input pre-elaborato man mano che sono necessarie alla generazione dell'output. Questo li rende flessibili e context-dependent, come l'attention biologica.

Il processo implementato da un sistema che incorproa un meccanismo di attention contrasta con uno che non lo comprende. In quest'uyltimo, l'encoder genrea un vettore a lunghezza fissa indipendedntemtne dalla lugnhezza co complessità dell'input. In assenza di unn eccanismo che evidenzia l'informazione saliente lungo l'intero input, il doceoder avrà accesso sotlanto all'informazione linmitata che sarebbe codificata all'interno del vettore a lunghezza fissa. Questo risulta, potnenzialmente, nelf atto che il defcodeder perde informazioni importanti.

Il meccanismo di attention è+ statop inizialmente propsoto per elabroare sequenze di parle nella machine translation, che ha un aspetto temporale intrionscec,. Tuttavia può essere genralizzato per elabroare informazione che può essere statica e non encessariamente correlata in maniera sequenziale, così come nel contesto dell'image proccesing.