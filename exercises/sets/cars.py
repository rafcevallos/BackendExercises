# create set with 4 vehicle models
showroom = set(['Prius', 'USS Enterprise', 'Millenium Falcon', 'Delorean'])
# print the length of showroom
print(len(showroom))

# pick item in showroom and add it to the set again
showroom.add('Prius')
# print showroom
print(showroom)
# Only one instance of 'Prius' is in the set despite adding it. Sets must have all unique values.

# using update(), add 2 more vehicle models to showroom with another set
# create new showroom set
showroom2 = set(['Batmobile', 'Ecto1'])
showroom.update(showroom2)
print(showroom)

# Remove a car from the set with discard() method
showroom.discard('Prius')
# print showroom with 'Prius' removed
print(showroom)


# Another set of cars with some new models and some similar models
junkyard = set(['Batmobile','Ecto1', 'USS Enterprise', 'Tank', "Quinjet", "Mjolnir"])
print("junkyard", junkyard)

# use intersection() method to see which cars exist in showroom and junkyard
intersection = showroom.intersection(junkyard)
print("intersection", intersection)

# use union() method to combine junkyard into showroom
newcollection = showroom.union(junkyard)
print("newcollection", newcollection)

# use discard() method to remove any cars from junkyard to put in showroom
newcollection.discard('Tank')
print("newcollection", newcollection)