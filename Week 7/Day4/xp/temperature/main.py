import random

def get_random_temp(season):
    if season == 'winter':
        lower_limit = -10
        upper_limit = 16
    elif season == 'spring' or season == 'autumn':
        lower_limit = 0
        upper_limit = 23
    elif season == 'summer':
        lower_limit = 24
        upper_limit = 32
    else:
        lower_limit = 33
        upper_limit = 40
    
    return round(random.uniform(lower_limit, upper_limit), 1)

def main():
    season = input("Enter the season: ")
    temperature = get_random_temp(season)
    
    print(f"The temperature right now is {temperature} degrees Celsius.")
    
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 < temperature <= 23:
        print("Enjoy the pleasant weather.")
    elif 24 <= temperature <= 32:
        print("It's getting warm. Stay hydrated.")
    else:
        print("Hot day! Find some shade and keep cool.")

main()
