"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02 import exceptions


class Plane(base.Vehicle):

    def __init__(self,  weight=0, fuel=0, fuel_consumption=0, max_cargo=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = int()
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_check):
        if self.cargo + cargo_check > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo += cargo_check

    def remove_all_cargo(self):
        old_cargo = int(self.cargo)
        self.cargo = 0
        return old_cargo


if '__name__' == 'main':
    plane = Plane()