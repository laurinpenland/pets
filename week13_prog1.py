"""
Author:  Laurin Penland

Course:  CSC 121

Assignment:  Lab Week 13:  Object Oriented Programming

Description:  Program that creates Pet class and asks the user to create three Pet instances
"""
class Pet:
    #construct an instance of the Pet class; accept 3 arguments and assign them to the name, age, and animal_type attributes
    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.__animal_type = animal_type

    #use the string method to describe the pets and their attributes
    def __str__(self):
        return "Your {} is named {} and is {} years old.".format(self.get_animal_type(), self.get_name(), self.get_age())

    #methods to set or change the name, animal_type, and age attributes
    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.age = age

    #methods to return the name, animal_type, and age attributes
    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.age

def main():
    '''function to create 3 pet objects and return and print results
    Parameters: none
    Returns: none'''
    #create an empty list to store pet objects
    pets = []
    #print program header
    print("\nProgram to Create Three Pet Objects")
    print("-----------------------------------")
    #ask the user for pet attributes of 3 pets using a loop
    for i in range(1,4):
        print(f"\nPet number {i}:\n")
        pet_type = input("Enter the type of pet that you have? (For example: cat, dog, ferret, etc.)\n")
        pet_name = input("Enter your pet's name:\n")
        pet_age = input("Enter your pet's age:\n")
        #create instance of pet
        pet = Pet(pet_name, pet_age, pet_type)
        #add pet instance to list
        pets.append(pet)
        #print confirmation using get methods
        print(f"You entered: {pet.get_animal_type()}, {pet.get_name()}, and {pet.get_age()}")
        i+=1
    #print each description of the pets using the str method and a loop
    print("\nPet Bios:\n")
    for pet in pets:
        print(pet)

if __name__ == '__main__':
    main()
