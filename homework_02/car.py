"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base


class Car(base.Vehicle):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, cls_engine: object):
        self.engine = cls_engine
