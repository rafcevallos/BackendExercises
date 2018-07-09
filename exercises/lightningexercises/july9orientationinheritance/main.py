# instantiate a new DOG and pring out the results of making it speak
from dog import Dog
from pet import Pet

#Create an instance of the Dog class
jindo = Dog("Jindo")
# print(f"What's that girl? {jindo.speak()} Timmy's in a well? Oh, word!)
# print("a dog instance", jindo)

# Create an instance of the Pet class and compose the Dog instance into it by adding the dog as a roperty of the new Pet
barxton = Pet("Toni Barxton", jindo)

# Add my family as owners by calling Barxton's set_owner method
barxton.set_owner("Raffy Taffy", "555-867-5309")

# Print a hman-readable output thanks to our the __str__ method we defined in Pet
print("Here's this bullshit: ", barxton)
print("Owner shit: ", barxton.owner_name, barxton.owner_number)