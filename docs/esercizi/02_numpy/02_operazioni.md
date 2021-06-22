# Risoluzione degli esercizi

```py
def rettifica(array):
    array[array < 0] = 0
    return array

rettifica(np.array([-1, 2, -3, 4]))
```

```py
def asort(array):
    s = np.sort(array)
    return s[-1::-1]

asort(np.array([3, 2, 5, -1]))
```
