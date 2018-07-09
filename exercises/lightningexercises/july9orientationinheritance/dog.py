from animal import Animal

# Create a Dog class that:
# 1. Inherits from animal
# 2. Has its own prop of "breed"
# 3. Initializes the Animal class with "species", "leg_num" and "domesticated" attributes

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__("dog", leg_num=4, domesticated=True)

    def speak(self):
        return f'I am a dog, and I like to say {self.saySomething()}'

    # if __name__ = "Jindo":
    #     jindo = Dog()
    #     print("New Dog = ", jindo)
