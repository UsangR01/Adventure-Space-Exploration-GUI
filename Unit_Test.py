import unittest
from negotiator import Negotiator

class TestNegotiator(unittest.TestCase):

    def setUp(self):
        self.negotiator=Negotiator("TestNegotiator")

    def testNegotiator_Life(self):
        self.assertEqual(self.negotiator.health, 5)
        self.negotiator.dropHealth()
        self.negotiator.assertEqual(self.negotiator.health, 4)  # The negotiator's health has dropped by 1. 4 left...
        self.negotiator.getHealth()
        self.assertEqual(self.negotiator.health, 5)             # The negotiator's health has increased by 1. 5 left...
        self.negotiator.getHealth()
        self.assertEqual(self.negotiator.health, 5)             # The negotiator's health can't exceed a maximum of 5...

if __name__ == '__main__':
    unittest.main()