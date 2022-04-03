from train_calculator import TrainCalculator
import unittest

class TrainCalculateTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._train_calculator = TrainCalculator('AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7')

    def test_distance_between_stops(self):
        self.assertEqual(self._train_calculator.distance_between_stops('ABC'), 9)
        self.assertEqual(self._train_calculator.distance_between_stops('AD'), 5)
        self.assertEqual(self._train_calculator.distance_between_stops('ADC'), 13)
        self.assertEqual(self._train_calculator.distance_between_stops('AEBCD'), 22)
        self.assertEqual(self._train_calculator.distance_between_stops('AED'), 'NO SUCH ROUTE')

    def test_paths_of_max_stops(self):
        self.assertCountEqual(self._train_calculator.paths_of_max_stops('C', 'C', 3), ['CDC', 'CEBC'])
        self.assertCountEqual(self._train_calculator.paths_of_max_stops('C', 'C', 2), ['CDC'])
        self.assertCountEqual(self._train_calculator.paths_of_max_stops('C', 'C', 1), [])

    def test_paths_of_exactly_stops(self):
        self.assertCountEqual(self._train_calculator.paths_of_exactly_stops('A', 'C', 4), ['ABCDC', 'ADCDC', 'ADEBC'])
        self.assertCountEqual(self._train_calculator.paths_of_exactly_stops('A', 'B', 1), ['AB'])
        self.assertCountEqual(self._train_calculator.paths_of_exactly_stops('A', 'C', 1), [])

    def test_shortest_distance(self):
        self.assertEqual(self._train_calculator.shortest_distance('A', 'C'), 9)
        self.assertEqual(self._train_calculator.shortest_distance('B', 'B'), 9)

    def test_paths_of_max_length(self):
        self.assertCountEqual(self._train_calculator.paths_of_max_length('C', 'C', 30), ['CDC', 'CEBC', 'CEBCDC', 'CDCEBC', 'CDEBC', 'CEBCEBC', 'CEBCEBCEBC'])

if __name__ == '__main__':
    unittest.main()