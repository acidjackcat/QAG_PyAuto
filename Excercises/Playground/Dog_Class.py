""" Lets create new class Dog that should reperesent all existing dogs on
this planet"""


class Dog:
    """A simple attempt to model a dog. """

    def __init__(self, name, age, color, breed):
        """Initialize name, age, color and breed parameters:"""
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

    # Here is some actions for our Dog: bark, sit, roll_over, bring_it:
    def bark(self):
        """Simulation of barking in response to command:"""
        print(f"{self.name} is now barking.")

    def sit(self):
        """Simulation of sitting in response to command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulation of roll over in response to command """
        print(f"{self.name} is now rolling over.")

    def bring_it(self):
        """Simulation of bringin the item in response to command"""
        print(f"{self.name} is bringing thrown item.")


his_dog = Dog("Woffie", 5, "White", "Labrador")
his_dog.sit()
his_dog.roll_over()
his_dog.bark()
print(f"{his_dog.name} age is {his_dog.age}")

my_dog = Dog('Willie', 6, "black", "Doberman")
your_dog = Dog('Lucy', 3, "red", "black hound")
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()