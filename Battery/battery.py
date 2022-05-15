from abc import ABC, abstractmethod



class Battery(ABC):

    @abstractmethod
    def needsService(self):
        pass