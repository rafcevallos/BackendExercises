# HIGHER ORDER FUNCTIONS
    # a.) take another function as an argument
    # b.) return a function

    # functions == FIRST CLASS CITIZENS(objects) -- PASS 'EM AROUND


def read_my_name(func):
    name = "Slim Shady"
    name_thing = func(name)

    return name_thing

def make_a_phrase(name):
    return f'Hi.  My Name is {name}'

print(read_my_name(make_a_phrase))