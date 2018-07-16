import unittest
from lootbag import LootBag


class TestLootBag(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bag = LootBag()

    def test_can_list_toys_from_bag_for_child(self):
        expected_result = 'Transformer'
        actual_result = self.bag.list_toys_for_child('Raffy')

        self.assertIn(expected_result, actual_result)

    def test_add_toy_to_bag(self):
        bag = LootBag()
        toy = 'Transformer'
        self.assertEqual(toy, bag.add_toy_to_bag('Transformer', 'Raffy'), "Toy added to bag.")

        # toy = 'Thundercats'
        # toy_list = self.bag.list_toys_for_child("Raffy")
        # self.assertNotIn(toy, toy_list)
        # bag.add_toy_to_bag('truck', 'Raffy')
        # toy_list = self.bag.list_toys_for_child('Raffy')
        # self.assertIn(toy, toy_list)


if __name__ == '__main__':
    unittest.main()
