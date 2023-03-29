from modules.datamodel import Animal, Result
from typing import List, Tuple


class PetManager:
    def __init__(self) -> None:
        self.zoo = []

    def _validate(self, animal: Animal) -> Result:
        """check if we can accept this animal.
        Checks:
            1. species is "dog" or "cat"
            2. id is unique
        """
        result = Result()
        existing_ids = set(map(lambda x: x.id, self.zoo))
        if animal.id in existing_ids:
            result.success = False
            result.message = "Duplicate ID"
        return result

    def add_animal(self, animal: Animal) -> Result:
        result = self._validate(animal)
        if result.success:
            self.zoo.append(animal)
        return result

    def list_animals(self, species: str = None, gender: bool = None) -> List[Animal]:
        """
        return list of animal objects, if "species"or "gender" are specified - return only
        animals with specified parameters
        """
        result = []
        # Your code here
        return result

    def get_animal(self, id: int = None, name: str = None) -> Tuple[Animal, Result]:
        """
        Return requested animal and search result.

        If id is passed - return the animal with given id
        if id and name are passed - return the animal with given id and given name, if exists
        if only name is given - return the only animal with this name. If more then 1 animals
        have this name - fail.
        The method should return tuple (Animal, Result) if search was successful, else
        tuple (None, Result) with proper values set in result object
        """
        pass

    def delete_animal(self, id: int) -> Result:
        """
        Delete from the list the animal with given id, if found.
        Return Result object with success=True if the animal deleted, else with success=False
        """
        pass


class Commands:
    add = 1
    search = 2
    list = 3
    delete = 4
    exit = 5


if __name__ == "__main__":
    print("Starting Pet Manager")
    mgr = PetManager()

    menu = """
    1) add animal
    2) search for animal
    3) lsit all animals
    4) delete an animal
    5) exit
    """

w = """Welcome to Pet manager! Please, choose command:
1 - add animal;
2 - search for an animal;
3 - list all animals;
4 - delete an animal;
5 - exit
Enjoy!"""

print(w)

while True:
    c = input("Enter command: ")
    try:
        command = int(c)
    except ValueError:
        print("Invalid command")
        command = 0
    if command == Commands.add:
        id = int(input("ID: "))
        name = input("NAME: ")
        g = input("Gender (M/F): ")
        gender_male = g == "M"
        species = input("Species: ")
        animal = Animal(id, gender_male, name, species)
        result = mgr.add_animal(animal)
        if result.success:
            print("OK")
        else:
            print(f"Error: {result.message}")

    if command == Commands.list:
        pass
        print(self.zoo)
        # your code here
    
    if command == Commands.exit:
        print("Goodbye!")
        quit()
    # Other commands here
