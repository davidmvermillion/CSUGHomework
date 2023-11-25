# This program is a single-run if loop to determine whether a user entry is contained in either the planets
#   or dwarf_planets string list objects

# Lists of acceptable entries
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
dwarf_planets = ["Pluto", "Ceres", "Makemake", "Haumea", "Eris"]

# Single-run planet checker
planet = input('I can determine whether an object is a planet or dwarf planet.\nPlease enter the object you wish to check.\n')
if planet in planets:
    print(f'{planet} is a planet')
elif planet in dwarf_planets:
    print(f'{planet} is a dward planet')
else:
    print('Sorry, I don\'t recognize that object. Please check your spelling and try again after restarting the program.')
    