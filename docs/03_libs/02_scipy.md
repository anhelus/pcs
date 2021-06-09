# SciPy

SciPy è una collezione di algoritmi matematici e funzioni costruite su NumPy. Aggiunge funzioanlità significative alle normali sessioni Python, fornendo all'utente dei comandi e delle classi per manipolare e visualizzare i dati.

Per installarlo:

pipenv install scipy

>>> import numpy as np
>>> import matplotlib as mpl
>>> import matplotlib.pyplot as plt

## Generiamo una distribuzione di probabilità

Comparazione tra il valore teorico di una distribuzione di densità di probabilità e l'istogramma di un grande numero di valori generati casualmente.


```py
from scipy.stats import norm, uniform

x_1 = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
x_2 = np.linspace(uniform.ppf(0.01), uniform.ppf(0.99), 100)

r_1 = norm.rvs(size=1000)
r_2 = uniform.rvs(size=1000)

fig, (ax_1, ax_2) = plt.subplots(2, 1)

ax_1.plot(x_1, norm.pdf(x_1))
ax_1.hist(r_1, density=True)

ax_2.plot(x_2, uniform.pdf(x_2))
ax_2.hist(r_2, density=True)

plt.show()
```

## calcoliamo determinante ed inversa

```py
from scipy import linalg

def can_be_inverted(mat):
	if linalg.det(mat) != 0.:
		return True
	else:
		return False


def invert_if_invertible(mat):
	if can_be_inverted(mat):
		return linalg.inv(mat)
	else:
		return None
```

## Trasformata di fourier di un seno

```py
from scipy.fft import fft

N = 100

T = 0.01

x = np.linspace(0., N*T, N)

y = np.sin(2.0 * np.pi * x)

yf = fft(y)

plt.plot(np.abs(yf[0:50]))

plt.show()
```

somma di seni

```py
y_tr = np.sin(2.0 * np.pi * x) + np.sin(20 * 2.0 * np.pi * x)

y_trf = fft(y_tr)

plt.plot(np.abs(y_trf[0:50]))
```

somma di seni con smorzamento

```py
y_tr = np.sin(2.0 * np.pi * x) + 0.5 * np.sin(20 * 2.0 * np.pi * x)

y_trf = fft(y_tr)

plt.plot(np.abs(y_trf[0:50]))
```
