import WordSet


class TrainingSet(WordSet.WordSet):

    def __init__(self, filepath, separator):

        super().__init__(filepath, separator)
        self.count()
        self.split()
        self.create_hashmaps()

    def count(self):
        # Ilosc slow w wiadomosciach ze spamu/hamu(NIE UNIKALNYCH!)
        self.spam_word_count = 0
        self.ham_word_count = 0

        # Ilosc wiadomosci ze spamu/hamu
        self.ham_msg_count = 0
        self.spam_msg_count = 0

        for i in range(len(self.set_table)):

            if self.set_table['Type'][i] == 'ham':
                self.ham_word_count += len(self.set_table['Text'][i])
                self.ham_msg_count += 1

            if self.set_table['Type'][i] == 'spam':
                self.spam_word_count += len(self.set_table['Text'][i])
                self.spam_msg_count += 1

        print("***************************************************")
        print("IN TRAINING SET")
        print("HAM: ", self.ham_msg_count/len(self.set_table), "%")
        print("SPAM: ", self.spam_msg_count/len(self.set_table), "%")
        print("***************************************************")

    def split(self):
        self.unique_setS = []
        self.unique_setH = []

        # Tutaj rodziela slowa ktore
        # wystepowaly w spamie i slowa ktore wystepowaly w hamie
        for i in range(len(self.set_table)):
            if self.set_table['Type'][i] == 'ham':
                for word in self.set_table['Text'][i]:
                    self.unique_setH.append(word)
            else:
                for word in self.set_table['Text'][i]:
                    self.unique_setS.append(word)

        self.unique_setS = list(set(self.unique_setS))
        self.unique_setH = list(set(self.unique_setH))

    def create_hashmaps(self):
        # Hashmapa slowo->ilosc wystapien
        self.words_count_h = {w: 1 for w in self.unique_setH}
        self.words_count_s = {w: 1 for w in self.unique_setS}

        # Liczenie slow
        for i in range(len(self.set_table)):
            if self.set_table['Type'][i] == 'spam':
                for word in self.set_table['Text'][i]:
                    self.words_count_s[word] += 1

        for i in range(len(self.set_table)):
            if self.set_table['Type'][i] == 'ham':
                for word in self.set_table['Text'][i]:
                    self.words_count_h[word] += 1
