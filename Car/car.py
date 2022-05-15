from abc import ABC
from Engine import engine
from Battery import battery


class Car(ABC):

    def __init__(self, engine, battery):

        self.engine = engine
        self.battery = battery

    def needsService(self):

        if engine.Engine.needsService() is True or battery.Battery.needsService() is True:
            return True
        return False
