class Car:
    def __init__(self):
        self.speed = 0

    def accelerate(self):
        self.speed += 20
        print(f"Car is accelerating. Current speed: {self.speed} km/h")

    # PostCondition: Speed must reduce after brake
    def brake(self):
        print("Applying brakes")
        self.speed -= 20
        if self.speed < 0:
            self.speed = 0
        print(f"Car has slowed down. Current speed: {self.speed} km/h")


class HybridCar(Car):
    def __init__(self):
        super().__init__()
        self.charge = 100

    # Strengthened PostCondition: Speed must reduce after brake
    # PostCondition: Charge must increase.
    def brake(self):
        print("Applying brakes in HybridCar")
        super().brake()  # Call the parent class's brake method
        self.charge += 10  # Strengthening the postcondition
        print(f"HybridCar charge increased. Current charge: {self.charge}%")


def main():
    car = Car()
    car.accelerate()
    car.brake()

    hybrid_car = HybridCar()
    hybrid_car.accelerate()
    hybrid_car.brake()


if __name__ == "__main__":
    main()