https://machinelearningmastery.com/an-introduction-to-recurrent-neural-networks-and-the-math-that-powers-them/ 


When it comes to sequential or time series data, traditional feedforward networks cannot be used for learning and prediction. A mechanism is required to retain past or historical information to forecast future values. Recurrent neural networks, or RNNs for short, are a variant of the conventional feedforward artificial neural networks that can deal with sequential data and can be trained to hold knowledge about the past.

Prerequisites
This tutorial assumes that you are already familiar with artificial neural networks and the backpropagation algorithm. If not, you can go through this very nice tutorial, Calculus in Action: Neural Networks, by Stefania Cristina. The tutorial also explains how a gradient-based backpropagation algorithm is used to train a neural network.

What Is a Recurrent Neural Network
A recurrent neural network (RNN) is a special type of artificial neural network adapted to work for time series data or data that involves sequences. Ordinary feedforward neural networks are only meant for data points that are independent of each other. However, if we have data in a sequence such that one data point depends upon the previous data point, we need to modify the neural network to incorporate the dependencies between these data points. RNNs have the concept of “memory” that helps them store the states or information of previous inputs to generate the next output of the sequence.


# Srotolare la RNN

Una semplice RNN ha un loop di feedback, come mostrato nel primo diagramma della figura precedente. Il feedback loop mostrato nel rettangolo grigio può essere UNROLLED in tre step temporali per produrre la seconda rete della figura precednete... Ovviamente, possiamo variare l'architettura in modo che la rete si srotoli in $k$ step temporali. nella figura, utilizziamo la seguente notazione:

* $x_t \in R$ è l'input allo step temporale $t$. Per mantenere le cose semplici