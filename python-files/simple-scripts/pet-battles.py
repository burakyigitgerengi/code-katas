from __future__ import annotations

import random
import time


class WrongNamingError(Exception):

    def __str__(self) -> str:
        return "Only use alphabet characters & the name must be an instance of 'str'."


class GenderError(Exception):
    def __str__(self) -> str:
        return "Your selection is only limited to: 1, 2, 3."


class Human:
    def __init__(self, name: str, gender: str) -> None:

        self._max_health = 100
        self.health = self.max_health
        self.name = name
        self.gender = gender

    @property
    def max_health(self):
        return self._max_health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, input: str):

        if isinstance(input, str) and input.isalpha():
            self._name = input

        else:
            raise WrongNamingError

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, input: str):

        if isinstance(input, str) and input.isalpha():
            self._gender = input.capitalize()

        else:
            raise GenderError

    def __str__(self) -> str:
        return f'Character Name: "{self.name}" | Gender: {self.gender} | Health: {self.health}/{self.max_health}'

    def attack(self, target: Human | Pet) -> int:
        attack_value = random.randint(20, 40)
        return target.health - attack_value

    def explore(self):
        print("Exploring the nearby area...\nThis might take a while.")
        time.sleep(random.randint(5, 15))
        pet_found = random.choice([True, False])
        match pet_found:
            case True:
                print("You found a pet! Do you want to adopt it?")
                user_choice_pet_found = input(
                    "You found a pet! Do you want to adopt it?\n(yes/no): "
                )
                match user_choice_pet_found:
                    case "yes":
                        pet_name = input("Name your pet: ")
                        global pet_of_user
                        pet_of_user = Pet(pet_name)
                        print(f"{pet_of_user.name} is your new buddy now!")

                    case "no":
                        print("You refused to pet.")

                    case _:
                        print("Invalid chocice.")

            case False:
                user_choice_pet_not_found = input(
                    "You couldn't find any pet... Keep on looking?\n(yes/no): "
                )
                match user_choice_pet_not_found:
                    case "yes":
                        self.explore()
                    case "no":
                        main_menu()
                    case _:
                        print("Invalid chocice.")


class Pet:
    def __init__(self, name: str) -> None:

        self._max_health = 75
        self.health = self.max_health

        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Name must be letters only.")

        self.name = name.capitalize()

    @property
    def max_health(self):
        return self._max_health

    def attack(self, target: Human | Pet) -> None:
        attack_value = random.randint(15, 30)
        target.health -= attack_value

    def __str__(self) -> str:
        return f'Pet Name: "{self.name}" | Health: {self.health}/{self.max_health}'


# Character Creation


def get_name_from_user() -> str:

    while True:
        try:
            name_from_user = input(
                "Please insert a name of your desire for your character: "
            )

            if name_from_user.isalpha():
                name_from_user = name_from_user.capitalize()
                print(f"Name of your character: {name_from_user}")
                return name_from_user

            else:
                raise WrongNamingError()
        except WrongNamingError as e:
            print("Error: ", e)


def get_gender_from_user() -> str:

    while True:
        try:
            gender_from_user = input(
                "Please insert a gender of your desire for your character:\n1. Female \n2. Male \n3. Other \n> "
            )

            match gender_from_user:

                case "1":
                    return "Female"

                case "2":
                    return "Male"

                case "3":
                    return "Other"

                case _:
                    print("Invalid chocice.")

            if not gender_from_user == ["1", "2", "3"]:
                raise GenderError

            else:
                raise GenderError
        except GenderError as e:
            print("Error: ", e)


def main_menu():

    print(
        "-Main Menu- \n (1) Inspect Yourself \n (2) Inspect Pet \n (3) Explore \n (0) Exit"
    )
    selection = input(">")
    match selection:
        case "1":
            print(created_char)
            main_menu()
        case "2":
            while True:
                try:
                    if pet_of_user:
                        print(pet_of_user)
                        main_menu()
                    else:
                        raise ValueError("You don't have a pet.")
                        main_menu()
                except NameError:
                    print("You don't have a pet.")
                    main_menu()

        case "3":
            created_char.explore()
            main_menu()

        case "0":
            exit()

        case _:
            print("Invalid chocice.")


def main():
    name = get_name_from_user()
    gender = get_gender_from_user()

    global created_char
    created_char = Human(name, gender)

    print(created_char)
    main_menu()


main()
