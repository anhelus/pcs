trasposta

un'operazione comune è fare la trasporta delle nostre matrici. gli array numpy hanno la proprietà T che ci permette di trasporre una matrice.

si può anche dover cambiare le dimensioni di una matrice. questo può accadere quando, ad esempio, si ha un modello che si attende una certa forma di input che è diversa dal nostro dataset. questo è dove il meotodo reshape può essere utile. abbiamo infatti bisogno semplicemente di passare le nuove dimensioni che vogliamo per la matrice.

>>> data.reshape(2, 3)
array([[1, 2, 3],
       [4, 5, 6]])
>>> data.reshape(3, 2)
array([[1, 2],
       [3, 4],
       [5, 6]])




reshaping

inversa

reshaping and flattening