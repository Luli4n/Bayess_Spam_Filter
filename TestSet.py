import WordSet
import pandas as pd


class TestSet(WordSet.WordSet):

    def __init__(self, filepath, separator, training_set):
        super().__init__(filepath, separator)

        self.training_set = training_set

        self.n_of_words = len(self.training_set.unique_set)
        self.count_of_hits = 0

        self.check_messages()

        print(self.count_of_hits)
        print(len(self.set_table))



    def check_messages(self):
        # kazdego maila bierze ze zbioru testowego i sprawdza go
        for i in range(len(self.set_table)):
            # prawodopodobienstwa dla hamu i spamu
            ham_prob = 1
            spam_prob = 1
            msg = self.set_table['Text'][i]
            msg_type = self.set_table['Type'][i]
            for word in msg:
                # jezeli dane slowo nie wystapilo to dawane jest 1
                if word in self.training_set.words_count_h:
                    ham_prob *= (self.training_set.words_count_h[word] / (len(self.training_set.set_table) + self.training_set.ham_word_count))
                else:
                    ham_prob *= (1 / (len(self.training_set.set_table) + self.training_set.ham_word_count))
                if word in self.training_set.words_count_s:
                    spam_prob *= (self.training_set.words_count_s[word] / (len(self.training_set.set_table) + self.training_set.spam_word_count))
                else:
                    spam_prob *= (1 / (len(self.training_set.set_table) + self.training_set.spam_word_count))
            # pomnozenie przez prawdopodobienstwo tego ze wiadomosc jest spamem
            ham_prob *= self.training_set.ham_msg_count / (self.training_set.ham_msg_count + self.training_set.spam_msg_count)
            spam_prob *= self.training_set.spam_msg_count / (self.training_set.ham_msg_count + self.training_set.spam_msg_count)
            # sprawdzenie czy prawdopodobienstwo spamu wieksze czy mniejsze i porownanie z faktycznym stanem rzeczy
            if ham_prob > spam_prob and msg_type == 'ham':
                self.count_of_hits += 1
            if ham_prob < spam_prob and msg_type == 'spam':
                self.count_of_hits += 1