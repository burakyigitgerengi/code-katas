MAX_FLOOR = 14
MIN_FLOOR = 0

elevator_floor = 0
user_floor = 0


class Elevator:
    def __init__(self):
        if elevator_floor != user_floor:
            print(f"*The display shows the elevator is at floor {elevator_floor}*")

    def get_user_floor_input(self):
        global user_floor
        while True:
            try:
                user_floor_input = input("At which floor are you? (0-14): ")
                user_floor_input = int(user_floor_input)
                if 0 <= user_floor_input <= 14:
                    user_floor = user_floor_input
                    break
                else:
                    raise ValueError("You must enter a valid number.")
            except ValueError:
                print("You must enter a valid number.")

    def call(self):
        global elevator_floor
        print("*You pressed the button to call the elevator*")
        elevator_floor = user_floor  # The elevator moves to you
        print(f"Elevator has arrived at floor {elevator_floor}.")
        self.select_floor()  # Use self to call methods within the class

    def select_floor(self):
        global elevator_floor
        while True:
            try:
                selected_floor = input("Type the floor you want to move to (0-14): ")
                selected_floor = int(selected_floor)
                if 0 <= selected_floor <= 14:
                    elevator_floor = selected_floor
                    print(f"Ding! You have arrived at floor {elevator_floor}.")
                else:
                    raise ValueError("You must enter a valid number.")
            except ValueError:
                print("You must enter a valid number.")


def main():
    elevator = Elevator()
    elevator.get_user_floor_input()
    elevator.call()


main()
