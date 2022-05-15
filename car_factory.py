from Engine.willoughby_engine import Willoughby
from Engine.sternman_engine import Sternman
from Engine.capulet_engine import Capulet
from Battery.spindler_battery import Spindler
from Battery.nubbin_battery import Nubbin
from car import Car


class Factory:

    @staticmethod
    def calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Spindler(current_date,last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def palindrome(current_date, last_service_date, warning_light):
        engine = Sternman(warning_light)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def Thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car