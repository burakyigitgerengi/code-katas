import random
import time

# Healths

MAX_HUMAN_HEALTH = 100
MAX_PET_HEALTH = 80

# Classes


class Gender:
    MALE = "male"
    FEMALE = "female"
    NONBINARY = "nonbinary"


class Human:
    def __init__(self, name: str, gender: str) -> None:

        self.name = name
        self.gender = gender

        self.health = MAX_HUMAN_HEALTH

    def __str__(self) -> str:
        return f'Character Name: "{self.name}" | Gender: {self.gender} | Health: {self.health}/{MAX_HUMAN_HEALTH}'

    def attack(self, target: Human, Pet) -> int:
        attack_value = random.randint(20, 40)
        return target.health - attack_value

    def explore(self):
        print("Exploring the nearby area...\nThis might take a while.")
        time.sleep(random.randint(10, 25))
        chances = [True, False]
        pet_found = random.choice(chances)
        match pet_found:
            case True:
                print("You found a pet! Do you want to adopt it?")
                user_choice_pet_found = input("You can reply by typing yes or no: ")
                match user_choice_pet_found:
                    case "yes":
                        pet_name = input("Name your pet: ")
                        global pet_of_user
                        pet_of_user = Pet(pet_name)
                        print(f"{pet_of_user.name} is your new buddy now!")

                    case "no":
                        print("You refused to pet.")

            case False:
                user_choice_pet_not_found = input(
                    "You couldn't find any pet...\nKeep on looking? (yes/no)"
                )
                match user_choice_pet_not_found:
                    case "yes":
                        self.explore()
                    case "no":
                        main_menu()


class Pet:
    def __init__(self, name: str) -> None:
        while True:
            try:
                if name.isalpha():
                    self.name = name.capitalize()
                    break
                else:
                    raise ValueError("Name must be letters only.")
            except:
                ValueError("Name must be letters only.")

        self.health = MAX_PET_HEALTH

    def attack(self, target: Human, Pet) -> int:
        attack_value = random.randint(15, 30)
        return target.health - attack_value

    def __str__(self) -> str:
        return f'Pet Name: "{self.name}"'


# Creation Func


def create_your_character():

    while True:
        try:
            name_input = input("Please insert a name of your desire (letters only): ")
            if name_input.isalpha():
                name_input = name_input.capitalize()
                break
            else:
                raise ValueError("Name must be letters only.")
        except:
            ValueError("Name must be letters only.")

    while True:
        try:

            gender_input = input(
                "Please insert the number assigned to your preffered gender (male: 1, female: 2, nonbinary: 3): "
            )

            if gender_input == "1":
                gender_input = "Male"
                break

            if gender_input == "2":
                gender_input = "Female"
                break

            if gender_input == "3":
                gender_input = "Non-binary"
                break

            else:
                raise ValueError("You can only insert 1, 2, 3.")

        except:
            ValueError("You can only insert 1, 2, 3.")

    try:
        global created_char
        created_char = Human(name_input, gender_input)
        print("Character sucessfully created.")
    except:
        raise ModuleNotFoundError


# Main Menu
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


# Main
def main():
    create_your_character()
    print(created_char)
    main_menu()


main()
