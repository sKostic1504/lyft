import unittest

from Engine.willoughby_engine import Willoughby


class TestCapuletEngine(unittest.TestCase):
    def testNeedsServiceT(self):
        current_mileage = 400000
        last_service_mileage = 320000
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertTrue(engine.needsService())

    def testNeedsServiceF(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertFalse(engine.needsService())