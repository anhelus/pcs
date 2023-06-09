# E27 - Convolutional Neural Networks in TensorFlow e Keras

## Esercizio E27.1

Creare un modello di rete neurale composto in questo modo:

```bash
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv_1 (Conv2D)             (None, 30, 30, 32)        896       
                                                                 
 pooling_1 (MaxPooling2D)    (None, 15, 15, 32)        0         
                                                                 
 conv_2 (Conv2D)             (None, 13, 13, 32)        9248      
                                                                 
 dropout (Dropout)           (None, 13, 13, 32)        0         
                                                                 
 flatten (Flatten)           (None, 5408)              0         
                                                                 
 classification (Dense)      (None, 10)                54090     
                                                                
_________________________________________________________________
```

Questo modello deve essere in grado di classificare le immagini presenti nel dataset [CIFAR10](https://keras.io/api/datasets/cifar10/).

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).
