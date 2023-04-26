# Esercitazione 2.1 - NumPy

## Esercizi sugli array

### Esercizio 2.1.1

Scrivere una funzione che restituisca il prodotto *riga per colonna* di due vettori `v1` e `v2`. Utilizzare in primis una list comprehension, verificando anche che la lunghezza dei due vettori sia coerente. Valutare inoltre il tempo necessario all'esecuzione utilizzando la libreria [`time`](https://docs.python.org/3/library/time.html).

Effettuare la stessa operazione in NumPy, valutando contestualmente il tempo necessario in entrambi i casi.

### Esercizio 2.1.2

Scrivere la funzione `crea_array(dim_1, dim_2, val_min, val_max)` che crea array di dimensione arbitraria `dim_1` $\times$ `dim_2` composti da numeri interi casuali compresi tra `val_min` e `val_max`. Di default, la funzione dovrà creare dei vettori riga. Utilizzare il package [`random`](https://docs.python.org/3/library/random.html).

Provare ad effettuare la stessa operazione in NumPy.

### Esercizio 2.1.3

Scrivere la funzione `rettifica(array)` che restituisce un array analogo a quello in ingresso, ma con tutti i valori negativi "rettificati" a $0$.

## Esercizi sulle operazioni algebriche

### Esercizio 2.1.4

Verificare che il prodotto tra una matrice invertibile e la sua inversa sia la matrice identità.

### Esercizio 2.1.5

Scrivere la funzione `calcola_determinante()` che accetta come parametro in ingresso una matrice $2 \times 2$ e ne calcola il determinante. Gestire opportunamente il caso in cui la matrice in ingresso sia difforme dalle indicazioni fornite in precedenza, o che non la matrice non sia invertibile.

### Esercizio 2.1.6

Scrivere la funzione `inverti_se_invertibile(mat)` che, data una matrice bidimensionale, restituisca l'inversa soltanto se `mat` è bidimensionale, quadrata, e il determinante è diverso da zero. Utilizzare un'unica istruzione condizionale.

## Esercizi sulle operazioni polinomiali in NumPy

### Esercizio 2.1.7

Scrivere la funzione `somma_polinomi()` che accetta come parametri due polinomi di grandezza arbitraria, sommandoli tra loro. Trattiamo i polinomi come liste; in particolare, all'$i$-mo elemento della lista corrisponderà il coefficiente di $i$-mo grado del polinomio.

### Esercizio 2.1.8

Usare una lista per scrivere la funzione `calcola_media(array, pesi)` che restituisce il valor medio di un array. Il valore di default del parametro `pesi` dovrà essere una lista vuota. Nel caso che `pesi=[]`, dovrà essere calcolata una media aritmetica; in caso contrario, si dovrà verificare la coerenza delle dimensioni di `array` e `pesi`, e restituire la media pesata.

### Esercizio 2.1.9

Scrivere la funzione `descrivi(array)` che permette di descrivere un array in termini non parametrici, individuando mediana, deviazione standard e range interquartile (ovvero tra il 25-percentile ed il 75-percentile).
