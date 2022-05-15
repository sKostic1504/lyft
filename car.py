from serviceable import Serviceable


class Car(Serviceable):

    def __init__(self, engine, battery):

        self.engine = engine
        self.battery = battery

    def needsService(self):
        return self.engine.needsService() or self.battery.needsService()
