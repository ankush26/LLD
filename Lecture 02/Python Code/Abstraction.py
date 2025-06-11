class Car:
    def start_engine(self):
        raise NotImplementedError("This method should be overridden.")

    def shift_gear(self, gear):
        raise NotImplementedError("This method should be overridden.")

    def accelerate(self):
        raise NotImplementedError("This method should be overridden.")

    def brake(self):
        raise NotImplementedError("This method should be overridden.")

    def stop_engine(self):
        raise NotImplementedError("This method should be overridden.")


class SportsCar(Car):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0
        self.current_gear = 0
        self.tyre_company = "MRF"

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine starts with a roar!")

    def shift_gear(self, gear):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off! Cannot shift gear.")
            return
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")

    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off! Cannot accelerate.")
            return
        self.current_speed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_gear = 0
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")