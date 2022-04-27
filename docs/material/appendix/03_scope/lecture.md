# Appendice C - Ambito di una variabile

All'interno di un programma ogni variabile ha una sorta di "ciclo di vita", che ne prevede la creazione, utilizzo e, infine, distruzione.

L'intero script ha un ambito definito come *globale*: ciò significa che tutte le variabili specificate nel corpo "principale" dello script hanno validità in tutto il nostro codice. Le singole funzioni, invece, definiscono un ambito *locale*, creato alla chiamata della funzione, e distrutto al termine della stessa.

Facciamo un esempio. Definiamo una funzione `calcolo_voto_accesso_laurea` che accetta in ingresso un argomento, ovvero la lista con i voti degli esami.

```py
def calcolo_voto_accesso_laurea(voti_esami):
    somma_voti = 0
    for voto in voti_esami:
        somma_voti += voto
    voto_medio = somma_voti/len(voti_esami)
    voto_accesso = voto_medio / 3 * 11
    return voto_accesso
```

Proviamo a chiamarla.

```py
lista_voti = [18, 20, 19, 30, 24, 30]

print('Il voto di accesso è: ', calcolo_voto_accesso_laurea(lista_voti))
```

A schermo vedremo:

```py
Il voto di accesso è:  86.16666666666666
```

## C1 - Prima modifica

Facciamo una prima modifica:

```py
lista_voti = [18, 20, 19, 30, 24, 30]

def calcolo_voto_accesso_laurea(voti_esami):
    print(f'La lista dei voti è: {lista_voti}')
    somma_voti = 0
    for voto in voti_esami:
        somma_voti += voto
    voto_medio = somma_voti/len(voti_esami)
    voto_accesso = voto_medio / 3 * 11
    return voto_accesso

print('Il voto di accesso è: ', calcolo_voto_accesso_laurea(lista_voti))
```

Adesso vedremo a schermo due valori:

```py
La lista dei voti è: [18, 20, 19, 30, 24, 30]
Il voto di accesso è:  86.16666666666666
```

## C2 - Seconda modifica

Proviamo a modificare ancora il codice:

```py
lista_voti = [18, 20, 19, 30, 24, 30]

def calcolo_voto_accesso_laurea(voti_esami):
    somma_voti = 0
    for voto in voti_esami:
        somma_voti += voto
    voto_medio = somma_voti/len(voti_esami)
    voto_accesso = voto_medio / 3 * 11
    return voto_accesso

print('Il voto medio è: ', voto_medio)
print('Il voto di accesso è: ', calcolo_voto_accesso_laurea(lista_voti))
```

Adesso vedremo a schermo il seguente risultato:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'voto_medio' is not defined
Il voto di accesso è:  86.16666666666666
```

Cosa è successo? Andiamo un attimo a ritroso, e partiamo dalla prima modifica.

In questo caso, infatti, abbiamo provato ad accedere alla variabile *globale* `lista_voti`, definita nel corpo "principale" dello script, dall'interno della funzione `calcola_voto_accesso_laurea`. Ciò è evidentemente possibile, in quanto possiamo accedere ad una variabile globale da un ambito locale.

Il contrario, tuttavia, non è possibile: infatti, nella seconda modifica, proviamo ad accedere ad una variabile locale alla funzione `calcola_voto_accesso_laurea` dall'esterno della funzione stessa. Questo non può avvenire, perché le variabili locali "scompaiono" al termine della funzione in cui sono definite, per cui l'interprete ci darà un errore.
