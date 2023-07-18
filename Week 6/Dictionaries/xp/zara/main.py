# Step 1: Information about the brand
name = 'Zara'
creation_date = 1975
creator_name = 'Amancio Ortega Gaona'
type_of_clothes = ['men', 'women', 'children', 'home']
international_competitors = ['Gap', 'H&M', 'Benetton']
number_stores = 7000
major_color = {
    'France': ['blue'],
    'Spain': ['red'],
    'US': ['pink', 'green']
}

# Step 2: Creating the 'brand' dictionary
brand = {
    'name': name,
    'creation_date': creation_date,
    'creator_name': creator_name,
    'type_of_clothes': type_of_clothes,
    'international_competitors': international_competitors,
    'number_stores': number_stores,
    'major_color': major_color
}

# Step 3: Changing the number of stores to 2
brand['number_stores'] = 2

# Step 4: Printing a sentence about Zara's clients
print(f"Zara's clients include {', '.join(type_of_clothes)}.")

# Step 5: Adding the 'country_creation' key
brand['country_creation'] = 'Spain'

# Step 6: Checking and adding Desigual as an international competitor
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# Step 7: Deleting the information about the date of creation
del brand['creation_date']

# Step 8: Printing the last international competitor
last_competitor = brand['international_competitors'][-1]
print(f"The last international competitor is {last_competitor}.")

# Step 9: Printing the major clothes colors in the US
us_colors = brand['major_color']['US']
print(f"The major clothes colors in the US are: {', '.join(us_colors)}.")

# Step 10: Printing the amount of key-value pairs in the dictionary
num_pairs = len(brand)
print(f"The dictionary contains {num_pairs} key-value pairs.")

# Step 11: Printing the keys of the dictionary
keys = brand.keys()
print("Keys of the dictionary:")
for key in keys:
    print(key)

# Step 12: Creating the 'more_on_zara' dictionary
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# Step 13: Merging 'more_on_zara' dictionary into 'brand' dictionary
brand.update(more_on_zara)

# Step 14: Printing the value of the key 'number_stores'
print(f"The value of 'number_stores' key is: {brand['number_stores']}")
