month = int(input("Enter a month (1-12): "))

if month >= 3 and month <= 5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    season = "Autumn"
else:
    season = "Winter"

print("The season of the month is:", season)
