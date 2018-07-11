# 1. Write a function that takes a list, a number, and a string as args.
# 2. The string parameter should have a default value.
def print_cities(cities, num, str="I have visited the city of "):
# 3. In the function body, loop over the list and output the items.
    for city in cities[:num]:
        print(str + city)

city_list = ["Atlanta", "Hobart", "Boulder", "Chicago", "Melbourne"]

# prints all 5 cities
print_cities(city_list, 5)
# prints the first city in the list
print_cities(city_list, 1, "I loved visiting ")

# 4. Use slice to loop through only the first n items in the array, where n = the value of the second argument.
some_cities = city_list[2:4]
few_cities = 

# 5. Each item should be prefaced by value of the string argument


# 6. One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "


# 7. Try it out! Execute the function both with and without passing in a value for the string parameter