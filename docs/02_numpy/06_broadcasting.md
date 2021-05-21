alle volte possiamo voler effettuare un'operazione tra un array ed un singolo numero (chiamata anche operazione tra vettore e scallare) o tra array di diverse dimensioni. Ad esempio, il nostro array (che chiameremo data) contiene infimazioni sulla distanza in miglia, ma vogliamo convertire l'informazioni in chilometri. POssiamo far questa operazione ocn:

>>> data = np.array([1.0, 2.0])
>>> data * 1.6
array([1.6, 3.2])

Numpy comprende che la moltiplicazione deve avvenire all'interno di ogni c ella. Questo concetto è chiamato *broadcasting*. Il broadcasting è un meccanismo che permette a NumPy di efettuare operazioni su array di diverse forme. Le dimensioi del nostro array devono essere compatibili, per esempio, quando le dimensioni di entrambi gli array sono uguali, o quando una di queste è unitaria. Se le dimensioni non sono compatibili, avremo un ValueError.