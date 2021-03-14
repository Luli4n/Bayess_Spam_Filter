import pandas as pd

#Początek pliku który będzie odpowiadał za wczytywanie słów do bazy

#Wczytanko pliku
#Pamietajcie zeby zmienic sciezke
try:
    set_table=pd.read_csv('C:/Users/julek/PycharmProjects/ProjektSI/TrainingSet.csv',sep=';',names=['Type','Text'],)
except:
    quit()

#Usuniecie przecinkow,kropek i innych znaków niepotrzebnych
#Zamiana każdego tekstu na małe literki

set_table['Text']=set_table['Text'].str.replace('\W',' ')

set_table['Text']=set_table['Text'].str.lower()

#Wyodrebnienie slow i stworzenie slownika
#zawierajacego unikalne slowa
unique_set=[]

set_table['Text']=set_table['Text'].str.split()

for msg in set_table['Text']:
    for word in msg:
        unique_set.append(word)

unique_set=set(unique_set)
unique_set=list(unique_set)

#Stworzenie macierzy słownikowej
#kolumny=słowa
#wiersze=numer_wiadomosci
#przeciecie= ilosc wystapien słowa w danej wiadomosci
words_count={w:[0]*len(set_table) for w in unique_set}

for i in range(len(set_table)):
    for word in set_table['Text'][i]:
            words_count[word][i]+=1

#Dodanie do macierzy podpisu kolumny w postaci slowa
words_count=pd.DataFrame(words_count)
print(words_count.head(3))