# NEVER TAKE A LIST OF REQUIREMENTS AT FACE VALUE -- ASK COPIOUS AMOUNTS OF QUESTIONS -- DO NOT ASSUME

# 1. Items can be added to bag, and assigned to a child.
# 2. Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
# 3. Must be able to list all children who are getting a toy.
# 4. Must be able to list all toys for a given child's name.
# 5. Must be able to set the delivered property of a child, which defaults to false to true.

class LootBag:

    def list_toys_for_child(self, child):
        return ['Transformer']

    def add_toy_to_bag(self, toy, child):
        return "Toy added to bag."