# 1. Define a dictionary that contains information about several members of your family. Use the following example as a template.
my_family = {
    'brother': {
        'name': 'Billy Bob',
        'age': 42
    },
    'mother': {
        'name': 'Soon',
        'age': 59
    },
    'father': {
        'name': 'Luis',
        'age': 61
    }
}

# 2. Using a dictionary comprehension, produce output that looks like the following example: Krista is my sister and is 42 years old

# Standard way with a loop.  BTW, family_stuff could be a list or a tuple, too.  It doesn't matter.
family_stuff = set()
for family_member, member_values in my_family.items():
    family_stuff.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.')

print("My family!", family_stuff)

# With comprehension instead
comp_family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}

print("My family!", comp_family_stuff)