https://numpy.org/doc/stable/user/absolute_beginners.html#plotting-arrays-with-matplotlib

# Plot di array

Se dobbiamo generare un plot per i nosri valri, possiamo farlo in maneira estreamemte semplice usando Matplotlib.

## Installazione di Matplotlib

pipenv install matplotlib

Per esempio, se abbiamo un array come questo:

>>> a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])

importiamo matplotlib:

import matplotlib.pypplot as plt

A questo punto, ci basterà eseguire quesot comando:

plt.plot(a)s