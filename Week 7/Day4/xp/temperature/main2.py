import random

def get_random_temp(season):
    if season.lower() == "winter":
        lower_limit, upper_limit = -10, 16
    elif season.lower() == "spring" or season.lower() == "autumn" or season.lower() == "fall":
        lower_limit, upper_limit = 0, 23
    elif season.lower() == "summer":
        lower_limit, upper_limit = 24, 40
    else:
        raise ValueError("Invalid season entered. Please choose from 'winter', 'spring', 'summer', or 'autumn/fall'.")

    return round(random.uniform(lower_limit, upper_limit), 1)

def main():
    season = input("Enter the season (winter/spring/summer/autumn): ")
    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24:
        print("The weather is pleasant. Enjoy your day!")
    elif 24 <= temperature < 32:
        print("It's getting warm. Stay hydrated.")
    else:
        print("It's hot outside. Stay cool and hydrated!")

if __name__ == "__main__":
    main()
