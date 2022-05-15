import unittest
import datetime
from Battery.spindler_battery import Spindler


class TestSpindlerBattery(unittest.TestCase):
    def testNeedsServiceT(self):
        current_date = datetime.datetime(2022, 4, 15)
        last_service_date = datetime.datetime(2014, 1, 1)
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needsService())

    def testNeedsServiceF(self):
        current_date = datetime.datetime(2022, 4, 15)
        last_service_date = datetime.datetime(2021, 1, 1)
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needsService())