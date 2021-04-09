import WordSet


class TestSet(WordSet.WordSet):

    def __init__(self, filepath, separator, training_set):
        super().__init__(filepath, separator)

        self.training_set = training_set

        self.n_of_words = len(self.training_set.unique_set)
        self.count_of_hits = 0

        self.check_messages()

        print("IN TEST SET")
        print("Number of hits per number of all messages:", self.count_of_hits, "/", len(self.set_table))
        print("Accuracy: ", self.count_of_hits/len(self.set_table), "%")
        print("***************************************************")

    def check_messages(self):
        # Sprawdzenie maili ze zbioru testowego
        for i in range(len(self.set_table)):
            # Prawodopodobienstwa dla hamu i spamu
            ham_prob = 1
            spam_prob = 1

            msg = self.set_table['Text'][i]
            msg_type = self.set_table['Type'][i]
            for word in msg:

                # Jezeli dane slowo nie wystapilo to w liczniku wystepuje 1
                if word in self.training_set.words_count_h:
                    ham_prob *= (self.training_set.words_count_h[word] / (
                                len(self.training_set.set_table) + self.training_set.ham_word_count))
                else:
                    ham_prob *= (1 / (len(self.training_set.set_table) + self.training_set.ham_word_count))

                if word in self.training_set.words_count_s:
                    spam_prob *= (self.training_set.words_count_s[word] / (
                                len(self.training_set.set_table) + self.training_set.spam_word_count))
                else:
                    spam_prob *= (1 / (len(self.training_set.set_table) + self.training_set.spam_word_count))

            # Pomnozenie przez prawdopodobienstwo tego ze wiadomosc jest spamem
            ham_prob *= self.training_set.ham_msg_count / (
                        self.training_set.ham_msg_count + self.training_set.spam_msg_count)
            spam_prob *= self.training_set.spam_msg_count / (
                        self.training_set.ham_msg_count + self.training_set.spam_msg_count)

            # Porownanie wyznaczonych prawdobodobienstw z ich faktycznym okresleniem
            if ham_prob > spam_prob and msg_type == 'ham':
                self.count_of_hits += 1

            elif ham_prob < spam_prob and msg_type == 'spam':
                self.count_of_hits += 1
