class ClassInvariant:
    def __init__(self, value):
        if value <= 0:
            raise ValueError("Invariant violation: value must be greater than 0.")
        self._value = value

    @property
    def value(self):
        return self._value

    def set_value(self, new_value):
        if new_value <= 0:
            raise ValueError("Invariant violation: value must be greater than 0.")
        self._value = new_value

    def invariant_check(self):
        if self._value <= 0:
            raise ValueError("Invariant violation: value must be greater than 0.")
        print(f"Current value is {self._value}, invariant holds.")