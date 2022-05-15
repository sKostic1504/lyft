import unittest

from Engine.capulet_engine import Capulet


class TestCapuletEngine(unittest.TestCase):
    def testNeedsServiceT(self):
        current_mileage = 400000
        last_service_mileage = 320000
        engine = Capulet(current_mileage, last_service_mileage)
        self.assertTrue(engine.needsService())

    def testNeedsServiceF(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = Capulet(current_mileage, last_service_mileage)
        self.assertFalse(engine.needsService())