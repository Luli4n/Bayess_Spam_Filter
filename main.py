import TrainingSet
import TestSet
import warnings


# Wejscie do programu

class Main:

    def __init__(self):
        warnings.simplefilter(action='ignore', category=FutureWarning)
        self.training_set = TrainingSet.TrainingSet('TrainingSet.csv', ';')
        self.test_set = TestSet.TestSet('TestSet.csv', ';', self.training_set)


test = Main()
