# A tuple is an immutable list. A tuple can not be changed in any way once it is created.

# 1	A tuple is defined in the same way as a list, except that the whole set of elements is enclosed in parentheses instead of square brackets.
# 2	The elements of a tuple have a defined order, just like a list. Tuples indices are zero-based, just like a list, so the first element of a non-empty tuple is always t[0].
# 3	Negative indices count from the end of the tuple, just as with a list.
# 4	Slicing works too, just like a list. Note that when you slice a list, you get a new list; when you slice a tuple, you get a new tuple.

# 1. Create a tuple named zoo that contains your favorite animals.
zoo = ('red panda', 'wallaby', 'ankylosaurus') #<-- tuple packing

# 2. Find one of your animals using the .index(value) method on the tuple.
index_num = zoo.index('red panda')
print('The index of red panda is:', index_num)

# 3. Determine if an animal is in your tuple by using for value in tuple.
for animal in zoo:
    if animal == 'red panda':
        print(animal)

# 4. Create a variable for each of the animals in your tuple with this cool feature of Python.
# Each animal is now a variable and not a string.  Now, we don't have to do zoo + index value
(red_panda, wallaby, ankylosaurus) = zoo
print(wallaby)

# 5. Convert your tuple into a list.
# zooList is zoo converted to list
zooList = list(zoo)
print('Zoo List =', zooList)

# 6. Use extend() to add three more animals to your zoo.
# moreZoo holes 3 additional animals to be added to zoo
moreZoo = ['skunk', 'wombat', 'dodo']
print('More Zoo =', moreZoo)

# add moreZoo to zooList to get all animals in one list
zooList.extend(moreZoo)
print('Full Zoo =', zooList)

# 7. Convert the list back into a tuple with tuple().
zooTuple = tuple(zooList)
print('Zoo Tuple =', zooTuple)