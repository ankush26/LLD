class Vehicle:
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.__class__.__name__} : Engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.__class__.__name__} : Engine turned off.")

    def accelerate(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def brake(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    def __init__(self):
        self.is_engine_on = False
        self.current_speed = 0

    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.__class__.__name__} : Cannot accelerate! Engine is off.")
            return
        self.current_speed += 20
        print(f"{self.__class__.__name__} : Accelerating to {self.current_speed} km/h.")

    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 20
            print(f"{self.__class__.__name__} : Slowing down to {self.current_speed} km/h.")
        else:
            print(f"{self.__class__.__name__} : Already stopped.")


class SportsCar(Car):
    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.__class__.__name__} : Cannot accelerate! Engine is off.")
            return
        if self.current_speed >= 200:
            print(f"{self.__class__.__name__} : Already at maximum speed!")
            return
        self.current_speed += 30
        print(f"{self.__class__.__name__} : Accelerating to {self.current_speed} km/h.")


class FamilyCar(Car):
    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.__class__.__name__} : Cannot accelerate! Engine is off.")
            return
        if self.current_speed >= 150:
            print(f"{self.__class__.__name__} : Already at maximum speed!")
            return
        self.current_speed += 20
        print(f"{self.__class__.__name__} : Accelerating to {self.current_speed} km/h.")


# Example usage
if __name__ == "__main__":
    sports_car = SportsCar()
    sports_car.start_engine()
    sports_car.accelerate()
    sports_car.accelerate()
    sports_car.brake()

    family_car = FamilyCar()
    family_car.start_engine()
    family_car.accelerate()
    family_car.brake()