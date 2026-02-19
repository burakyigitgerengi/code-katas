MAX_FLOOR = 14
MIN_FLOOR = 0

elevator_floor = 0
user_floor = 0


def get_floor_of_user():
    global user_floor
    floor_of_user = input("At which floor are you? (0-14): ")
    try:
        floor_of_user = int(floor_of_user)
        if 0 <= floor_of_user <= 14:
            user_floor = floor_of_user
        else:
            raise ValueError
    except ValueError:
        print("You must enter a valid number.")


class Elevator:
    def __init__(self):
        if elevator_floor != user_floor:
            print(f"*The display shows the elevator is at floor {elevator_floor}*")
        else:
            print(f"*The elevator is already here at floor {elevator_floor}*")

    def call(self):
        global elevator_floor
        print("*You pressed the button to call the elevator*")
        elevator_floor = user_floor  # The elevator moves to you
        print(f"Elevator has arrived at floor {elevator_floor}.")
        self.select_floor()  # Use self to call methods within the class

    def select_floor(self):
        global elevator_floor
        selected_floor = input("Type the floor you want to move to (0-14): ")
        try:
            selected_floor = int(selected_floor)
            if 0 <= selected_floor <= 14:
                elevator_floor = selected_floor
                print(f"Ding! You have arrived at floor {elevator_floor}.")
            else:
                raise ValueError
        except ValueError:
            print("You must enter a valid number.")


def main():
    get_floor_of_user()
    elevator = Elevator()
    elevator.call()


main()