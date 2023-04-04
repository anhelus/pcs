# YOLO

## Introduzione alla Object Detection

La *object detection* è una tecnica usata in ambito di computer vision per l'identificazione e la localizzazione di oggetti all'interno di un'immagine o di un video.

La localizzazione è il processo di identificare la posizione corretta di uno o più oggetti usando delle bounding box, che corrispondono o rectangular shapes around the objects. 

This process is sometimes confused with image classification or image recognition, which aims to predict the class of an image or an object within an image into one of the categories or classes. 

The illustration below corresponds to the visual representation of the previous explanation. The object detected within the image is “Person.” 

In this conceptual blog, you will first understand the benefits of object detection, before introducing YOLO, the state-of-the-art object detection algorithm. 

In the second part, we will focus more on the YOLO algorithm and how it works. After that, we will provide some real-life applications using YOLO. 

The last section will explain how YOLO evolved from 2015 to 2020 before concluding on the next steps. 

## Cosa è YOLO?
You Only Look Once (YOLO) is a state-of-the-art, real-time object detection algorithm introduced in 2015 by Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi in their famous research paper “You Only Look Once: Unified, Real-Time Object Detection”. 

The authors frame the object detection problem as a regression problem instead of a classification task by spatially separating bounding boxes and associating probabilities to each of the detected images using a single convolutional neural network (CNN). 

Some of the reasons why YOLO is leading the competition include its:

Speed 
Detection accuracy 
Good generalization 
Open-source
1- Speed
YOLO is extremely fast because it does not deal with complex pipelines. It can process images at 45 Frames Per Second (FPS). In addition, YOLO reaches more than twice the mean Average Precision (mAP) compared to other real-time systems, which makes it a great candidate for real-time processing. 

From the graphic below, we observe that YOLO is far beyond the other object detectors with 91 FPS.

2- High detection accuracy
YOLO is far beyond other state-of-the-art models in accuracy with very few background errors. 

3- Better generalization
This is especially true for the new versions of YOLO, which will be discussed later in the article. With those advancements, YOLO pushed a little further by providing a better generalization for new domains, which makes it great for applications relying on fast and robust object detection. 

For instance the Automatic Detection of Melanoma with Yolo Deep Convolutional Neural Networks paper shows that the first version YOLOv1 has the lowest mean average precision for the automatic detection of melanoma disease, compared to YOLOv2 and YOLOv3.

4- Open source 
Making YOLO open-source led the community to constantly improve the model. This is one of the reasons why YOLO has made so many improvements in such a limited time. 

## Architettura di YOLO

L'architettura di YOLO prende spunto da quella di GoogleNet. Ha 24layer convoluzionali, quattro layer di max-pooling, e due layer completamente connessi.

L'architettura funziona come segue:

* l'immagine di input viene ridimensionata a $448 \times 448$ peima di andare nella rete convoluzionale
* una convoluzione $1 \times 1$


he architecture works as follows:

Resizes the input image into 448x448 before going through the convolutional network.
A 1x1 convolution is first applied to reduce the number of channels, which is then followed by a 3x3 convolution to generate a cuboidal output.
The activation function under the hood is ReLU, except for the final layer, which uses a linear activation function.
Some additional techniques, such as batch normalization and dropout, respectively regularize the model and prevent it from overfitting.
By completing the Deep Learning in Python course, you will be ready to use Keras to train and test complex, multi-output networks and dive deeper into deep learning.

How Does YOLO Object Detection Work?
Now that you understand the architecture, let’s have a high-level overview of how the YOLO algorithm performs object detection using a simple use case.

“Imagine you built a YOLO application that detects players and soccer balls from a given image. 

But how can you explain this process to someone, especially non-initiated people?

 → That is the whole point of this section. You will understand the whole process of how YOLO performs object detection; how to get image (B) from image (A)”

Il funzionamento dell'algoritmo è legato a questi quattro step:

##### 1. Residual blocks

Il primo step di YOLO inzia dividendo l'immagine originaria $A$ in una cella di $N \times N$ griglie di ugual forma. Ogni cella nella griglia è quindi repsonsabile per la localizzazione e predizione della classe dell'oggetto che copre, assieme ai valori di probabilità e confidenza. 

##### 2. Bounding box regression

Il passo successivo è determinare i bounding box che corrisponde ai rettangoli che evidenziano tutti gli oggetti nell'immagine. POssiamo avere tante bounding box quanti sono gli oggetti in una data immagine.

YOLO determian gli attributi di questi bouniding box usando un singolo modulo di regressione nel seguente formato:

$$
Y=[pc, bx, by, bh, bw, c1, c2]
$$

dove:

* $Y$ è la rappresentazione integrale per ciascun bounding bxo;
* $p_c$ corrisponde al punteggio di probabilità della griglia contentente un oggetto. Ad esempio, tutte le griglie rosse avranno un punteggio di probabilità più alto di zero.
* $b_x, b_y$ sono le coordinate $x$ ed $y$ del centro delle bounding box rispetto alla griglia che le contiene.
* $b_h, b_w$ corrispodnono all'altezza ed all'ampiezza della bounding box rispetto alla griglia che la contiene.
* $c_1$ e $c_2$ corrispondono alle classi del nostro caso d'uso.

TODO ESEMPIO

##### 3. Intersection Over Unions o IoU

La maggior parte delle volte, un singolo oggetto in un'immagine può avere più box candidate per la predizione, anche se non tutti sono rilevanti. L'obiettivo della IoU (valore tra 0 ed 1) è scartatere queste box e mantenere solo quelle rilevanti. La logica dietro a questo è la seguente:

* l'utente definisce la soglia di selezione della IoU, ad esempio, 0.5
* YOLO quindi calcola la IoU di ogni cella che è l'area dell'intersezione divisa da quella dell'unione
* infine, ignora le predizioni di ogni cella che ha una IoU minore o uguale alla soglia, e consiedera quella con una IoU maggiore della soglia.

TODO ESEMPIO

##### 4. Non-Max Suppression

Impostare una soglia per la IoU non è sempre abbastanza perché un oggetto può avere più box con una IoU al di sotto della soglia, e lasciare queste box può includere del rumore. Possiamo usare la NMS per mantenere solo le box con la probabilità di detection più alta.

## Differenze tra diverse versioni di YOLO

Dalla prima release di YOLO, si sono evolute molte versioni.

##### YOLOv1

La prima versione di YOLO ha migliorato di molto la object detection, grazie alla sua abilità di riconoscere gli oggetti in maniera rapida ed efficienzte.

Tuttavia, come moltre altre soluzioni, la prima versione di YOLO ha i suoi limiti:

* ci sono problemi nell'individuare immagini di piccola dimensione all'interno di un insieme di immagini, come un gruppo di persone in uno stadio. Questo è perché ogni griglia nell'archietttura YOLO è progettata per individuare un singolo oggetto.
* YOLO non è in grado di individuare forme nuove o inusuali
* infine, la funzioen di costo usata per approssimare le pefromance di detection tratta gli errori su bounding box piccole e grandi allo stesso modo, il che crea delle localizzazioni imperfette.

##### YOLOv2 (YOLO9000)

https://www.datacamp.com/blog/yolo-object-detection-explained

YOLOv2 è stato creato nel 2016.

I miglioramenti includono l'uso di Darknet-19 come nuova architettura, batch normalization, risoluzione degli input più alta, layer convoluzionali con delle anchor, clustering, e fine-grained features.

YOLOv2 usa una risoluzione di $448\times 448$ invece di $224 \times 224$, il che rende il modello in grado di modificare i suoi filtri in modo da agire meglio su immagini a più alta risoluzione. Questo approccio aumenta l'accuracy del 4% mAP, dopo il training di 10 epoche sui dati di ImageNet.

* INvece di predire le coordinate esatte delle bounding box degli oggetti come YOLOv1, YOLOv2 semplifica il problema rimpiazzando i layer completamente connessi con delle anchor box. Questo approccio decrementa leggeremnte l'accuracy, ma migliora il recall del modello.
* Le anchor boxes sono trovate in automatico da YOLOv2 usando il k-means con $k=5$ invece di effettuare una selezione manuale. Questo approccio fornisce un buon compromesso tra il recall e la precsione del modello.
* le predizioni YOLOv2 p


## YOLOv8

YOLOv8 definisce una nuova architettura allo stato dell'arte per la [object detection](object_detection.md) e per la [instance segmentration](image_segmentation.md).

YOLOv8 è il nuovo modello allo stato dell'arte, sviluppato da Ultralytics, gli stessi che hanno creato il modello YOLOv5. YOLOv8 include diversi migliramenti rispetto ad YOLOv5.

La serie di modelli YOLO (You Only Look Once) è diventata famosa nel mondo della computer vision. La fama di YOLO è attribuile alla sua considerevole accuratezza, ottenibile mantenendo comunque una dimensione ridotta del modello. I modelli YOLO possono essere addestrati su una GPU singola, il che li rende accessibili ad un ampio range di sviluppatori, e deployabili su edge o nel cloud.

YOLO è stato al centro dell'attenzione della computer vision fin dal suo lancio nel 2015 da Joseph Redmond, che lo manteneva in codice C in un framweork scritto da Redmond stesso e chiamato Darknet.

L'autore di YOLOv8, Glenn Jocher, ha usato come base la repository di YOLOv3 in PyTorch. Da qui, Ultralytics alla fine ha lanciato il suo primo modello, ovvero YOLOv5.

YOLOv5 


https://blog.roboflow.com/whats-new-in-yolov8/ 