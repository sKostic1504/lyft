from Tires import tires


class Octoprime(tires.Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needsService(self):
        return sum(self.tire_wear) >= 3.0