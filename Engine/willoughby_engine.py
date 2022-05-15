from Engine.engine import Engine

class Willoughby(Engine):

    def __init__(self, warning_light):

        self.warning_light = warning_light

    def needsService(self):
        if self.warning_light is True:
            return True
        return False
