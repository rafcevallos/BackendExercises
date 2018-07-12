import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog
# two lines seperating imports from first line of code is PEP STANDARD


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")

    def test_animal_creation(self):

        # bob = Dog("Bob")
        murph = Dog("Murphy")

        self.assertIsInstance(murph, Dog)
        self.assertIsInstance(murph, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)
        self.assertNotEqual(self.bob.legs, 12)

    def test_animal_can_set_species(self):
        # setting Bob's species as Canid
        self.bob.set_species("Caninae")
        # testing if user types in caninae in lowercase that it will still pass as true
        """this test passes if both values are true"""
        self.assertEqual(self.bob.species.lower(), "caninae")

        """this test passes if both values are not equal to each other"""
        self.assertNotEqual(self.bob.species.lower(), "caninaey")

    def test_animal_can_get_species(self):
        # Bob's species was set in line 28, so we just get his species by invoking get_species()
        """this tests SUCCESS - passes if both values are true"""
        self.assertEqual(self.bob.get_species().lower(), "caninae")

        """this tests FAILURE - passes if both values are not equal to each other"""
        self.assertNotEqual(self.bob.get_species().lower(), "poop")

    def test_str(self):
        self.assertEqual(self.bob.__str__().lower(), "bob is a caninae")
        self.assertNotEqual(self.bob.__str__().lower(), "Poop is a Butt")

    # def test_animal_walk(self):


    def test_setting_speed(self):
        #create a new instance of dog
        self.poopy = Dog("Poopy")
        self.assertEqual(self.poopy.speed, 0)
        self.poopy.walk()
        self.assertEqual(self.poopy.speed, 0.2)

if __name__=='__main__':
    unittest.main()
