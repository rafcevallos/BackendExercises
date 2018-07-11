
# permissions: r: read only, w: write only, (will overwrite file), a: appending to existing file w/o overriding, r+: read & write

# syntax:  def open(file, mode, buffering, encoding, errors, newline, closefd, opener)
with open("text.txt", "w") as testfile:
    testfile.write("Hello, C25. Hope you're having a great day!")

with open("test.txt", "a") as testfile:
    testfile.write("Hello, C25.  Hope you're awake!")

# If you change these sets to list, LISTS retain ORDER.   SETS do not.
nickset = {"Handsome Jake", "Jake with the good hair",
           "Swole Master General", "Fat Booty Tuesday", "Jake the Snake", "The Shirt"}

nameset = {"Jake", "Cashew", "Rachael", "Erin M.",
           "Erin A.", "Deanna", "Meghan", "Ronnie"}

with open("data/nicknames.txt", "w") as nicknames:
    for nick in nickset:
        nicknames.write(nick + '\n')

with open("data/names.txt", "w") as names:
    for name in nameset:
        names.write(name + '\n')

# later, back at the batcave...
# namelist = []
# nicklist = []
with open("data/names.txt", "r") as names:
    namelist = names.readlines()
    # print(namelist)

with open("data/nicknames.txt", "r") as nicks:
    nicklist = nicks.readlines()
    # print(nicklist)

# Handsome Jake related
jake_names = [f"{name.strip().split(' ')[0]} \"{nicklist[i].strip()}\" {name.strip().split(' ')[1]}" for i, name in enumerate(namelist)]

print(jake_names)



# is-a = INHERITANCE
# part of = COMPOSITION (THiS = FLEXIBILITY)
# has-a = AGGREGATION

#favor COMPOSITION over INHERITANCE/AGGREGATIOn because you want your data to be flexible instead of rigid.  It allows programmers to change what needs to be changed instead of the entire dataset