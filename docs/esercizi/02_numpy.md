# Esercizi su NumPy

1. Definire una funzione `svd_rec(u, v, sigma)` che, dati i valori di $U$, $V$ e $\Sigma$ ottenuti dalla decomposizione ai valori singolari di una matrice $A$ permetta di ricostruire quest'ultima. Implementare gli opportuni controlli per valutare la coerenza dei parametri passati in ingresso, e definire uno script in grado di scomporre e ricomporre una generica matrice $A$.

2. Trovare il minimo ed il massimo di un array usando soltanto cicli.

3. E' possibile caratterizzare i dati di una distribuzione in maniera non parametrica specificando i valori del *range interquartile* (ovvero il numero di elementi che ricadono tra il 25 ed il 75 percentile), la *mediana* e la *deviazione standard*. Scrivere una funzione che accetti un vettore in ingresso e restituisca in uscita questi valori sotto forma di dizionario.