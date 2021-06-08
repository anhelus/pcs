# Plot e visualizzazione

Per visualizzare i valori contenuti in un array abbiamo bisogno di un'altra libreria, dedicata espressamente al plotting, e chiamata *Matplotlib*.

Per installarla, entriamo nel nostro ambiente virtuale, e digitiamo la seguente istruzione:

```sh
pipenv install matplotlib
```



Per esempio, se abbiamo un array come questo:

>>> a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])

importiamo matplotlib:

import matplotlib.pypplot as plt

A questo punto, ci basterà eseguire quesot comando:

plt.plot(a)s