import unittest
from Tires.octoprime_tires import Octoprime


class TestOctoprimeTires(unittest.TestCase):
    def testNeedsServiceT(self):
        wear = [0.9, 0.9, 0.9, 0.3]
        tires = Octoprime(wear)
        self.assertTrue(tires.needsService())

    def testNeedsServiceF(self):
        wear = [0.9, 0.9, 0.9, 0.2]
        tires = Octoprime(wear)
        self.assertFalse(tires.needsService())