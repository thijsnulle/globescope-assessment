from mars_rover import MarsMission
import unittest

class TrainCalculateTest(unittest.TestCase):

    def test_single_mars_rover_only_rotation(self):
        mars_mission = MarsMission('5 5\n1 1 N\nLR')
        self.assertEqual(mars_mission.execute_instructions(), '1 1 N')
    
    def test_single_mars_rover_four_same_rotations(self):
        mars_mission = MarsMission('5 5\n2 2 N\nRRRR')
        self.assertEqual(mars_mission.execute_instructions(), '2 2 N')
    
    def test_single_mars_rover_same_end_position(self):
        mars_mission = MarsMission('5 5\n3 3 N\nMRRMRR')
        self.assertEqual(mars_mission.execute_instructions(), '3 3 N')

    def test_single_mars_rover(self):
        mars_mission = MarsMission('5 5\n1 2 N\nLMLMLMLMM')
        self.assertEqual(mars_mission.execute_instructions(), '1 3 N')

    def test_multiple_mars_rovers(self):
        mars_mission = MarsMission('5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM')
        self.assertEqual(mars_mission.execute_instructions(), '1 3 N\n5 1 E')

if __name__ == '__main__':
    unittest.main()