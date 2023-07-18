def describe_city(city, country="Unknown"):
    sentence = city + " is in " + country
    print(sentence)

# Call the function with different arguments
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("Tokyo")
