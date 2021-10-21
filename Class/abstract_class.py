
from abc import *

class Car(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass

class K5(Car):
    def drive(self):
        print("K5 drive")

k5 = K5()
k5.drive()
