from abc import abstractmethod


class Serviceable():

    @abstractmethod
    def needsService(self):
        pass