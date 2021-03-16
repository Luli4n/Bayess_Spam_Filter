import pandas as pd

# Początek pliku który będzie odpowiadał za wczytywanie słów do bazy

# Wczytanko pliku
# Pamietajcie zeby zmienic sciezke
try:
    set_table = pd.read_csv('D:\pajczarmProgramy\SIpodejscie2projekt\TrainingSet.csv', sep=';',
                            names=['Type', 'Text'], )
except:
    quit()

# Usuniecie przecinkow,kropek i innych znaków niepotrzebnych
# Zamiana każdego tekstu na małe literki

set_table['Text'] = set_table['Text'].str.replace('\W', ' ')

set_table['Text'] = set_table['Text'].str.lower()

# Wyodrebnienie slow i stworzenie slownika
# zawierajacego unikalne slowa
unique_set = []

set_table['Text'] = set_table['Text'].str.split()

for msg in set_table['Text']:
    for word in msg:
        unique_set.append(word)

unique_set = set(unique_set)
unique_set = list(unique_set)

# Stworzenie macierzy słownikowej
# kolumny=słowa
# wiersze=numer_wiadomosci
# przeciecie= ilosc wystapien słowa w danej wiadomosci
words_count = {w: [0] * len(set_table) for w in unique_set}

for i in range(len(set_table)):
    for word in set_table['Text'][i]:
        words_count[word][i] += 1

# Dodanie do macierzy podpisu kolumny w postaci slowa

words_count = pd.DataFrame(words_count)
print(words_count.head(3))

#Odtad dodalem moje
#Zrobilem 2 struktury ktore licza ile danego slowa jest w wiadomosciach ze spamu i z hamu
unique_setS = []
unique_setH = []

#Tutaj rodziela slowa ktore wystepowaly w spanie i slowa ktore wystepowaly w hamie
for i in range(len(set_table)):
    if set_table['Type'][i] == 'ham':
        for word in set_table['Text'][i]:
            unique_setH.append(word)
    else:
        for word in set_table['Text'][i]:
            unique_setS.append(word)

unique_setS = set(unique_setS)
unique_setS = list(unique_setS)
unique_setH = set(unique_setH)
unique_setH = list(unique_setH)

#hashmapa slowo->ilosc wystapien
words_count_h = {w: 0 for w in unique_setH}
words_count_s = {w: 0 for w in unique_setS}

#Liczenie slow
for i in range(len(set_table)):
    if set_table['Type'][i] == 'spam':
        for word in set_table['Text'][i]:
            words_count_s[word] += 1

for i in range(len(set_table)):
    if set_table['Type'][i] == 'ham':
        for word in set_table['Text'][i]:
            words_count_h[word] += 1
