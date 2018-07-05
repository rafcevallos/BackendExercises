planet_list = ["Mercury", "Mars"]

# 1. Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

# 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])
print(planet_list)

# 3. Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(2, "Venus")
planet_list.insert(3, "Earth")
print(planet_list)

# 4. Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print(planet_list)

# 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
terrestrial = planet_list[0:4]
# planet_list[terrestrial]
print(terrestrial)

# 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print(planet_list)