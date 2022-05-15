from Engine.engine import Engine

class Sternman(Engine):

    def __init__(self, current_mileage, last_service_mileage):

        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needsService(self):

        if self.current_mileage - self.last_service_mileage > 60000:
            return True

        return False
