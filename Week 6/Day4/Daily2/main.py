import datetime

# Ask the user for their birthdate
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert the birthdate string to a datetime object
birthdate_date = datetime.datetime.strptime(birthdate, "%d/%m/%Y")

# Get the current date
current_date = datetime.datetime.now()

# Calculate the age based on the difference between the current date and the birthdate
age = current_date.year - birthdate_date.year

# Check if it's a leap year
is_leap_year = False
if birthdate_date.year % 4 == 0 and (birthdate_date.year % 100 != 0 or birthdate_date.year % 400 == 0):
    is_leap_year = True

# Display the cake with candles
cake = '''
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''

candles = "i" * (age % 10)

print(cake.replace("iiiii", candles))

# Display two cakes if it's a leap year
if is_leap_year:
    print(cake.replace("iiiii", candles))
