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

#ilosc slow w wiadomosciach ze spamu/hamu(NIE UNIKALNYCH!)
spam_word_count = 0
ham_word_count = 0
#ilosc wiadomosci ze spamu/hamu
ham_msg_count=0
spam_msg_count=0

for i in range(len(set_table)):
    if (set_table['Type'][i] == 'ham'):
        ham_word_count += len(set_table['Text'][i])
        ham_msg_count+=1
    if (set_table['Type'][i] == 'spam'):
        spam_word_count += len(set_table['Text'][i])
        spam_msg_count+=1

#ODTAD USUNALEM BO NIE KORZYSTALEM Z TEGO
# for msg in set_table['Text']:
#     for word in msg:
#         unique_set.append(word)
#
# unique_set = set(unique_set)
# unique_set = list(unique_set)

# Stworzenie macierzy słownikowej
# kolumny=słowa
# wiersze=numer_wiadomosci
# przeciecie= ilosc wystapien słowa w danej wiadomosci
# words_count = {w: [0] * len(set_table) for w in unique_set}
#
# for i in range(len(set_table)):
#     for word in set_table['Text'][i]:
#         words_count[word][i] += 1
#
# # Dodanie do macierzy podpisu kolumny w postaci slowa
#
# words_count = pd.DataFrame(words_count)
# print(words_count.head(3))

#DOTAD USUNALEM

# Odtad dodalem moje
# Zrobilem 2 struktury ktore licza ile danego slowa jest w wiadomosciach ze spamu i z hamu
unique_setS = []
unique_setH = []

# Tutaj rodziela slowa ktore wystepowaly w spanie i slowa ktore wystepowaly w hamie
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

# hashmapa slowo->ilosc wystapien
words_count_h = {w: 1 for w in unique_setH}
words_count_s = {w: 1 for w in unique_setS}

# Liczenie slow
for i in range(len(set_table)):
    if set_table['Type'][i] == 'spam':
        for word in set_table['Text'][i]:
            words_count_s[word] += 1

for i in range(len(set_table)):
    if set_table['Type'][i] == 'ham':
        for word in set_table['Text'][i]:
            words_count_h[word] += 1

#wczytanie zbioru testowego
try:
    set_table_test = pd.read_csv('D:\pajczarmProgramy\SIpodejscie2projekt\TestSet.csv', sep=';',
                                 names=['Type', 'Text'], )
except:
    quit()
#usuwanie przecinkow itd
set_table_test['Text'] = set_table_test['Text'].str.replace('\W', ' ')

set_table_test['Text'] = set_table_test['Text'].str.lower()

set_table_test['Text'] = set_table_test['Text'].str.split()


n_of_words = len(unique_set)
count_of_hits=0
#kazdego maila bierze ze zbioru testowego i sprawdza go
for i in range(len(set_table_test)):
    #prawodopodobienstwa dla hamu i spamu
    ham_prob = 1
    spam_prob = 1
    msg=set_table_test['Text'][i]
    msg_type=set_table_test['Type'][i]
    for word in msg:
        #jezeli dane slowo nie wystapilo to dawane jest 1
        if word in words_count_h:
            ham_prob *= (words_count_h[word] / (len(set_table) + ham_word_count))
        else:
            ham_prob *= (1 / (len(set_table) + ham_word_count))
        if word in words_count_s:
            spam_prob *= (words_count_s[word] / (len(set_table) + spam_word_count))
        else:
            spam_prob *= (1 / (len(set_table) + spam_word_count))
    #pomnozenie przez prawdopodobienstwo tego ze wiadomosc jest spamem
    ham_prob*=ham_msg_count/(ham_msg_count+spam_msg_count)
    spam_prob*=spam_msg_count/(ham_msg_count+spam_msg_count)
    #sprawdzenie czy prawdopodobienstwo spamu wieksze czy mniejsze i porownanie z faktycznym stanem rzeczy
    if ham_prob>spam_prob and msg_type== 'ham':
        count_of_hits+=1
    if ham_prob<spam_prob and msg_type== 'spam':
        count_of_hits+=1
print(count_of_hits)
print(len(set_table_test))