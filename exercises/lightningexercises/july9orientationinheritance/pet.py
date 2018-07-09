# 1. Give a pet its own property of NAME
# 2. Give it a property of animal_type
# 3. animal_type needs to be an instance of a dog
# 4. Create a method on pet that assigns an owner
# 5. __str__ return a string with pet's name, # of legs, and what it says

#Pet wants us to have an animal already made
class Pet():
    def __init__(self, name, critter_instance):
        self.name = name
        self.animal_type = critter_instance

    def set_owner(self, name, phone):
        self.owner_name = name
        self.owner_number = phone

    def __str__(self):
        return f"This pet's name is {self.name}.  It has {self.animal_type.leg_num} legs and likes to say {self.animal_type.saySomething()}!"