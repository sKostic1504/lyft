from Tires import tires


class Carrigan(tires.Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needsService(self):
        for tire in self.tire_wear:
            if tire >= 0.9:
                return True
        return False