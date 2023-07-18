def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

# Define the list of magician names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Call the show_magicians() function to print the original list
show_magicians(magician_names)

# Call the make_great() function to modify the list
make_great(magician_names)

# Call the show_magicians() function again to print the modified list
show_magicians(magician_names)
