# 1. Define a set that contains tuples. Each tuple should contain two strings:
#    i.)The name of an artist
#   ii.)A song by that artist

# Make sure that some of the songs are from the band Nickelback. You can see a list of their greatest hits on Amazon.

songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Radiohead', 'Karma Police'),
    ('Kendrick Lamar', 'Loyalty'),
    ('Nickelback', 'Animals')
}

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

kill_nickelback = {nickel for nickel in songs if nickel[0] != "Nickelback"}

print(kill_nickelback)