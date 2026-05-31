#! ==========================================================
#! LEZIONE 8: COMPREHENSION, ITERATORI E FUNZIONI ANONIME
#! ==========================================================

#! LIST COMPREHENSION
# Sintassi compatta per creare nuove liste applicando trasformazioni o filtri[cite: 901].
# Struttura: [espressione for elemento in iterabile if condizione][cite: 920].

#* Esempio: Quadrati di numeri (Trasformazione) [cite: 898]
quadrati = [n**2 for n in range(10)] # [0, 1, 4, ..., 81]

#* Esempio: Numeri pari (Filtro) [cite: 915]
pari = [n for n in range(10) if n % 2 == 0] # [0, 2, 4, 6, 8]

#* Esempio: Cicli annidati [cite: 937]
# Crea coppie (x, y) solo se x è diverso da y
lista_1 = [1, 2, 3]
lista_2 = [3, 1, 4]
mix = [(x, y) for x in lista_1 for y in lista_2 if x != y]


#! SET & DICTIONARY COMPREHENSION
# La stessa logica si applica a set e dizionari[cite: 939, 940].

#* Set (rimuove duplicati automaticamete) [cite: 941, 942]
quadrati_set = {n**2 for n in [1, 2, 2, 3]} # {1, 4, 9}

#* Dictionary [cite: 943, 944]
mappa_quadrati = {n: n**2 for n in range(5)} # {0:0, 1:1, 2:4, ...}


#! ITERATORI
# Un iteratore è un oggetto che restituisce un elemento alla volta.
# Deve implementare due "magic methods":
# 1. __iter__: inizializza e ritorna l'iteratore (self).
# 2. __next__: ritorna il valore successivo o solleva StopIteration.

#* Uso manuale con iter() e next()
s = "abc"
it = iter(s) 
# print(next(it)) -> 'a'
# print(next(it)) -> 'b'


#! FUNZIONI ANONIME (LAMBDA)
# Funzioni senza nome definite in una sola riga.
# Sintassi: lambda argomenti: espressione (il return è implicito).

#* Esempio: Somma
somma = lambda a, b: a + b
# print(somma(2, 3)) -> 5


#! MAP, FILTER, REDUCE
# Operazioni funzionali sulle collezioni.

#* MAP: applica una funzione a ogni elemento
numeri = [1, 2, 3]
al_quadrato = list(map(lambda x: x**2, numeri)) # [1, 4, 9]

#* FILTER: mantiene solo gli elementi che soddisfano un predicato
solo_pari = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) # [2, 4]

#* REDUCE: riduce la collezione a un singolo valore (va importato)
from functools import reduce
prodotto = reduce(lambda x, y: x * y, [1, 2, 3, 4]) # 24


#! MODULI E LIBRERIE
# Un modulo è un file (.py) contenente funzioni e classi.

#* 1. Libreria Standard (già incluse in Python)
# math, random, statistics, datetime, csv, re, os.
from random import randint # Importa solo una funzione specifica

#* 2. Librerie di Terze Parti (vanno installate)
# Si installano da terminale: conda install nome_libreria.
# Librerie comuni per Data Science:
# - NumPy: calcolo matricial
# - Pandas: manipolazione tabelle.
# - Matplotlib/Seaborn: creazione grafici.

#* Esempio Alias:
import matplotlib.pyplot as plt
# plt.plot([1, 2, 3]) # Uso dell'alias 'plt'