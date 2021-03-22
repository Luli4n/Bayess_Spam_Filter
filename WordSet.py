import pandas as pd

class WordSet:

    def __init__(self,filepath,separator):

        try:
            self.set_table = pd.read_csv(filepath, sep=separator,
                                    names=['Type', 'Text'], )
        except:
            print("Blad wczytania pliku "+filepath)
            quit()

        # Wyodrebnienie slow i stworzenie slownika
        # zawierajacego unikalne slowa
        self.unique_set = []
        self.deleteUnnecessary()


    # Usuniecie przecinkow,kropek i innych znaków niepotrzebnych
    # Zamiana każdego tekstu na małe literki
    def deleteUnnecessary(self):

        # Usuniecie znakow specjalnych
        self.set_table['Text'] = self.set_table['Text'].str.replace('\W', ' ')

        # Usuniecie malych literek
        self.set_table['Text'] = self.set_table['Text'].str.lower()

        # Wyodrebnienie slow
        self.set_table['Text'] = self.set_table['Text'].str.split()
