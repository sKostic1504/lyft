from Battery import battery
from Car import car
from Engine import engine


class Thovex(car.Car):

    def needsService(self):
        if engine.needsService() is True or battery.needsService() is True:
            return True
        return False