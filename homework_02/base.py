from abc import ABC
import homework_02


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel
        self.weight = weight
        self.started = False

    def start(self):
        if (self.started == False and self.fuel > 0) or self.started:
            self.started = True
        else:
            raise homework_02.exceptions.LowFuelError
# ничего не сказано про дистанцию в условии

    def move(self, distance):
        self.fuel -= self.fuel_consumption * distance
        if self.fuel >= 0:
            return self.fuel
        else:
            raise homework_02.exceptions.NotEnoughFuel


if __name__ == '__main__':
    veh = Vehicle(fuel = 50, fuel_consumption=1)
    print(veh.move(5))

