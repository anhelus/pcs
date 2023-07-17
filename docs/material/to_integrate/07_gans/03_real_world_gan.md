# Problemi Comuni

Le GAN ha nno un certo nuemmro di problemi comuni. Tutti questi sono aree di ricerca attiva. Anche se nessunod iqeusti problemi è stato completamente risolto, vedremo alcuned elle soluzioni proposte.

### Vanishing gradients

La ricerca suggerisce che se il discriminator è troppo buono, l'adedestreamento del genrator può falire a causa del vanishing gradient. In effetti, un discrimioantore ottimale non fornisce abbastanza informazioni al generator per fare progressi.

##### Tentativi di rimedio

* Wasserstei loss: questa loss è progettata per previnrei i vanishgin gradient anche quando addestriamo il discriminator in maniera ottimale.
* modified minimax loss: il paper originale epr le GAN propose una modifica alla minimax loss per affrontare il vanishign gradient.

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