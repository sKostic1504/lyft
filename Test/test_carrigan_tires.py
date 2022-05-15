import unittest

from Tires.carrigan_tires import Carrigan


class TestCarriganTires(unittest.TestCase):
    def testNeedsServiceT(self):
        wear = [0.4, 0.8, 0.6, 0.9]
        tires = Carrigan(wear)
        self.assertTrue(tires.needsService())

    def testNeedsServiceF(self):
        wear = [0.1, 0.1, 0.8, 0.1]
        tires = Carrigan(wear)
        self.assertFalse(tires.needsService())