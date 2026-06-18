import random


class User:
    def __init__(self) -> None:
        self.current_floor = random.randint(0, 14)
        print(f"You are currently at floor: {self.current_floor}.")


class Elevator:
    def __init__(self, user: User):
        self.current_floor = random.randint(0, 14)
        self._max_floor = 14
        self._min_floor = 0
        if self.current_floor != user.current_floor:
            print(f"*The display shows the elevator is at floor {self.current_floor}*")

    @property
    def max_floor(self):
        return self._max_floor

    @max_floor.setter
    def max_floor(self, value: int):
        self._max_floor = value

    @property
    def min_floor(self):
        return self._min_floor

    @min_floor.setter
    def min_floor(self, value):
        self._min_floor = value

    def call(self, user: User):
        print("*You pressed the button to call the elevator*")
        self.current_floor = user.current_floor  # The elevator moves to you
        print(f"Elevator has arrived at floor {self.current_floor}.")
        self.select_floor()  # Use self to call methods within the class

    def select_floor(self):
        while True:
            try:
                selected_floor = int(
                    input("Type the floor you want to move to (0-14): ")
                )
                if 0 <= selected_floor <= 14:
                    self.current_floor = selected_floor
                    print(f"Ding! You have arrived at floor {self.current_floor}.")
            except ValueError:
                return "You must enter a valid number."


def main():
    user = User()
    elevator = Elevator(user)
    elevator.call(user)


main()
