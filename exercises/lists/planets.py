# Lists are very similar to arrays. They can contain any type of variable,
# and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

# lists use []
# tuples use ()

planet_list = ["Mercury", "Mars"]

# 1. Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print('Planet List Append() Jupiter/Saturn =', planet_list)

# 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])
print('Planet List Extend() =', planet_list)

# 3. Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(2, "Venus")
planet_list.insert(3, "Earth")
print('Planet List Insert() =', planet_list)

# 4. Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print('Planet List Append() Pluto =', planet_list)

# 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
terrestrial = planet_list[0:4]
# planet_list[terrestrial]
print('Terristrial Planets =', terrestrial)

# 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print('Delete Pluto =', planet_list)


# ITERATING OVER PLANETS
# 1. Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
spaceExplore = [('Cassini', 'Saturn'), ('Opportunity', 'Mars')]
# print(spaceExplore)


# 2. Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited.
for planet in planet_list:
    for satellite in spaceExplore:
        if planet == satellite[1]:
            print(satellite[1] + " has visited " + planet)
