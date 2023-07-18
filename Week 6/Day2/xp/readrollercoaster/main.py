height_inches = float(input("Enter your height in inches: "))
height_cm = height_inches * 2.54

if height_cm >= 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("Sorry, you need to grow some more to ride the roller coaster.")
