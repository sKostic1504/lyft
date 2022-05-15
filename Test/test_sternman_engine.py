import unittest

from Engine.sternman_engine import Sternman


class TestSternmanEngine(unittest.TestCase):
    def testNeedsServiceT(self):
        warning = True
        engine = Sternman(warning)
        self.assertTrue(engine.needsService())

    def testNeedsServiceF(self):
        warning = False
        engine = Sternman(warning)
        self.assertFalse(engine.needsService())