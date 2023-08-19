def calculate_age_on_planets(age_seconds):
    # Define the orbital periods relative to Earth in seconds
    orbital_periods = {
        'Earth': 365.25 * 24 * 60 * 60,
        'Mercury': 0.2408467 * 365.25 * 24 * 60 * 60,
        'Venus': 0.61519726 * 365.25 * 24 * 60 * 60,
        'Mars': 1.8808158 * 365.25 * 24 * 60 * 60,
        'Jupiter': 11.862615 * 365.25 * 24 * 60 * 60,
        'Saturn': 29.447498 * 365.25 * 24 * 60 * 60,
        'Uranus': 84.016846 * 365.25 * 24 * 60 * 60,
        'Neptune': 164.79132 * 365.25 * 24 * 60 * 60
    }

    # Calculate the age on each planet
    ages_on_planets = {planet: age_seconds / orbital_periods[planet] for planet in orbital_periods}

    return ages_on_planets

# Example usage:
age_seconds = 1000000000
ages_on_planets = calculate_age_on_planets(age_seconds)

# Print the ages on each planet
for planet, age in ages_on_planets.items():
    print(f"{planet}: {age:.2f} Earth-years old.")
